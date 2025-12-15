---
name: weather
description: Check current weather and forecasts for any city using Open-Meteo API. Use when the user asks about weather, temperature, forecast, rain, humidity, wind, or climate conditions for any location.
---

# Weather Skill

This skill fetches real-time weather data from the Open-Meteo API (free, no API key required, no dependencies).

## Instructions

When the user asks about weather:

### Step 1: Get Coordinates

Use WebFetch to geocode the city name:

```
URL: https://geocoding-api.open-meteo.com/v1/search?name={CITY_NAME}&count=1&language=en&format=json
Prompt: Extract the latitude, longitude, name, and country from the first result
```

**Default location** if no city specified: Prague (lat: 50.0755, lon: 14.4378)

### Step 2: Fetch Weather

Use WebFetch to get weather data with the coordinates:

```
URL: https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto&forecast_days=7
Prompt: Extract current temperature, humidity, weather conditions, wind speed, and the 7-day forecast with highs/lows
```

### Step 3: Present Results

Format the weather data nicely using the template in `templates/weather-report.md`.

## Weather Code Reference

| Code | Meaning |
|------|---------|
| 0 | Clear sky |
| 1-3 | Partly cloudy to overcast |
| 45-48 | Fog |
| 51-55 | Drizzle |
| 61-65 | Rain (slight to heavy) |
| 71-75 | Snow |
| 80-82 | Rain showers |
| 95-99 | Thunderstorm |

## Capabilities

- **Current Weather**: Temperature, feels-like, humidity, wind, conditions
- **7-Day Forecast**: Daily highs/lows and precipitation chance
- **Any Location**: Works worldwide via geocoding
- **No Dependencies**: Uses only WebFetch - nothing to install

## Error Handling

- If geocoding returns no results, ask for a more specific location
- If API fails, apologize and suggest trying again
