# Weather Report Template

Use this format when presenting weather data:

---

## Weather in {city_name}, {country}

### Current Conditions
| Metric | Value |
|--------|-------|
| Temperature | {temperature}{unit} |
| Feels Like | {feels_like}{unit} |
| Conditions | {weather_description} |
| Humidity | {humidity}% |
| Wind | {wind_speed} {wind_unit} |

### 7-Day Forecast

| Day | High | Low | Conditions | Rain % |
|-----|------|-----|------------|--------|
| {day_1} | {max_1} | {min_1} | {desc_1} | {rain_1}% |
| {day_2} | {max_2} | {min_2} | {desc_2} | {rain_2}% |
| ... | ... | ... | ... | ... |

---

**Data Source:** Open-Meteo API
**Timezone:** {timezone}
