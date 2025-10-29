import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 3, Capstone Project: E-commerce Analytics

    ## Three-Day Data Analysis with Python Course

    **Business Context:** You're a data analyst for an online retail company.
    The CEO wants insights before the holiday season to make strategic decisions.

    **Goal:** Complete end-to-end analysis using all skills from the course!
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Project Overview

    This capstone project integrates everything you've learned:

    1. **Part 1: Advanced Data Preparation** (30 min)
       - Load UCI Online Retail dataset
       - Extract datetime features
       - Create RFM metrics

    2. **Part 2: Multi-Dataset Analysis** (30 min)
       - Create aggregated tables
       - Merge datasets
       - Pivot tables for insights

    3. **Part 3: Interactive Visualizations** (40 min)
       - Answer 5 business questions with charts
       - Use Plotly Express and Seaborn

    4. **Part 4: Funnel Analysis** (20 min)
       - Build customer lifecycle funnel
       - Calculate conversion rates
       - Visualize the funnel

    5. **Part 5: Executive Summary** (Optional)
       - Create interactive dashboard with marimo UI
       - Write key findings

    **Solutions available in separate file!**
    """
    )
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import seaborn as sns
    import matplotlib.pyplot as plt

    print(f"pandas version: {pd.__version__}")
    return (pd,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 1: Advanced Data Preparation

    Load the UCI Online Retail dataset and enhance it with datetime features.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 1.1: Load the Dataset

    Download and load the UCI Online Retail dataset.
    **This is the same dataset from Day 2!**
    """
    )
    return


@app.cell
def _(pd):
    import urllib.request
    import zipfile
    from io import BytesIO

    # Download and load UCI Online Retail dataset
    print("Downloading dataset...")
    url = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"

    with urllib.request.urlopen(url) as response:
        zip_data = BytesIO(response.read())

    print("Loading...")
    with zipfile.ZipFile(zip_data) as z:
        with z.open("Online Retail.xlsx") as f:
            retail_df = pd.read_excel(f)

    print(
        f"✓ Dataset loaded: {retail_df.shape[0]:,} rows × {retail_df.shape[1]} columns"
    )
    retail_df.head()
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 1.2: Clean the Dataset

    **Tasks:**
    1. Remove rows where Description is missing
    2. Remove rows where Quantity <= 0
    3. Remove rows where UnitPrice <= 0
    4. Remove cancelled orders (InvoiceNo starts with 'C')
    5. Remove rows where CustomerID is missing
    6. Print how many rows were removed

    **Store the result in `retail_clean`**
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Create retail_clean

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 1.3: Extract Datetime Features

    **Tasks:**
    Using the `.dt` accessor on InvoiceDate column:

    1. Extract `Year`
    2. Extract `Month`
    3. Extract `Quarter`
    4. Extract `DayOfWeek` (as name, like "Monday")
    5. Extract `Hour`

    **Add these as new columns to `retail_clean`**
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Extract datetime features

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 1.4: Create Calculated Columns

    **Tasks:**
    1. Create `TotalPrice` = Quantity × UnitPrice
    2. Create `InvoiceYearMonth` = combine Year and Month (format: "2024-01")

    **Hint for InvoiceYearMonth:**
    ```python
    df['InvoiceYearMonth'] = df['InvoiceDate'].dt.to_period('M').astype(str)
    ```
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Create TotalPrice and InvoiceYearMonth columns

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 1.5: Calculate RFM Metrics

    **RFM = Recency, Frequency, Monetary**

    For each customer, calculate:
    - **Recency**: Days since last purchase
    - **Frequency**: Number of unique invoices (orders)
    - **Monetary**: Total amount spent

    **Tasks:**
    1. Find the reference date (use the maximum InvoiceDate in the dataset)
    2. Group by CustomerID
    3. Calculate:
       - Recency: (reference_date - max(InvoiceDate)).days
       - Frequency: count of unique InvoiceNo
       - Monetary: sum of TotalPrice
    4. Store result in `rfm_data`

    **Hint:**
    ```python
    reference_date = df['InvoiceDate'].max()
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (reference_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    })
    ```
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Calculate RFM metrics

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 2: Multi-Dataset Analysis

    Create separate aggregated tables and merge them back together.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 2.1: Create Customer Summary Table

    **Tasks:**
    Aggregate by CustomerID to create a customer summary with:
    - Total number of orders (unique InvoiceNo count)
    - Total items purchased (sum of Quantity)
    - Total revenue (sum of TotalPrice)
    - First purchase date (min of InvoiceDate)
    - Last purchase date (max of InvoiceDate)
    - Most common country (mode of Country)

    Store in `customer_summary`
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Create customer_summary

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 2.2: Create Product Summary Table

    **Tasks:**
    Aggregate by StockCode and Description to create:
    - Total quantity sold
    - Total revenue
    - Number of unique customers who bought it
    - Average unit price

    Store in `product_summary`
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Create product_summary

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 2.3: Merge Customer Summary with RFM

    **Tasks:**
    Merge `customer_summary` with `rfm_data` on CustomerID.

    Store in `customer_enriched`
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Merge customer_summary with rfm_data

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 2.4: Create Pivot Table

    **Tasks:**
    Create a pivot table showing:
    - Rows: Country
    - Columns: Quarter
    - Values: Sum of TotalPrice

    This shows revenue by country and quarter.

    Store in `country_quarter_pivot`
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Create pivot table

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 3: Interactive Visualizations

    Answer 5 business questions with visualizations.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Visualization 1: Revenue Trends Over Time

    **Business Question:** How has monthly revenue changed over time?

    **Tasks:**
    1. Group retail_clean by InvoiceYearMonth
    2. Sum TotalPrice for each month
    3. Create a line chart with Plotly Express
    4. Add markers to the line
    5. Add appropriate title and labels
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Create monthly revenue line chart

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Visualization 2: Top 15 Countries by Revenue

    **Business Question:** Which countries generate the most revenue?

    **Tasks:**
    1. Group by Country, sum TotalPrice
    2. Sort descending
    3. Take top 15
    4. Create horizontal bar chart with Plotly Express
    5. Color bars by revenue amount
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Create top countries bar chart

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Visualization 3: Customer Segmentation (RFM)

    **Business Question:** Can we identify customer segments based on behavior?

    **Tasks:**
    1. Use customer_enriched DataFrame
    2. Create scatter plot: Recency (x) vs Monetary (y)
    3. Size points by Frequency
    4. Color by Frequency
    5. Add hover data with CustomerID
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Create RFM scatter plot

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Visualization 4: Sales by Hour of Day

    **Business Question:** When do customers shop most?

    **Tasks:**
    1. Group retail_clean by Hour
    2. Count number of transactions (or sum TotalPrice)
    3. Create bar chart showing activity by hour
    4. Use Seaborn or Plotly Express
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Create hourly sales chart

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Visualization 5: Product Performance

    **Business Question:** What are our top-selling products?

    **Tasks:**
    1. Use product_summary
    2. Sort by total revenue
    3. Take top 20
    4. Create horizontal bar chart
    5. Show product Description and revenue
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Create top products chart

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 4: Funnel Analysis

    Build a customer lifecycle funnel.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 4.1: Define Funnel Stages

    **Customer Lifecycle Funnel:**
    1. **All Customers**: Everyone who made at least 1 purchase
    2. **Repeat Customers**: Made 2+ purchases
    3. **Frequent Customers**: Made 5+ purchases
    4. **VIP Customers**: Made 10+ purchases

    **Tasks:**
    Using customer_summary (which has order counts):
    1. Count customers at each stage
    2. Create a dictionary `funnel_counts` with stage names and counts
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Define funnel stages and count customers

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 4.2: Calculate Conversion Rates

    **Tasks:**
    1. Create a DataFrame from funnel_counts
    2. Calculate conversion rate from each stage to the next
    3. Calculate overall conversion (All → VIP)
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Calculate conversion rates

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 4.3: Visualize the Funnel

    **Tasks:**
    Create a funnel chart using Plotly's go.Funnel

    **Example:**
    ```python
    fig = go.Figure(go.Funnel(
        y=stages_list,
        x=counts_list,
        textinfo='value+percent previous'
    ))
    ```
    """
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    # Create funnel visualization

    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 5: Executive Summary (Optional)

    **Challenge:** Create an interactive dashboard with marimo UI elements.

    Ideas:
    - Dropdown to filter by country
    - Slider to filter by date range
    - Reactive charts that update based on filters
    - KPI cards showing key metrics

    **This is advanced - try if you finish early!**
    """
    )
    return


