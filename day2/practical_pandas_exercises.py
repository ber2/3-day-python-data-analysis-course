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
    # Day 2, Practical Session: Pandas in Action

    ## Three-Day Data Analysis with Python Course

    **Goal:** Apply pandas skills to analyze a real-world retail dataset!
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Practical Session Overview

    This session is **hands-on practice** with a real dataset. We'll work through:

    1. **Data Exploration** - Loading and inspecting the UCI Online Retail dataset
    2. **Data Cleaning** - Handling missing values, removing bad data
    3. **Transformation** - Creating new columns, applying functions
    4. **Aggregation** - GroupBy operations to answer business questions

    ---

    **Instructions:**
    - Try to solve each exercise yourself first
    - Work at your own pace
    - Ask questions anytime!
    - Solutions available in separate file
    """
    )
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np

    print(f"pandas version: {pd.__version__}")
    print(f"numpy version: {np.__version__}")
    return np, pd


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Loading the UCI Online Retail Dataset

    We'll use a real-world dataset from the UCI Machine Learning Repository.
    This dataset contains all transactions occurring for a UK-based online retail
    between 01/12/2010 and 09/12/2011.

    **Dataset:** Online Retail (UCI ML Repository)
    **License:** CC BY 4.0
    """
    )
    return


@app.cell
def _(pd):
    import urllib.request
    import zipfile
    from io import BytesIO

    # Download and extract the UCI Online Retail dataset
    print("Downloading dataset...")
    url = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"

    with urllib.request.urlopen(url) as response:
        zip_data = BytesIO(response.read())

    print("Extracting and loading Excel file...")
    with zipfile.ZipFile(zip_data) as z:
        # Extract the Excel file
        with z.open('Online Retail.xlsx') as f:
            retail_df = pd.read_excel(f)

    print(f"✓ Dataset loaded successfully!")
    print(f"  Shape: {retail_df.shape[0]:,} rows × {retail_df.shape[1]} columns")
    print(f"\nFirst few rows:")
    retail_df.head()
    return BytesIO, retail_df, urllib, z, zip_data, zipfile


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 1: Data Exploration

    Now that we have the real-world retail dataset loaded, let's explore it!

    **Dataset columns:**
    - `InvoiceNo`: Transaction ID (starts with 'C' if cancelled)
    - `StockCode`: Product code
    - `Description`: Product name
    - `Quantity`: Number of items (negative for returns)
    - `InvoiceDate`: Transaction timestamp
    - `UnitPrice`: Price per unit in GBP (£)
    - `CustomerID`: Customer identifier
    - `Country`: Customer's country
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1.1: Basic Dataset Inspection

    **Tasks:**
    1. Display the first 10 rows using `.head(10)`
    2. Show the dataset info using `.info()`
    3. Get statistical summary using `.describe()`
    4. Print the shape of the dataset
    5. List all column names using `.columns`

    **Work with the `retail_df` DataFrame.**
    """
    )
    return


@app.cell
def _(retail_df):
    # YOUR CODE HERE
    # Task 1: Display first 10 rows

    # Task 2: Show info

    # Task 3: Statistical summary

    # Task 4: Shape

    # Task 5: Column names

    pass


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1.2: Identify Data Quality Issues

    **Tasks:**
    1. Check for missing values in each column using `.isna().sum()`
    2. Calculate what percentage of CustomerID values are missing
    3. Find how many unique countries are in the dataset using `.nunique()`
    4. Find how many unique products (StockCode) exist
    5. Check if there are any negative quantities (returns/cancellations)

    **Hint:** For task 5, use boolean indexing: `retail_df[retail_df['Quantity'] < 0]`
    """
    )
    return


@app.cell
def _(retail_df):
    # YOUR CODE HERE
    # Task 1: Missing values per column

    # Task 2: Percentage of missing CustomerID

    # Task 3: Unique countries

    # Task 4: Unique products

    # Task 5: Count negative quantities

    pass


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1.3: Basic Filtering

    **Tasks:**
    1. Filter for transactions from "United Kingdom" only, store in `uk_only`
    2. Filter for bulk purchases (Quantity > 10), store in `bulk_purchases`
    3. Filter for cancelled orders (InvoiceNo starts with 'C'), store in `cancelled`
    4. Filter for premium items (UnitPrice > 100), store in `premium_items`

    **Hint:** Use `.str.startswith('C')` for checking if InvoiceNo starts with 'C'
    """
    )
    return


@app.cell
def _(retail_df):
    # YOUR CODE HERE
    # Task 1: UK transactions only

    # Task 2: Bulk purchases (Quantity > 10)

    # Task 3: Cancelled orders

    # Task 4: Premium items (UnitPrice > 100)

    pass


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 2: Data Cleaning

    Now let's clean the dataset for analysis.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2.1: Clean the Dataset

    **Tasks:**
    1. Create a copy of `retail_df` called `retail_clean`
    2. Remove rows where Description is missing (null product names are useless)
    3. Remove rows where Quantity <= 0 (returns and errors)
    4. Remove rows where UnitPrice <= 0 (pricing errors)
    5. Remove cancelled orders (InvoiceNo starts with 'C')
    6. Print how many rows were removed

    **Hint:** Chain conditions with `&` (and) operator:
    ```python
    df[(df['col1'] > 0) & (df['col2'] > 0)]
    ```
    """
    )
    return


