# Sales Data Analysis Project

## Project Overview
This project provides a comprehensive analysis of sales data, aiming to extract meaningful insights, identify trends, and offer actionable recommendations for business improvement. The analysis covers various aspects, including product performance, sales trends over time, geographical distribution of sales, and managerial effectiveness.

## Goals of the Analysis
-   **Understand Sales Trends:** Analyze daily, monthly, and weekly sales patterns to identify seasonality and growth.
-   **Product Performance:** Identify top-selling products and categories, as well as underperforming items.
-   **Geographical Insights:** Understand sales distribution across different cities to inform regional strategies.
-   **Managerial Effectiveness:** Evaluate sales performance attributed to individual managers.
-   **Purchase Behavior:** Analyze preferred purchase types (e.g., In-store, Online, Drive-thru) and payment methods.

## Dataset Information
The dataset `9. Sales-Data-Analysis.csv` contains the following columns:
-   `Order ID`: Unique identifier for each order.
-   `Date`: Date of the purchase.
-   `Product`: Name of the product sold.
-   `Price`: Price of the product.
-   `Quantity`: Quantity of the product sold.
-   `Purchase Type`: How the purchase was made (e.g., Online, In-store, Drive-thru).
-   `Payment Method`: Method used for payment (e.g., Credit Card, Gift Card, Cash).
-   `Manager`: Name of the manager responsible for the sale.
-   `City`: City where the sale occurred.

## Interactive Dashboard
This project includes an interactive dashboard built with Streamlit. The dashboard allows users to filter the data and visualize the insights in real-time.

## How to Run the Dashboard

To run the interactive dashboard, please follow these steps:

### Prerequisites
-   Python 3.x installed.
-   The required Python libraries are listed in the `requirements.txt` file.

### Steps
1.  **Clone the repository or download the files.**
2.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
4.  **View the dashboard:** Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

## Tools and Technologies Used
-   Python 3.x
-   Streamlit (for the interactive dashboard)
-   Pandas (for data manipulation and analysis)
-   Plotly Express (for interactive visualizations)

# Sales_data_analysis