@app.cell
def _(mo, retail_clean):
    # OPTIONAL: Create interactive filters
    # Example:
    country_filter = mo.ui.dropdown(
        options=["All"] + sorted(retail_clean["Country"].unique().tolist()),
        value="All",
        label="Select Country:",
    )
    country_filter
    return (country_filter,)


@app.cell
def _(country_filter, retail_clean):
    # OPTIONAL: Filter data based on selection
    if country_filter.value == "All":
        filtered_df = retail_clean
    else:
        filtered_df = retail_clean[retail_clean["Country"] == country_filter.value]

    print(f"Showing data for: {country_filter.value}")
    print(f"Transactions: {len(filtered_df):,}")
    return


@app.cell
def _():
    # OPTIONAL: Create reactive visualizations
    # Charts here will update when country_filter changes!
    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    ## Congratulations! 🎉

    You've completed the capstone project!

    **What you accomplished:**
    - ✓ Advanced data cleaning and preparation
    - ✓ Datetime feature extraction
    - ✓ RFM analysis for customer segmentation
    - ✓ Multi-dataset merging and pivoting
    - ✓ Business-focused visualizations
    - ✓ Funnel analysis with conversion metrics

    **You now have the skills to:**
    - Load and clean real-world datasets
    - Transform data for analysis
    - Create insightful visualizations
    - Answer business questions with data
    - Build end-to-end analytics projects

    **Next steps:**
    - Review the solutions notebook
    - Practice with your own datasets
    - Explore advanced pandas and visualization libraries
    - Build a portfolio project to showcase your skills!

    **Great job! You're now a data analyst!** 📊
    """
    )
    return


if __name__ == "__main__":
    app.run()
