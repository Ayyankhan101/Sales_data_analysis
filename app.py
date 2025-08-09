
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(layout="wide", page_title="Sales Data Analysis", page_icon=":bar_chart:")

# Load the dataset
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('9. Sales-Data-Analysis.csv.gz', compression='gzip')
    except FileNotFoundError:
        df = pd.read_csv('9. Sales-Data-Analysis.csv')
        
    df.columns = df.columns.str.strip().str.replace(' ', '_')
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    for col in ['Product', 'Purchase_Type', 'Payment_Method', 'Manager', 'City']:
        if col in df.columns:
            df[col] = df[col].str.strip()
    df['Total_Sales'] = df['Price'] * df['Quantity']
    df.dropna(inplace=True)
    df.drop_duplicates(subset=['Order_ID'], inplace=True)
    return df

df = load_data()

# Sidebar
st.sidebar.title("Sales Dashboard")
st.sidebar.header("Filters")

# Date range filter
min_date = df['Date'].min().date()
max_date = df['Date'].max().date()
start_date, end_date = st.sidebar.date_input("Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

# City filter
selected_cities = st.sidebar.multiselect("City", df['City'].unique(), default=df['City'].unique())

# Manager filter
selected_managers = st.sidebar.multiselect("Manager", df['Manager'].unique(), default=df['Manager'].unique())

# Product filter
selected_products = st.sidebar.multiselect("Product", df['Product'].unique(), default=df['Product'].unique())

# Filter data
filtered_df = df[
    (df['Date'].dt.date >= start_date) &
    (df['Date'].dt.date <= end_date) &
    (df['City'].isin(selected_cities)) &
    (df['Manager'].isin(selected_managers)) &
    (df['Product'].isin(selected_products))
]

# Main content
st.title("Sales Data Analysis Dashboard")

# Key Metrics
total_sales = filtered_df['Total_Sales'].sum()
total_orders = filtered_df['Order_ID'].nunique()
average_order_value = total_sales / total_orders if total_orders > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Average Order Value", f"${average_order_value:,.2f}")

st.markdown("---")

# Sales Trends
st.header("Sales Trends")
daily_sales = filtered_df.groupby('Date')['Total_Sales'].sum().reset_index()
fig_daily_sales = px.line(daily_sales, x='Date', y='Total_Sales', title='Daily Sales Trend', markers=True,color_discrete_sequence=["#38bd55"])
st.plotly_chart(fig_daily_sales, use_container_width=True)

# Monthly and Day of Week Sales
col1, col2 = st.columns(2)

with col1:
    filtered_df['Month'] = filtered_df['Date'].dt.month_name()
    monthly_sales = filtered_df.groupby('Month')['Total_Sales'].sum().reindex(
        ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ).reset_index()
    fig_monthly_sales = px.bar(monthly_sales, x='Month', y='Total_Sales', title='Total Sales by Month', color='Total_Sales', color_continuous_scale=px.colors.sequential.Viridis,color_discrete_sequence=["#3b85e6"])
    st.plotly_chart(fig_monthly_sales, use_container_width=True)

with col2:
    filtered_df['Day_of_Week'] = filtered_df['Date'].dt.day_name()
    daily_of_week_sales = filtered_df.groupby('Day_of_Week')['Total_Sales'].sum().reindex(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ).reset_index()
    fig_daily_of_week_sales = px.bar(daily_of_week_sales, x='Day_of_Week', y='Total_Sales', title='Total Sales by Day of Week' , color='Total_Sales', color_continuous_scale=px.colors.sequential.Viridis, color_discrete_sequence=["#902fb6"])
    st.plotly_chart(fig_daily_of_week_sales, use_container_width=True)

st.markdown("---")

# Product Performance
st.header("Product Performance")
col1, col2 = st.columns(2)

with col1:
    top_products_sales = filtered_df.groupby('Product')['Total_Sales'].sum().nlargest(10).reset_index()
    fig_top_products_sales = px.bar(top_products_sales, x='Total_Sales', y='Product', orientation='h', title='Top 10 Products by Total Sales' ,color='Total_Sales', color_continuous_scale=px.colors.sequential.Plasma,color_discrete_sequence=["#2ecbd6"])
    st.plotly_chart(fig_top_products_sales, use_container_width=True)

with col2:
    top_products_quantity = filtered_df.groupby('Product')['Quantity'].sum().nlargest(10).reset_index()
    fig_top_products_quantity = px.bar(top_products_quantity, x='Quantity', y='Product', orientation='h', title='Top 10 Products by Quantity Sold', color='Quantity', color_continuous_scale=px.colors.sequential.Plasma , color_discrete_sequence=["#dfdfdf"])
    st.plotly_chart(fig_top_products_quantity, use_container_width=True)

st.markdown("---")

# Geographical and Managerial Insights
st.header("Geographical & Managerial Insights")
col1, col2 = st.columns(2)

with col1:
    sales_by_city = filtered_df.groupby('City')['Total_Sales'].sum().sort_values(ascending=False).reset_index()
    fig_sales_by_city = px.bar(sales_by_city, x='Total_Sales', y='City', orientation='h', title='Total Sales by City' , color='Total_Sales', color_continuous_scale=px.colors.sequential.Viridis, color_discrete_sequence=["#f0a500"])
    st.plotly_chart(fig_sales_by_city, use_container_width=True)

with col2:
    sales_by_manager = filtered_df.groupby('Manager')['Total_Sales'].sum().sort_values(ascending=False).reset_index()
    fig_sales_by_manager = px.bar(sales_by_manager, x='Total_Sales', y='Manager', orientation='h', title='Total Sales by Manager', color='Total_Sales', color_continuous_scale=px.colors.sequential.Viridis, color_discrete_sequence=["#f0a500"])
    st.plotly_chart(fig_sales_by_manager, use_container_width=True)

st.markdown("---")

# Purchase Behavior Analysis
st.header("Purchase Behavior Analysis")
col1, col2 = st.columns(2)

with col1:
    sales_by_purchase_type = filtered_df.groupby('Purchase_Type')['Total_Sales'].sum().sort_values(ascending=False).reset_index()
    fig_purchase_type = px.pie(sales_by_purchase_type, values='Total_Sales', names='Purchase_Type', title='Total Sales by Purchase Type')
    st.plotly_chart(fig_purchase_type, use_container_width=True)

with col2:
    sales_by_payment_method = filtered_df.groupby('Payment_Method')['Total_Sales'].sum().sort_values(ascending=False).reset_index()
    fig_payment_method = px.pie(sales_by_payment_method, values='Total_Sales', names='Payment_Method', title='Total Sales by Payment Method')
    st.plotly_chart(fig_payment_method, use_container_width=True)

# Data Table
st.markdown("---")
st.header("Raw Data")
st.dataframe(filtered_df)
