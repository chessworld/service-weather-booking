import urllib.request
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime
import logging

# from ..models import WeatherOption, Location

PLACES_USER_AGENT = \
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
    '(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'


def search_location(search='', select=0):
    """
    Returns search result list or [] if no matches or if the search string was ''.

    Example https://api.weather.bom.gov.au/v1/locations?search=3130
            https://api.weather.bom.gov.au/v1/locations?search=Parkville+VIC

    Multiple matching records are returned. If suburb and state are specified then
    selecting the first element should be sufficient.

    If no match is found an empty list is returned and self.gohash is None.
    
    data:[{geohash, id, name, postcode, state},]

    geohash     e.g. 'r1r143n'
    id          e.g. 'Parkville (Vic.)-r1r143n'
    name        e.g. 'Parkville'
    state       e.g. 'VIC'

    Location is returned as a 6 character precision geohash such as '1r143n'.
    (https://en.wikipedia.org/wiki/Geohash)
    """

    # The search API doesn't like the dash character.
    search = search.replace('-', '+')

    data = _fetch_json(f'https://api.weather.bom.gov.au/v1/locations?search={search}')
    locations = data['data']
    
    logging.info(locations)
    return locations



def get_station(loc):
    geohash = loc['geohash'][:-1]
    url = f'https://api.weather.bom.gov.au/v1/locations/{geohash}/observations'
    result = _fetch_json(url)
    station = result['data']['station']
    
    url = f"http://www.bom.gov.au/places/{loc['state'].lower()}/{loc['name'].lower()}"
    print(url)
    req = urllib.request.Request(url, data=None, headers={'User-Agent': PLACES_USER_AGENT})
    page_html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(page_html, 'html.parser')
    station_p = soup.find('p', 'station-id')    
    wmo_id = station_p.contents[0][4:] if len(station_p.contents) > 0 else None
    station['wmo_id'] = wmo_id
    
    print(station)
    return station


def _fetch_json(url):
    req = urllib.request.Request(url, data=None, headers={'User-Agent': PLACES_USER_AGENT})
    json_text = urllib.request.urlopen(req).read().decode()
    result =  json.loads(json_text)
    return result


def get_station_details(link):
    url = 'http://www.bom.gov.au' + link
    req = urllib.request.Request(url, data=None, headers={'User-Agent': PLACES_USER_AGENT})
    page_html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(page_html, 'html.parser')

    station_details = {}
    station_details_table = soup.find('table', {'class': 'stationdetails'})

    for cell in station_details_table.find_all('td'):
        if "Station Details" not in cell.get_text():
            attribute, value = cell.get_text().split(": ", 1)
            station_details[attribute] = value

    print(f'Station Details: {station_details}')
    return station_details


def get_observations(state, station_name, wmo_id):
    page = 'canberra' if state.lower() == 'act' else f'{state.lower()}all'
    url = f'http://www.bom.gov.au/{state.lower()}/observations/{page}.shtml'
    req = urllib.request.Request(url, data=None, headers={'User-Agent': PLACES_USER_AGENT})
    page_html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(page_html, 'html.parser')

    for table in soup.find_all('table'):
        for row in table.find_all('tr'):
            header = row.find('th')
            if header and station_name in header.get_text():
                link = header.find('a')
                break

    if link:
        link_address = link['href']
        print(f"The link for {station_name} is: {link_address}")
    else:
        print(f"No link found for {station_name}")
    

    get_station_details(link_address)

        
    # Use regular expression to extract the key and number
    match = re.search(r'products/(\w+)/\w+\.(\d+)', link_address)
    product_id = match.group(1)

    if str(match.group(2)) != str(wmo_id):
        print("WARNING: wmo id does not match")

    wmo_id = match.group(2)

    url = f'http://www.bom.gov.au/fwo/{product_id}/{product_id}.{wmo_id}.json'
    data = _fetch_json(url)
    

    ## TESTING
    
    # # Accessing the notice details
    # notice = data['observations']['notice'][0]
    # copyright = notice['copyright']
    # copyright_url = notice['copyright_url']
    # disclaimer_url = notice['disclaimer_url']
    # feedback_url = notice['feedback_url']
    # print("Notice details:")
    # print("Copyright:", copyright)
    # print("Copyright URL:", copyright_url)
    # print("Disclaimer URL:", disclaimer_url)
    # print("Feedback URL:", feedback_url)

    # # Accessing the header details
    # header = data['observations']['header'][0]
    # refresh_message = header['refresh_message']
    # ID = header['ID']
    # name = header['name']
    # state_time_zone = header['state_time_zone']
    # print("\nHeader details:")
    # print("Refresh Message:", refresh_message)
    # print("ID:", ID)
    # print("Name:", name)
    # print("State Time Zone:", state_time_zone)

    # # Accessing the data
    # data_items = data['observations']['data']
    # print("\nData details:")
    # for item in data_items:
    #     print("Name:", item['name'])
    #     print("Local Date Time:", item['local_date_time'])
    #     print("Wind Speed (km/h):", item['wind_spd_kmh'])
    #     print("Temperature (C):", item['air_temp'])
    #     print("-" * 20)
        
    
    return data['observations']['data']


