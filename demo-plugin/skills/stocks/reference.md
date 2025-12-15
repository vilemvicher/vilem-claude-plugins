# Stock Market Skill Reference

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| yfinance | >=0.2.0 | Yahoo Finance API wrapper |

### Installation

```bash
pip install -r requirements.txt
# or
pip install yfinance
```

## Scripts

### quote.py

Get current stock price and key metrics.

```bash
python scripts/quote.py TICKER
```

**Output fields:**
- `price` - Current market price
- `change` - Dollar change from previous close
- `change_percent` - Percentage change
- `day_high` / `day_low` - Intraday range
- `volume` - Trading volume
- `market_cap` - Market capitalization
- `pe_ratio` - Price to earnings ratio
- `52_week_high` / `52_week_low` - Annual range
- `market_state` - PRE, REGULAR, POST, CLOSED

---

### company.py

Get detailed company information.

```bash
python scripts/company.py TICKER
```

**Output fields:**
- Company name, sector, industry, country
- Website, employee count
- Business description
- Financial metrics (margins, ROE, debt ratios)
- Dividend information
- Analyst recommendations and price targets

---

### history.py

Get historical price data.

```bash
python scripts/history.py TICKER [PERIOD]
```

**Periods:**
| Period | Description |
|--------|-------------|
| `1d` | 1 day (intraday) |
| `5d` | 5 days |
| `1mo` | 1 month (default) |
| `3mo` | 3 months |
| `6mo` | 6 months |
| `1y` | 1 year |
| `2y` | 2 years |
| `5y` | 5 years |
| `ytd` | Year to date |
| `max` | All available |

**Output includes:**
- OHLCV data (Open, High, Low, Close, Volume)
- Period statistics (change, high, low, average, volatility)

---

### compare.py

Compare multiple stocks side by side.

```bash
python scripts/compare.py TICKER1 TICKER2 [TICKER3...]
```

**Features:**
- Up to 10 stocks at once
- Identifies best/worst daily performers
- Shows key metrics for comparison

## Popular Tickers

### Tech Giants (FAANG+)
| Company | Ticker |
|---------|--------|
| Apple | AAPL |
| Microsoft | MSFT |
| Google/Alphabet | GOOGL |
| Amazon | AMZN |
| Meta | META |
| Netflix | NFLX |
| NVIDIA | NVDA |
| Tesla | TSLA |

### Indices (via ETFs)
| Index | ETF Ticker |
|-------|------------|
| S&P 500 | SPY |
| NASDAQ 100 | QQQ |
| Dow Jones | DIA |
| Russell 2000 | IWM |

### International
| Company | Ticker |
|---------|--------|
| Toyota | TM |
| Samsung (ADR) | SSNLF |
| TSMC | TSM |
| Alibaba | BABA |

## Market Hours

- **Pre-market**: 4:00 AM - 9:30 AM ET
- **Regular**: 9:30 AM - 4:00 PM ET
- **After-hours**: 4:00 PM - 8:00 PM ET
- **Closed**: Weekends and US holidays

## Data Limitations

- Real-time quotes may have 15-minute delay for some exchanges
- Some international stocks may have limited data
- Cryptocurrency tickers use format: `BTC-USD`, `ETH-USD`
