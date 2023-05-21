import requests

# Replace the base_url with the base URL of your Django project
base_url = "http://127.0.0.1:8000/weather_api"

# Replace the following with the correct API endpoint URL
url = f"{base_url}/locations/"

response = requests.get(url)

if response.status_code == 200:
    print("Successfully retrieved locations:")
    print(response.json())
else:
    print(f"Failed to retrieve locations (status code: {response.status_code})")