@app.cell
def _(retail_df):
    # YOUR CODE HERE
    # Create retail_clean and apply all filters

    # Print original vs cleaned size

    pass


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2.2: Handle Missing Customer IDs

    **Tasks:**
    For your `retail_clean` DataFrame:

    1. How many transactions have missing CustomerID?
    2. What percentage is this of total transactions?
    3. Create two datasets:
       - `retail_with_customers`: Only rows with CustomerID
       - `retail_no_customers`: Only rows without CustomerID

    **Business context:** Transactions without CustomerID are valid (guest checkouts)
    but we'll need separate them for customer analysis.
    """
    )
    return


@app.cell
def _(retail_clean):
    # YOUR CODE HERE
    # 1. Count missing CustomerID

    # 2. Calculate percentage

    # 3. Create both datasets

    pass


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 3: Transformation

    Let's create calculated columns for business insights.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.1: Add Calculated Columns

    **Tasks:**
    Working with `retail_with_customers`, create these new columns:

    1. `TotalPrice`: Quantity × UnitPrice (revenue per line item)
    2. `ItemCategory`: Categorize items by quantity
       - "Single" if Quantity == 1
       - "Small" if 2 <= Quantity <= 5
       - "Medium" if 6 <= Quantity <= 20
       - "Bulk" if Quantity > 20

    **Hint:** For the category, you can use nested if-elif or create a function to apply
    """
    )
    return


@app.cell
def _(retail_with_customers):
    # YOUR CODE HERE
    # 1. Add TotalPrice column

    # 2. Add ItemCategory column

    # Display first few rows to verify

    pass


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.2: Categorize Products

    **Tasks:**
    Create a function to categorize items by price tier, then apply it:

    1. Write function `price_tier(price)` that returns:
       - "Budget" if price < 3
       - "Standard" if 3 <= price < 10
       - "Premium" if price >= 10

    2. Apply it to create `PriceTier` column using `.apply()`

    3. Count how many products are in each tier using `.value_counts()`
    """
    )
    return


@app.cell
def _(retail_with_customers):
    # YOUR CODE HERE
    # 1. Define price_tier function
    def price_tier(price):
        # Your logic here
        pass

    # 2. Apply to create PriceTier column

    # 3. Count items per tier

    pass


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 4: Aggregation & Analysis

    Answer business questions using GroupBy!
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 4.1: Country Analysis

    **Business Question:** Which countries generate the most revenue?

    **Tasks:**
    1. Group by Country and sum TotalPrice
    2. Sort by total revenue (descending)
    3. Show top 10 countries
    4. What percentage of total revenue comes from UK?

    **Hint:** Use `.groupby()`, `.sum()`, `.sort_values()`, and `.head()`
    """
    )
    return


@app.cell
def _(retail_with_customers):
    # YOUR CODE HERE
    # 1. Revenue by country

    # 2. Sort descending

    # 3. Top 10

    # 4. UK percentage

    pass


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 4.2: Product Performance

    **Business Question:** What are our best-selling products?

    **Tasks:**
    1. Group by Description
    2. Calculate total quantity sold and total revenue for each product
    3. Sort by total quantity (descending)
    4. Show top 20 best-selling products

    **Hint:** Use `.groupby().agg()` with multiple aggregations:
    ```python
    df.groupby('col').agg({'col1': 'sum', 'col2': 'sum'})
    ```
    """
    )
    return


@app.cell
def _(retail_with_customers):
    # YOUR CODE HERE
    # Group by Description, aggregate Quantity and TotalPrice

    # Sort and show top 20

    pass


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 4.3: Country & Item Category Analysis

    **Business Question:** How do sales patterns differ across countries and item categories?

    **Tasks:**
    1. Group by Country and ItemCategory
    2. Calculate total revenue (TotalPrice sum) for each combination
    3. Sort by total revenue (descending)
    4. Show top 20 combinations

    **Hint:** Group by multiple columns: `.groupby(['Country', 'ItemCategory'])`
    """
    )
    return


@app.cell
def _(retail_enhanced):
    # YOUR CODE HERE
    # 1. Group by Country and ItemCategory

    # 2. Sum revenue

    # 3. Sort and show top 20

    pass


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 4.4: Customer Segmentation

    **Business Question:** Who are our most valuable customers?

    **Tasks:**
    1. Group by CustomerID
    2. Calculate for each customer:
       - Total revenue (`TotalPrice` sum)
       - Number of orders (`InvoiceNo` nunique - counts unique invoices)
       - Average order value (revenue / number of orders)
    3. Sort by total revenue
    4. Show top 20 customers

    **Hint:** Use `.agg()` with different functions:
    ```python
    .agg({
        'TotalPrice': 'sum',
        'InvoiceNo': 'nunique'
    })
    ```
    """
    )
    return


@app.cell
def _(retail_with_customers):
    # YOUR CODE HERE
    # Create customer summary

    # Calculate average order value

    # Show top 20

    pass


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 5: Executive Summary

    **Final Challenge:** Create a comprehensive country-level summary report.

    **Requirements:**
    Create a DataFrame with these metrics per country:
    - Total Revenue
    - Total Transactions (unique InvoiceNo count)
    - Total Customers (unique CustomerID count)
    - Average Order Value (Revenue / Transactions)
    - Average Items Per Order (Quantity sum / Transactions)

    Sort by Total Revenue and show top 15 countries.

    **Hint:** Use `.groupby().agg()` with multiple columns and functions,
    then calculate derived metrics.
    """
    )
    return


@app.cell
def _(retail_with_customers):
    # YOUR CODE HERE
    # Create executive summary

    pass


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    ## Congratulations! 🎉

    You've completed the Day 2 practical session using real-world data!

    **Skills you practiced:**
    - ✓ Loading data from external sources
    - ✓ Exploring datasets with pandas methods
    - ✓ Handling missing values and data quality issues
    - ✓ Creating calculated columns
    - ✓ Applying functions to transform data
    - ✓ GroupBy aggregations to answer business questions
    - ✓ Multi-level aggregations and summaries

    **You're now ready for Day 3: Data Visualization & Advanced Analysis!**
    """
    )
    return


if __name__ == "__main__":
    app.run()
