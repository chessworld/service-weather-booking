# Weather Booking API

The Weather Booking API allows users to book the weather for a specific date and location in Australia. Users can also view their booking history, share their bookings to social media platforms, and provide feedback.

## Getting Started

To use the Weather Booking API, you need to register as a user and obtain an API key. You can register by filling out this form: https://weatherbooking.com/register

You will receive an email with your API key and a unique guest ID. You will need to use these credentials to authenticate your requests to the API.

The base URL for the Weather Booking API is:

`https://api.weatherbooking.com/v1`

All requests and responses are in JSON format.

## Authentication

The Weather Booking API uses API keys to authenticate requests. You can view and manage your API keys in your account dashboard.

Your API keys carry many privileges, so be sure to keep them secure. Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.

Authentication to the API is performed via HTTP Basic Auth. Provide your API key as the basic auth username value. You do not need to provide a password.

For example, if your API key is `sk_test_4eC39HqLyjWDarjtT1zdp7dc`, then you can authenticate with a request header like this:

`Authorization: Basic c2tfdGVzdF80ZUMzOUhxTHlqV0Rhcmp0VDF6ZHA3ZGM6`

Alternatively, you can also provide your API key in the query string of your request:

`https://api.weatherbooking.com/v1/bookings?api_key=sk_test_4eC39HqLyjWDarjtT1zdp7dc`

However, this method is less secure and not recommended.

## Errors

The Weather Booking API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the 2xx range indicate success, codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a booking failed, etc.), and codes in the 5xx range indicate an error with our servers (these are rare).

Some common error codes are:

- 400 Bad Request – The request was unacceptable, often due to missing a required parameter.
- 401 Unauthorized – No valid API key provided.
- 403 Forbidden – The API key doesn't have permissions to perform that request.
- 404 Not Found – The requested resource doesn't exist.
- 409 Conflict – The request conflicts with another request (perhaps due to using the same idempotent key).
- 429 Too Many Requests – Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
- 500 Internal Server Error – Something went wrong on our end. (These are rare.)

When an error occurs, the API will return an error object with details about what went wrong. For example:

```json
{
  "error": {
    "code": "invalid_parameter",
    "message": "The booking date must be in the future.",
    "param": "booking_date"
  }
}
```

## Endpoints

The Weather Booking API has the following endpoints:

- /bookings – Create, retrieve, update, and delete bookings
- /locations – Retrieve a list of available locations
- /weather_options – Retrieve a list of available weather options
- /feedback – Submit feedback
- /share – Share a booking to a social media platform

Each endpoint will be described in detail below.

### Bookings

#### Create a booking

To create a booking, send a `POST` request to `/bookings` with the following parameters:

- `guest_id` (required) – The unique guest ID assigned to you when you registered.
- `location_id` (required) – The ID of the location you want to book. You can get a list of available locations from `/locations`.
- `booking_date` (required) – The date you want to book the weather for. It must be in the future and in YYYY-MM-DD format.
- `weather_id` (required) – The ID of the weather option you want to book. You can get a list of available weather options from `/weather_options`.

For example:

```json
{
  "guest_id": "g123456",
  "location_id": "l234567",
  "location_name": "Sydney",
  "booking_date": "2023-05-01",
  "weather_id": "w345678",
  "weather_option": "Sunny",
  "temperature": "Hot",
  "wind": "No wind",
  }
```


#### Retrieve a booking

To retrieve a booking, send a `GET` request to `/bookings/:booking_id` with the following parameter:

- `booking_id` (required) – The ID of the booking you want to retrieve.

For example:

`GET https://api.weatherbooking.com/v1/bookings/b789012`

The response will contain the booking details, such as:

```json
{
  "id": "b789012",
  "guest_id": "g123456",
  "location_id": "l234567",
  "location_name": "Sydney",
  "booking_date": "2023-05-01",
  "weather_id": "w345678",
  "weather_option": "Sunny",
  "temperature": "Hot",
  "wind": "No wind",
  "booking_status": "pending",
  "result_weather_id": null
}
```

#### Update a booking

To update a booking, send a `PATCH` request to `/bookings/:booking_id` with the following parameter:

