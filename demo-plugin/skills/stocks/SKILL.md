---
name: stocks
description: Get real-time stock prices, company info, and market data using Yahoo Finance. Use when the user asks about stocks, share prices, market performance, tickers, or wants to analyze company financials.
---

# Stock Market Skill

This skill fetches real-time stock market data using the `yfinance` Python library.

## Prerequisites

Install the required dependency:
```bash
pip install yfinance
```

## Instructions

When the user asks about stocks:

### 1. Get Current Stock Price

```bash
python scripts/quote.py TICKER
```

Example: `python scripts/quote.py AAPL`

Returns current price, day change, volume, and key metrics.

### 2. Get Company Information

```bash
python scripts/company.py TICKER
```

Returns company name, sector, industry, description, and key stats.

### 3. Get Historical Data

```bash
python scripts/history.py TICKER [PERIOD]
```

Periods: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `5y`, `max`

Example: `python scripts/history.py MSFT 1mo`

### 4. Compare Multiple Stocks

```bash
python scripts/compare.py TICKER1 TICKER2 [TICKER3...]
```

Example: `python scripts/compare.py AAPL MSFT GOOGL`

## Common Tickers

| Company | Ticker |
|---------|--------|
| Apple | AAPL |
| Microsoft | MSFT |
| Google | GOOGL |
| Amazon | AMZN |
| Tesla | TSLA |
| NVIDIA | NVDA |
| Meta | META |

## Error Handling

- Invalid ticker: Inform user and suggest checking the symbol
- Network error: Suggest trying again
- Market closed: Show last available price with timestamp

## Output Format

Present data in clean tables with:
- Currency symbols ($)
- Percentage changes with +/- indicators
- Color hints: mention if stock is up (green) or down (red)
