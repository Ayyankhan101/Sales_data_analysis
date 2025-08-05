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

## Key Findings and Insights
(These insights are based on the analysis performed using the provided Python script. Please refer to the visualizations generated after running the script for detailed insights.)

1.  **Sales Trends:** The analysis reveals fluctuations in daily sales, suggesting potential weekly or monthly patterns. Further investigation into longer periods would confirm specific peak times.
2.  **Product Performance:** "Burgers" consistently lead in total sales, followed by "Chicken Sandwiches" and "Fries," indicating they are core revenue drivers. "Sides & Other" and "Beverages" contribute less but are important for upselling.
3.  **Geographical Performance:** Cities like Madrid and London appear to be high-performing in terms of total sales, possibly due to higher population density or effective local strategies.
4.  **Managerial Contribution:** Managers such as Pablo Perez and Tom Jackson demonstrate strong sales performance, suggesting their strategies could be valuable for others.
5.  **Purchase and Payment Preferences:** "In-store" purchases are dominant, followed by "Drive-thru" and "Online," emphasizing the importance of physical presence. "Credit Card" is the most preferred payment method.

## Actionable Recommendations
1.  **Optimize Inventory and Marketing:** Focus on ensuring consistent availability and consider promotional bundles for top-selling products like Burgers, Chicken Sandwiches, and Fries.
2.  **Targeted Marketing:** Develop strategies to boost sales of "Sides & Other" and "Beverages," perhaps through combo deals or prominent placement.
3.  **Leverage High-Performing Locations:** Invest further in marketing and services in successful cities like Madrid and London, and analyze their success factors.
4.  **Knowledge Sharing:** Facilitate sessions for top-performing managers to share their successful sales techniques.
5.  **Enhance In-store and Drive-thru Experience:** Prioritize efficiency and customer service in these primary revenue channels.
6.  **Payment System Review:** Ensure robust credit card processing and consider promotions for gift card usage.

## How to Run the Analysis

To replicate this analysis, please follow these steps:

### Prerequisites
-   Python 3.x installed.
-   Jupyter Notebook installed (`pip install notebook`).
-   Required Python libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`.
    You can install them using pip:
    ```bash
    pip install pandas numpy matplotlib seaborn plotly
    ```
-   For PDF export, `nbconvert` and `pandoc` are required.
    ```bash
    pip install nbconvert
    sudo apt-get install pandoc  # For Debian/Ubuntu. Adjust for other OS.
    ```

### Steps
1.  **Download the Dataset:** Ensure `9. Sales-Data-Analysis.csv` is in the same directory as your Jupyter Notebook.
2.  **Create a New Jupyter Notebook:** Open Jupyter Notebook and create a new Python 3 notebook.
3.  **Copy and Paste Code:** Open the `sales_analysis_script.py` file (provided in the same directory) and copy its entire content. Paste this code into the first cell of your new Jupyter Notebook.
4.  **Add Markdown Cells:** To include the detailed markdown explanations and structure, you will need to manually add markdown cells in your Jupyter Notebook. You can refer to the original `sales_data_analysis.ipynb` (if you still have it) or the markdown sections I previously provided to recreate the narrative.
5.  **Run All Cells:** Execute all cells in the notebook to perform the analysis and generate visualizations.
    (Go to `Cell` -> `Run All` in the Jupyter Notebook menu).
6.  **Export to PDF:** Once all cells are executed, you can export the notebook to PDF from the Jupyter Notebook interface:
    `File` -> `Download as` -> `PDF via LaTeX (.pdf)`.

## Tools and Technologies Used
-   Python 3.x
-   Jupyter Notebook
-   Pandas (for data manipulation and analysis)
-   NumPy (for numerical operations)
-   Matplotlib (for static visualizations)
-   Seaborn (for enhanced statistical visualizations)
-   Plotly Express (for interactive visualizations)
-   nbconvert (for converting notebook to PDF)
-   Pandoc (dependency for nbconvert PDF export)


# Sales_data_analysis
