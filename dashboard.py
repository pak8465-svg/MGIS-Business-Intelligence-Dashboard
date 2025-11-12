"""
MGIS Business Intelligence Dashboard
A comprehensive financial dashboard for analyzing firm performance
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sample_data import generate_financial_data, generate_stock_prices, get_company_metrics

# Page configuration
st.set_page_config(
    page_title="MGIS Business Intelligence Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown('<p class="main-header">📊 MGIS Business Intelligence Dashboard</p>', unsafe_allow_html=True)
st.markdown("---")

# Load data
@st.cache_data
def load_data():
    financial_data = generate_financial_data()
    stock_data = generate_stock_prices()
    metrics = get_company_metrics()
    return financial_data, stock_data, metrics

financial_data, stock_data, metrics = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Company filter
companies = ["All"] + sorted(financial_data['Company'].unique().tolist())
selected_company = st.sidebar.selectbox("Select Company", companies)

# Sector filter
sectors = ["All"] + sorted(financial_data['Sector'].unique().tolist())
selected_sector = st.sidebar.selectbox("Select Sector", sectors)

# Apply filters
filtered_data = financial_data.copy()
if selected_company != "All":
    filtered_data = filtered_data[filtered_data['Company'] == selected_company]
if selected_sector != "All":
    filtered_data = filtered_data[filtered_data['Sector'] == selected_sector]

# Key Metrics Section
st.header("📈 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_revenue = filtered_data['Revenue'].sum()
    st.metric(
        label="Total Revenue",
        value=f"${total_revenue:,.0f}M",
        delta=f"{filtered_data['Revenue'].pct_change().mean()*100:.1f}%"
    )

with col2:
    total_profit = filtered_data['Profit'].sum()
    st.metric(
        label="Total Profit",
        value=f"${total_profit:,.0f}M",
        delta=f"{filtered_data['Profit'].pct_change().mean()*100:.1f}%"
    )

with col3:
    avg_margin = filtered_data['Profit_Margin'].mean()
    st.metric(
        label="Avg Profit Margin",
        value=f"{avg_margin:.1f}%"
    )

with col4:
    num_companies = filtered_data['Company'].nunique()
    st.metric(
        label="Companies",
        value=num_companies
    )

st.markdown("---")

# Two column layout for charts
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("💰 Revenue Trend")

    # Revenue trend chart
    revenue_trend = filtered_data.groupby(['Quarter', 'Company'])['Revenue'].sum().reset_index()

    fig_revenue = px.line(
        revenue_trend,
        x='Quarter',
        y='Revenue',
        color='Company',
        title='Quarterly Revenue by Company',
        markers=True
    )
    fig_revenue.update_layout(
        xaxis_title="Quarter",
        yaxis_title="Revenue (Million USD)",
        hovermode='x unified'
    )
    st.plotly_chart(fig_revenue, use_container_width=True)

with col_right:
    st.subheader("📊 Profit Analysis")

    # Profit by company
    profit_by_company = filtered_data.groupby('Company')['Profit'].sum().reset_index()

    fig_profit = px.bar(
        profit_by_company.sort_values('Profit', ascending=False),
        x='Company',
        y='Profit',
        title='Total Profit by Company',
        color='Profit',
        color_continuous_scale='Blues'
    )
    fig_profit.update_layout(
        xaxis_title="Company",
        yaxis_title="Profit (Million USD)"
    )
    st.plotly_chart(fig_profit, use_container_width=True)

st.markdown("---")

# Second row of charts
col_left2, col_right2 = st.columns(2)

with col_left2:
    st.subheader("🔄 Revenue vs Expenses")

    # Revenue vs Expenses scatter
    latest_quarter = filtered_data.groupby('Company').last().reset_index()

    fig_scatter = px.scatter(
        latest_quarter,
        x='Revenue',
        y='Expenses',
        size='Profit',
        color='Sector',
        hover_data=['Company'],
        title='Revenue vs Expenses (Latest Quarter)',
        size_max=60
    )
    fig_scatter.update_layout(
        xaxis_title="Revenue (Million USD)",
        yaxis_title="Expenses (Million USD)"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with col_right2:
    st.subheader("🏢 Sector Performance")

    # Sector comparison
    sector_data = filtered_data.groupby('Sector')[['Revenue', 'Profit']].sum().reset_index()

    fig_sector = go.Figure()
    fig_sector.add_trace(go.Bar(name='Revenue', x=sector_data['Sector'], y=sector_data['Revenue']))
    fig_sector.add_trace(go.Bar(name='Profit', x=sector_data['Sector'], y=sector_data['Profit']))

    fig_sector.update_layout(
        title='Revenue and Profit by Sector',
        xaxis_title="Sector",
        yaxis_title="Amount (Million USD)",
        barmode='group'
    )
    st.plotly_chart(fig_sector, use_container_width=True)

st.markdown("---")

# Stock Price Section
st.header("📈 Stock Price Trends")

# Filter stock data
if selected_company != "All":
    ticker = financial_data[financial_data['Company'] == selected_company]['Ticker'].iloc[0]
    stock_filtered = stock_data[stock_data['Ticker'] == ticker]
else:
    stock_filtered = stock_data

fig_stock = px.line(
    stock_filtered,
    x='Date',
    y='Price',
    color='Ticker',
    title='Stock Price History (Last 6 Months)',
    markers=False
)
fig_stock.update_layout(
    xaxis_title="Date",
    yaxis_title="Stock Price (USD)",
    hovermode='x unified'
)
st.plotly_chart(fig_stock, use_container_width=True)

st.markdown("---")

# Data Table Section
st.header("📋 Detailed Financial Data")

# Display options
show_rows = st.slider("Number of rows to display", min_value=5, max_value=50, value=10, step=5)

# Display the filtered data
display_columns = ['Company', 'Ticker', 'Sector', 'Quarter', 'Revenue', 'Expenses', 'Profit', 'Profit_Margin']
st.dataframe(
    filtered_data[display_columns].sort_values('Date', ascending=False).head(show_rows),
    use_container_width=True,
    hide_index=True
)

# Download button
csv = filtered_data.to_csv(index=False)
st.download_button(
    label="📥 Download Data as CSV",
    data=csv,
    file_name="financial_data.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>MGIS Business Intelligence Dashboard | Built with Streamlit</p>
        <p>Data is generated for demonstration purposes</p>
    </div>
    """,
    unsafe_allow_html=True
)
