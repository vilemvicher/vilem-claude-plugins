# Weather Skill Reference

## API Information

This skill uses the **Open-Meteo API** - a free, open-source weather API.

- **Website**: https://open-meteo.com
- **API Key**: Not required
- **Rate Limit**: 10,000 requests/day
- **Coverage**: Worldwide

## API Endpoints

### Geocoding API

Converts city names to coordinates.

**URL:**
```
https://geocoding-api.open-meteo.com/v1/search?name={CITY}&count=1&language=en&format=json
```

**Response:**
```json
{
  "results": [{
    "name": "Prague",
    "latitude": 50.08804,
    "longitude": 14.42076,
    "country": "Czechia",
    "timezone": "Europe/Prague"
  }]
}
```

### Weather API

Fetches current weather and forecast.

**URL:**
```
https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto&forecast_days=7
```

**Response Structure:**
```json
{
  "current": {
    "temperature_2m": 12.5,
    "relative_humidity_2m": 72,
    "apparent_temperature": 10.8,
    "weather_code": 2,
    "wind_speed_10m": 15.3
  },
  "daily": {
    "time": ["2024-01-15", "2024-01-16", ...],
    "temperature_2m_max": [14, 16, ...],
    "temperature_2m_min": [8, 9, ...],
    "weather_code": [2, 3, ...],
    "precipitation_probability_max": [10, 45, ...]
  }
}
```

## Weather Codes (WMO Standard)

| Code | Description |
|------|-------------|
| 0 | Clear sky |
| 1 | Mainly clear |
| 2 | Partly cloudy |
| 3 | Overcast |
| 45 | Foggy |
| 48 | Depositing rime fog |
| 51 | Light drizzle |
| 53 | Moderate drizzle |
| 55 | Dense drizzle |
| 61 | Slight rain |
| 63 | Moderate rain |
| 65 | Heavy rain |
| 71 | Slight snow |
| 73 | Moderate snow |
| 75 | Heavy snow |
| 80 | Slight rain showers |
| 81 | Moderate rain showers |
| 82 | Violent rain showers |
| 95 | Thunderstorm |
| 96 | Thunderstorm with slight hail |
| 99 | Thunderstorm with heavy hail |

## Common Locations (Quick Reference)

| City | Latitude | Longitude |
|------|----------|-----------|
| Prague | 50.0755 | 14.4378 |
| London | 51.5074 | -0.1278 |
| New York | 40.7128 | -74.0060 |
| Tokyo | 35.6762 | 139.6503 |
| Sydney | -33.8688 | 151.2093 |
| Paris | 48.8566 | 2.3522 |

## Additional Parameters

For Fahrenheit, add `&temperature_unit=fahrenheit` to the weather URL.
