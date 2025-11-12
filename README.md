# MGIS Business Intelligence Dashboard

A comprehensive, interactive financial dashboard for analyzing business performance across multiple firms. Built with Python and Streamlit, this dashboard provides real-time insights into revenue, expenses, profit margins, and stock prices.

## Features

- 📊 **Interactive Visualizations**: Dynamic charts and graphs using Plotly
- 💰 **Financial Metrics**: Track revenue, expenses, profit, and profit margins
- 📈 **Stock Price Trends**: Monitor stock performance over time
- 🔍 **Advanced Filtering**: Filter by company and sector
- 📥 **Data Export**: Download financial data as CSV
- 🏢 **Multi-Company Analysis**: Compare performance across different firms and sectors

## Dashboard Sections

1. **Key Performance Indicators (KPIs)**: Top-level metrics showing total revenue, profit, and margins
2. **Revenue Trends**: Quarterly revenue tracking by company
3. **Profit Analysis**: Visual comparison of profitability across firms
4. **Revenue vs Expenses**: Scatter plot analysis showing efficiency
5. **Sector Performance**: Grouped comparison by industry sector
6. **Stock Prices**: Historical price trends for all companies
7. **Detailed Data Table**: Filterable, sortable financial data with export capability

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/pak8465-svg/MGIS-Business-Intelligence-Dashboard.git
cd MGIS-Business-Intelligence-Dashboard
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the dashboard with:
```bash
streamlit run dashboard.py
```

The dashboard will open automatically in your default web browser at `http://localhost:8501`

## Project Structure

```
MGIS-Business-Intelligence-Dashboard/
├── dashboard.py          # Main dashboard application
├── sample_data.py        # Financial data generator
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualization library
- **NumPy**: Numerical computing

## Customization

### Using Your Own Data

To use real financial data instead of sample data:

1. Modify `sample_data.py` to load your data from CSV, Excel, or a database
2. Ensure your data has the following columns:
   - Company
   - Ticker
   - Sector
   - Quarter/Date
   - Revenue
   - Expenses
   - Profit

### Adding New Visualizations

Edit `dashboard.py` to add new charts or metrics using Plotly Express or Plotly Graph Objects.

## Sample Data

The dashboard includes a built-in data generator that creates realistic financial data for 5 sample companies across different sectors:

- TechCorp Inc. (Technology)
- FinServ Group (Financial Services)
- HealthCare Plus (Healthcare)
- Energy Solutions (Energy)
- Retail Dynamics (Retail)

Data includes 2 years of quarterly financial performance and 6 months of daily stock prices.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on GitHub.

---

**Built with ❤️ for MGIS Business Intelligence**
