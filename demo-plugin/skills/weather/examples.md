# Weather Skill Examples

## Example 1: Basic Weather Query

**User:** "What's the weather in Prague?"

**Claude's Actions:**
1. WebFetch geocoding API for "Prague" → gets lat/lon
2. WebFetch weather API with coordinates
3. Present formatted results

**Sample Output:**
```
Weather in Prague, Czechia

Current Conditions:
- Temperature: 12°C (feels like 10°C)
- Conditions: Partly cloudy
- Humidity: 65%
- Wind: 15 km/h

7-Day Forecast:
| Day       | High | Low | Conditions    | Rain |
|-----------|------|-----|---------------|------|
| Monday    | 14°C | 8°C | Sunny         | 10%  |
| Tuesday   | 16°C | 9°C | Partly cloudy | 5%   |
| Wednesday | 13°C | 7°C | Rain          | 80%  |
...
```

## Example 2: Default Location (No City Specified)

**User:** "What's the weather?"

**Claude's Actions:**
1. No city specified → use Prague as default
2. Inform user: "Using Prague as the default location"
3. Fetch and present weather

## Example 3: Weather Comparison

**User:** "Compare weather between Prague and London"

**Claude's Actions:**
1. Geocode both cities (can do in parallel)
2. Fetch weather for both locations
3. Present side-by-side comparison table

**Sample Output:**
```
Weather Comparison

              Prague          London
Temperature:  12°C            15°C
Feels like:   10°C            13°C
Humidity:     65%             78%
Conditions:   Partly cloudy   Overcast
Wind:         15 km/h         20 km/h
```

## Example 4: Rain/Precipitation Focus

**User:** "Will it rain in Prague this week?"

**Claude's Actions:**
1. Use default Prague coordinates
2. Focus on precipitation_probability_max in response
3. Highlight rainy days

**Sample Output:**
```
Prague Rain Forecast

Monday:    10% - Dry
Tuesday:   5%  - Dry
Wednesday: 80% - Rain expected
Thursday:  45% - Possible showers
Friday:    15% - Mostly dry
```

## Example 5: Unknown City Handling

**User:** "Weather in Asdfville"

**Claude's Actions:**
1. Geocoding returns no results
2. Inform user: "I couldn't find 'Asdfville'. Could you check the spelling or provide a more specific location?"

## Trigger Phrases

The skill activates on keywords like:
- "weather in..."
- "temperature in..."
- "forecast for..."
- "will it rain..."
- "how hot/cold is..."
- "humidity in..."
- "what's it like outside in..."
