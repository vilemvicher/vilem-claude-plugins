#!/usr/bin/env python3
"""
Stock comparison script - compares multiple stocks side by side.
Requires: pip install yfinance
"""

import sys
import json

try:
    import yfinance as yf
except ImportError:
    print(json.dumps({"error": "yfinance not installed. Run: pip install yfinance"}))
    sys.exit(1)


def get_stock_data(ticker: str) -> dict:
    """Get key metrics for a single stock."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        if not info or info.get('regularMarketPrice') is None:
            return {"ticker": ticker, "error": "Invalid ticker"}

        current = info.get('regularMarketPrice', 0)
        prev = info.get('previousClose', 0)
        change_pct = ((current - prev) / prev * 100) if prev else 0

        return {
            "ticker": ticker.upper(),
            "name": info.get('shortName', ticker),
            "price": round(current, 2),
            "change_percent": round(change_pct, 2),
            "market_cap": info.get('marketCap'),
            "pe_ratio": info.get('trailingPE'),
            "dividend_yield": info.get('dividendYield'),
            "52w_change": info.get('52WeekChange'),
            "volume": info.get('volume'),
            "sector": info.get('sector', 'N/A')
        }
    except Exception as e:
        return {"ticker": ticker, "error": str(e)}


def compare_stocks(tickers: list) -> dict:
    """
    Compare multiple stocks.

    Args:
        tickers: List of ticker symbols

    Returns:
        Dictionary with comparison data
    """
    if len(tickers) < 2:
        return {"error": "Need at least 2 tickers to compare"}

    if len(tickers) > 10:
        return {"error": "Maximum 10 tickers allowed"}

    results = []
    for ticker in tickers:
        data = get_stock_data(ticker.upper())
        results.append(data)

    # Find best/worst performers
    valid_results = [r for r in results if 'error' not in r]

    if not valid_results:
        return {"error": "No valid tickers found", "results": results}

    best_day = max(valid_results, key=lambda x: x.get('change_percent', 0))
    worst_day = min(valid_results, key=lambda x: x.get('change_percent', 0))

    return {
        "comparison": results,
        "summary": {
            "best_performer_today": {
                "ticker": best_day['ticker'],
                "change": best_day['change_percent']
            },
            "worst_performer_today": {
                "ticker": worst_day['ticker'],
                "change": worst_day['change_percent']
            },
            "total_stocks": len(tickers),
            "valid_stocks": len(valid_results)
        }
    }


def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Usage: python compare.py TICKER1 TICKER2 [TICKER3...]"}))
        sys.exit(1)

    tickers = sys.argv[1:]
    result = compare_stocks(tickers)
    print(json.dumps(result, indent=2))

    if "error" in result:
        sys.exit(1)


if __name__ == "__main__":
    main()