def get_weather(start_time, end_time, postcode):
    postcode = str(postcode)
    loc = search_location(postcode)[0]
    station = get_station(loc)
    state, stn_name, wmo_id = loc['state'], station['name'], station['wmo_id']  # get weather station details

    all_observations = get_observations(state, stn_name, wmo_id)    # observations
    
    
    def _convert_time(local_date_time_str) -> bool:        
        # Extracting day and time
        day, time_str = local_date_time_str.split('/')
        time_str = time_str.replace('pm', ' PM').replace('am', ' AM')

        # Using current month and year
        current_year = datetime.now().year
        current_month = datetime.now().month

        # Combining the date and time
        date_time_str = f"{current_year}-{current_month}-{day} {time_str}"

        # Parsing the date_time_str using strptime
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %I:%M %p')

        return date_time_obj
    
    
    def _check_range(val, start=None, end=None):
        """
        Returns: 0 if between the range (inclusive) else False.

        If start or end is None, then no upper/lower bound
        Example: if start=None, end=None then always True

        Args:
            val: value to check
            start: lower bound or None
            end: upper bound or None

        Returns:
           -1 if less than lower bound
           1 if greater than upper bound
           0 if between upper and lower bounds (inclusive)
        """
        
        if start is not None and val < start:
            return -1
        if end is not None and val > end:
            return 1
        return 0
    
    
    observations = [obvservation for obvservation in all_observations if not _check_range(_convert_time(obvservation['local_date_time']), start=start_time, end=end_time)]
    
    def _get_weather_option(observation):
        get_option = lambda val, start, end, options: options[_check_range(val, start=start, end=end)+1]
        
        # Temperature option
        temperature = get_option(
            observation['air_temp'],
            10,
            20,
            ('Cool', 'Warm', 'Hot')
            )
        
        # Wind option
        wind = get_option(
            observation['wind_spd_kmh'],
            20,
            30,
            ('No Wind', 'Calm', 'Windy')
            )
        
        # Check clouds
        clouds_oktas = observation['cloud_oktas']
        clouds_oktas = 0 if not clouds_oktas or clouds_oktas == '-' else float(clouds_oktas)
        # Rain
        rain = observation['rain_trace']
        rain = 0.0 if not rain or rain == '-' else float(rain)
        
        weather_type = 'Cloudy' if clouds_oktas > 3 else 'Rainy' if rain > 0 else 'Sunny'
        
        if wind == 'Windy' and clouds_oktas > 5 and weather_type == 'Rainy':
            weather_type = 'Stormy'
        
        weather_option = {
            'weather_type': weather_type,
            'temperature': temperature,
            'wind': wind
            }
        
        return weather_option
    
    weather_options = [_get_weather_option(observation) for observation in observations]
    
    return weather_options

# postcode = 3130
# now = datetime.now()
# start_time = datetime(now.year, now.month, now.day,9)
# end_time = datetime(now.year, now.month, now.day, 18)

# weather_options = get_weather(start_time=start_time, end_time=end_time, postcode=postcode)

# count = lambda key, val, items: len([item for item in items if item[key] == val])

# print(weather_options)
# print(count('wind', 'No Wind', weather_options))
