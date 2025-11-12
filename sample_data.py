"""
Sample Financial Data Generator
Generates realistic financial data for demonstration purposes
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_financial_data():
    """Generate sample financial data for multiple firms"""

    # Define companies
    companies = [
        {"name": "TechCorp Inc.", "ticker": "TECH", "sector": "Technology"},
        {"name": "FinServ Group", "ticker": "FNSV", "sector": "Financial Services"},
        {"name": "HealthCare Plus", "ticker": "HLTH", "sector": "Healthcare"},
        {"name": "Energy Solutions", "ticker": "ENRG", "sector": "Energy"},
        {"name": "Retail Dynamics", "ticker": "RETL", "sector": "Retail"},
    ]

    # Generate quarterly data for the last 2 years
    quarters = pd.date_range(end=datetime.now(), periods=8, freq='Q')

    all_data = []

    for company in companies:
        # Base values vary by company
        base_revenue = np.random.uniform(50, 200)  # Million USD
        growth_rate = np.random.uniform(0.02, 0.08)  # 2-8% quarterly growth
        profit_margin = np.random.uniform(0.10, 0.25)  # 10-25% profit margin

        for i, quarter in enumerate(quarters):
            # Add some randomness to simulate real business fluctuations
            revenue = base_revenue * (1 + growth_rate) ** i * np.random.uniform(0.95, 1.05)
            expenses = revenue * (1 - profit_margin) * np.random.uniform(0.98, 1.02)
            profit = revenue - expenses

            all_data.append({
                "Company": company["name"],
                "Ticker": company["ticker"],
                "Sector": company["sector"],
                "Quarter": quarter.strftime("%Y-Q%q"),
                "Date": quarter,
                "Revenue": round(revenue, 2),
                "Expenses": round(expenses, 2),
                "Profit": round(profit, 2),
                "Profit_Margin": round((profit / revenue) * 100, 2)
            })

    return pd.DataFrame(all_data)

def generate_stock_prices():
    """Generate sample stock price data"""

    companies = ["TECH", "FNSV", "HLTH", "ENRG", "RETL"]
    dates = pd.date_range(end=datetime.now(), periods=180, freq='D')

    all_prices = []

    for ticker in companies:
        # Starting price
        price = np.random.uniform(50, 300)

        for date in dates:
            # Random walk with slight upward bias
            change = np.random.normal(0.001, 0.02)  # 0.1% drift, 2% volatility
            price = price * (1 + change)

            all_prices.append({
                "Ticker": ticker,
                "Date": date,
                "Price": round(price, 2)
            })

    return pd.DataFrame(all_prices)

def get_company_metrics():
    """Get latest metrics for all companies"""

    df = generate_financial_data()
    latest = df.groupby('Company').last().reset_index()

    return latest[['Company', 'Ticker', 'Sector', 'Revenue', 'Profit', 'Profit_Margin']]
