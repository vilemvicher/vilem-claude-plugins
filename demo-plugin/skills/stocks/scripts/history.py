#!/usr/bin/env python3
"""
Historical data script - fetches price history using yfinance.
Requires: pip install yfinance
"""

import sys
import json

try:
    import yfinance as yf
except ImportError:
    print(json.dumps({"error": "yfinance not installed. Run: pip install yfinance"}))
    sys.exit(1)


VALID_PERIODS = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']


def get_history(ticker: str, period: str = '1mo') -> dict:
    """
    Get historical price data.

    Args:
        ticker: Stock ticker symbol
        period: Time period (1d, 5d, 1mo, 3mo, 6mo, 1y, 5y, max)

    Returns:
        Dictionary with historical data and statistics
    """
    if period not in VALID_PERIODS:
        return {"error": f"Invalid period. Use one of: {', '.join(VALID_PERIODS)}"}

    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)

        if hist.empty:
            return {"error": f"No historical data found for: {ticker}"}

        # Convert to list of records
        records = []
        for date, row in hist.iterrows():
            records.append({
                "date": date.strftime('%Y-%m-%d'),
                "open": round(row['Open'], 2),
                "high": round(row['High'], 2),
                "low": round(row['Low'], 2),
                "close": round(row['Close'], 2),
                "volume": int(row['Volume'])
            })

        # Calculate statistics
        closes = hist['Close']
        first_close = closes.iloc[0]
        last_close = closes.iloc[-1]
        period_change = last_close - first_close
        period_change_pct = (period_change / first_close) * 100

        return {
            "ticker": ticker.upper(),
            "period": period,
            "data_points": len(records),
            "start_date": records[0]['date'],
            "end_date": records[-1]['date'],
            "statistics": {
                "start_price": round(first_close, 2),
                "end_price": round(last_close, 2),
                "change": round(period_change, 2),
                "change_percent": round(period_change_pct, 2),
                "high": round(closes.max(), 2),
                "low": round(closes.min(), 2),
                "average": round(closes.mean(), 2),
                "volatility": round(closes.std(), 2)
            },
            "history": records[-10:]  # Last 10 records for brevity
        }

    except Exception as e:
        return {"error": f"Failed to fetch history: {str(e)}"}


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: python history.py TICKER [PERIOD]"}))
        print(json.dumps({"periods": VALID_PERIODS}))
        sys.exit(1)

    ticker = sys.argv[1].upper()
    period = sys.argv[2] if len(sys.argv) > 2 else '1mo'

    result = get_history(ticker, period)
    print(json.dumps(result, indent=2))

    if "error" in result:
        sys.exit(1)


if __name__ == "__main__":
    main()
