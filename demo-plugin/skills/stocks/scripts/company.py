#!/usr/bin/env python3
"""
Company info script - fetches detailed company information using yfinance.
Requires: pip install yfinance
"""

import sys
import json

try:
    import yfinance as yf
except ImportError:
    print(json.dumps({"error": "yfinance not installed. Run: pip install yfinance"}))
    sys.exit(1)


def get_company_info(ticker: str) -> dict:
    """
    Get detailed company information.

    Args:
        ticker: Stock ticker symbol (e.g., AAPL, MSFT)

    Returns:
        Dictionary with company details
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        if not info or 'shortName' not in info:
            return {"error": f"No company info found for: {ticker}"}

        return {
            "ticker": ticker.upper(),
            "name": info.get('longName', info.get('shortName', ticker)),
            "sector": info.get('sector', 'N/A'),
            "industry": info.get('industry', 'N/A'),
            "country": info.get('country', 'N/A'),
            "website": info.get('website', 'N/A'),
            "employees": info.get('fullTimeEmployees'),
            "description": info.get('longBusinessSummary', 'No description available'),
            "financials": {
                "market_cap": info.get('marketCap'),
                "revenue": info.get('totalRevenue'),
                "profit_margin": info.get('profitMargins'),
                "operating_margin": info.get('operatingMargins'),
                "return_on_equity": info.get('returnOnEquity'),
                "debt_to_equity": info.get('debtToEquity'),
                "free_cash_flow": info.get('freeCashflow')
            },
            "dividends": {
                "dividend_rate": info.get('dividendRate'),
                "dividend_yield": info.get('dividendYield'),
                "payout_ratio": info.get('payoutRatio'),
                "ex_dividend_date": info.get('exDividendDate')
            },
            "analyst": {
                "target_price": info.get('targetMeanPrice'),
                "target_high": info.get('targetHighPrice'),
                "target_low": info.get('targetLowPrice'),
                "recommendation": info.get('recommendationKey'),
                "num_analysts": info.get('numberOfAnalystOpinions')
            }
        }

    except Exception as e:
        return {"error": f"Failed to fetch company info: {str(e)}"}


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: python company.py TICKER"}))
        sys.exit(1)

    ticker = sys.argv[1].upper()
    result = get_company_info(ticker)
    print(json.dumps(result, indent=2))

    if "error" in result:
        sys.exit(1)


if __name__ == "__main__":
    main()