- `booking_id` (required) – The ID of the booking you want to update.

You can also provide any of the following parameters to change the booking details:

- `location_id` – The ID of the new location you want to book.
- `booking_date` – The new date you want to book the weather for. It must be in the future and in YYYY-MM-DD format.
- `weather_id` – The ID of the new weather option you want to book.

For example:


PATCH https://api.weatherbooking.com/v1/bookings/b789012
```json
{
  "location_id": "",
  "booking_date": "",
  "weather_id":"",
}
```

#### Delete a booking

To delete a booking, send a `DELETE` request to `/bookings/:booking_id` with the following parameter:

- `booking_id` (required) – The ID of the booking you want to delete.

For example:

`DELETE https://api.weatherbooking.com/v1/bookings/b789012`

The response will contain a confirmation message, such as:

```json
{
  "message": "Booking deleted successfully."
}
```

#### List all bookings

To list all bookings for a guest, send a `GET` request to `/bookings` with the following parameter:

- `guest_id` (required) – The unique guest ID assigned to you when you registered.

For example:

`GET https://api.weatherbooking.com/v1/bookings?guest_id=g123456`

The response will contain an array of booking objects, such as:

```json
[
  {
    "id": "b789012",
    "guest_id": "g123456",
    "location_id": "l234567",
    "location_name": "Sydney",
    "booking_date": "2023-05-01",
    "weather_id": "w345678",
    "weather_option": "Sunny",
    "temperature": "Hot",
    "wind": "No wind",
    "booking_status": "pending",
    "result_weather_id": null
  }
  ]
```

### Locations

#### Retrieve a list of locations

To retrieve a list of available locations for booking, send a `GET` request to `/locations`.

For example:

`GET https://api.weatherbooking.com/v1/locations`

The response will contain an array of location objects, such as:

```json
[
  {
    "id": "l234567",
    "suburb": "Sydney",
    "state": "NSW",
    "postcode": "2000",
    "country": "Australia"
  },
  {
    "id": "l456789",
    "suburb": "Melbourne",
    "state": "VIC",
    "postcode": "3000",
    "country": "Australia"
  }
  ]
 ```


### Weather Options

#### Retrieve a list of weather options

To retrieve a list of available weather options for booking, send a `GET` request to `/weather_options`.

For example:

`GET https://api.weatherbooking.com/v1/weather_options`

The response will contain an array of weather option objects, such as:

```json
[
  {
    "id": "w345678",
    "weather_option": "Sunny",
    "temperature": "Hot",
    "wind": "No wind"
  },
  {
    "id": "w567890",
    "weather_option": "Cloudy",
    "temperature": "Moderate",
    "wind": "Light breeze"
  }
 ]
```

### Feedback

#### Submit feedback

To submit feedback about the app or the service, send a `POST` request to `/feedback` with the following parameters:

- `guest_id` (required) – The unique guest ID assigned to you when you registered.
- `name` (optional) – Your name. If not provided, the feedback will be anonymous.
- `email` (optional) – Your email address. If not provided, the app creators will not be able to contact you for further feedback.
- `message` (required) – Your feedback message. It should be concise and constructive.

For example:

```json
{
  "guest_id": "g123456",
  "name": "Alice",
  "email": "alice@example.com",
  "message": "I love this app! It's so fun and easy to use. I wish I could book the weather for more than one day at a time."
}
```

The response will contain a confirmation message, such as:

```json
{
  "message": "Thank you for your feedback. We appreciate your support."
}
```

### Share

#### Share a booking to a social media platform

To share a booking to a social media platform, send a `POST` request to `/share` with the following parameters:

- `guest_id` (required) – The unique guest ID assigned to you when you registered.
- `booking_id` (required) – The ID of the booking you want to share.
- `platform` (required) – The name of the social media platform you want to share to. It can be one of the following: Facebook, Twitter, Instagram, or LinkedIn.

For example:

```json
{
  "guest_id": "g123456",
  "booking_id": "b789012",
  "platform": "Facebook"
}
```

The response will contain a confirmation message and a link to the shared post, such as:

```json
{
  "message": "Your booking has been shared successfully.",
  "link": ""
}