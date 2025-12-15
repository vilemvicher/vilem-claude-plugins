#!/usr/bin/env python3
"""
Stock quote script - fetches current price and key metrics using yfinance.
Requires: pip install yfinance
"""

import sys
import json

try:
    import yfinance as yf
except ImportError:
    print(json.dumps({"error": "yfinance not installed. Run: pip install yfinance"}))
    sys.exit(1)


def get_quote(ticker: str) -> dict:
    """
    Get current stock quote and key metrics.

    Args:
        ticker: Stock ticker symbol (e.g., AAPL, MSFT)

    Returns:
        Dictionary with price data and metrics
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        # Check if valid ticker
        if not info or info.get('regularMarketPrice') is None:
            # Try fast_info as fallback
            fast = stock.fast_info
            if hasattr(fast, 'last_price') and fast.last_price:
                return {
                    "ticker": ticker.upper(),
                    "price": round(fast.last_price, 2),
                    "currency": getattr(fast, 'currency', 'USD'),
                    "note": "Limited data available for this ticker"
                }
            return {"error": f"Invalid ticker symbol: {ticker}"}

        # Calculate change
        current_price = info.get('regularMarketPrice', 0)
        previous_close = info.get('previousClose', 0)
        change = current_price - previous_close if previous_close else 0
        change_percent = (change / previous_close * 100) if previous_close else 0

        return {
            "ticker": ticker.upper(),
            "name": info.get('shortName', info.get('longName', ticker)),
            "price": round(current_price, 2),
            "currency": info.get('currency', 'USD'),
            "change": round(change, 2),
            "change_percent": round(change_percent, 2),
            "day_high": info.get('dayHigh'),
            "day_low": info.get('dayLow'),
            "volume": info.get('volume'),
            "market_cap": info.get('marketCap'),
            "pe_ratio": info.get('trailingPE'),
            "52_week_high": info.get('fiftyTwoWeekHigh'),
            "52_week_low": info.get('fiftyTwoWeekLow'),
            "exchange": info.get('exchange'),
            "market_state": info.get('marketState', 'UNKNOWN')
        }

    except Exception as e:
        return {"error": f"Failed to fetch data: {str(e)}"}


def format_number(num):
    """Format large numbers with K, M, B suffixes."""
    if num is None:
        return "N/A"
    if num >= 1_000_000_000_000:
        return f"${num/1_000_000_000_000:.2f}T"
    if num >= 1_000_000_000:
        return f"${num/1_000_000_000:.2f}B"
    if num >= 1_000_000:
        return f"${num/1_000_000:.2f}M"
    if num >= 1_000:
        return f"${num/1_000:.2f}K"
    return f"${num:.2f}"


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: python quote.py TICKER"}))
        sys.exit(1)

    ticker = sys.argv[1].upper()
    result = get_quote(ticker)
    print(json.dumps(result, indent=2))

    if "error" in result:
        sys.exit(1)


if __name__ == "__main__":
    main()
