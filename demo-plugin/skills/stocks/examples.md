# Stock Market Skill Examples

## Example 1: Basic Stock Quote

**User:** "What's Apple's stock price?"

**Claude runs:**
```bash
python scripts/quote.py AAPL
```

**Sample Output:**
```
Apple Inc. (AAPL)

Current Price: $178.52
Change: +$2.34 (+1.33%)
Status: Market Open

Today's Range: $176.18 - $179.25
Volume: 52.4M shares

Key Metrics:
- Market Cap: $2.78T
- P/E Ratio: 28.5
- 52-Week Range: $124.17 - $198.23
```

---

## Example 2: Company Research

**User:** "Tell me about NVIDIA as a company"

**Claude runs:**
```bash
python scripts/company.py NVDA
```

**Sample Output:**
```
NVIDIA Corporation (NVDA)

Sector: Technology
Industry: Semiconductors
Country: United States
Employees: 26,196

Description:
NVIDIA Corporation provides graphics and compute solutions...

Financials:
- Market Cap: $1.2T
- Revenue: $26.9B
- Profit Margin: 55.6%
- Return on Equity: 91.5%

Analyst Consensus: Strong Buy
Price Target: $650 (range: $560 - $800)
```

---

## Example 3: Historical Performance

**User:** "How has Tesla performed over the last 6 months?"

**Claude runs:**
```bash
python scripts/history.py TSLA 6mo
```

**Sample Output:**
```
Tesla (TSLA) - 6 Month Performance

Period: Jul 15, 2024 - Jan 15, 2025

Performance Summary:
- Start Price: $245.30
- Current Price: $218.75
- Change: -$26.55 (-10.82%)

Range:
- Period High: $278.98
- Period Low: $182.45
- Average: $225.60

Volatility: $18.42 (std dev)
```

---

## Example 4: Stock Comparison

**User:** "Compare AAPL, MSFT, and GOOGL"

**Claude runs:**
```bash
python scripts/compare.py AAPL MSFT GOOGL
```

**Sample Output:**
```
Stock Comparison

| Metric        | AAPL     | MSFT     | GOOGL    |
|---------------|----------|----------|----------|
| Price         | $178.52  | $378.91  | $141.25  |
| Day Change    | +1.33%   | +0.87%   | -0.42%   |
| Market Cap    | $2.78T   | $2.81T   | $1.75T   |
| P/E Ratio     | 28.5     | 35.2     | 24.8     |
| Dividend      | 0.51%    | 0.74%    | None     |

Today's Best: AAPL (+1.33%)
Today's Worst: GOOGL (-0.42%)
```

---

## Example 5: Crypto Price

**User:** "What's Bitcoin trading at?"

**Claude runs:**
```bash
python scripts/quote.py BTC-USD
```

**Note:** Crypto tickers use format `SYMBOL-USD`

---

## Example 6: Market Index

**User:** "How's the S&P 500 doing?"

**Claude runs:**
```bash
python scripts/quote.py SPY
```

**Note:** Use ETF tickers for indices (SPY for S&P 500)

---

## Trigger Phrases

The skill activates on:
- "stock price of..."
- "how is [TICKER] doing"
- "what's [COMPANY] trading at"
- "compare stocks..."
- "stock performance of..."
- "tell me about [COMPANY] stock"
- "market cap of..."
- "P/E ratio of..."
