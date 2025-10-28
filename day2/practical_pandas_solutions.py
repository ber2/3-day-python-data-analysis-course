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
    # Day 2, Practical Session: Pandas in Action (SOLUTIONS)

    ## Three-Day Data Analysis with Python Course

    **This notebook contains complete solutions to all exercises.**
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
    mo.md(r"""# Part 1: Data Exploration (SOLUTIONS)""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 1.1: Basic Dataset Inspection (SOLUTION)""")
    return


@app.cell
def _(retail_df):
    # Task 1: Display first 10 rows
    print("First 10 rows:")
    print(retail_df.head(10))
    print()

    # Task 2: Show info
    print("Dataset info:")
    retail_df.info()
    print()

    # Task 3: Statistical summary
    print("Statistical summary:")
    print(retail_df.describe())
    print()

    # Task 4: Shape
    print(f"Shape: {retail_df.shape}")
    print()

    # Task 5: Column names
    print("Column names:")
    print(retail_df.columns.tolist())
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 1.2: Identify Data Quality Issues (SOLUTION)""")
    return


@app.cell
def _(retail_df):
    # Task 1: Missing values per column
    print("Missing values per column:")
    print(retail_df.isna().sum())
    print()

    # Task 2: Percentage of missing CustomerID
    missing_customer_pct = (retail_df['CustomerID'].isna().sum() / len(retail_df)) * 100
    print(f"Percentage of missing CustomerID: {missing_customer_pct:.2f}%")
    print()

    # Task 3: Unique countries
    unique_countries = retail_df['Country'].nunique()
    print(f"Unique countries: {unique_countries}")
    print()

    # Task 4: Unique products
    unique_products = retail_df['StockCode'].nunique()
    print(f"Unique products: {unique_products}")
    print()

    # Task 5: Count negative quantities
    negative_qty = (retail_df['Quantity'] < 0).sum()
    print(f"Transactions with negative quantities: {negative_qty}")
    return missing_customer_pct, negative_qty, unique_countries, unique_products


@app.cell
def _(mo):
    mo.md(r"""## Exercise 1.3: Basic Filtering (SOLUTION)""")
    return


@app.cell
def _(retail_df):
    # Task 1: UK transactions only
    uk_only = retail_df[retail_df['Country'] == 'United Kingdom']
    print(f"UK transactions: {len(uk_only):,}")
    print()

    # Task 2: Bulk purchases (Quantity > 10)
    bulk_purchases = retail_df[retail_df['Quantity'] > 10]
    print(f"Bulk purchases (Quantity > 10): {len(bulk_purchases):,}")
    print()

    # Task 3: Cancelled orders
    cancelled = retail_df[retail_df['InvoiceNo'].astype(str).str.startswith('C')]
    print(f"Cancelled orders: {len(cancelled):,}")
    print()

    # Task 4: Premium items (UnitPrice > 100)
    premium_items = retail_df[retail_df['UnitPrice'] > 100]
    print(f"Premium items (UnitPrice > £100): {len(premium_items):,}")
    return bulk_purchases, cancelled, premium_items, uk_only


@app.cell
def _(mo):
    mo.md(r"""# Part 2: Data Cleaning (SOLUTIONS)""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 2.1: Clean the Dataset (SOLUTION)""")
    return


@app.cell
def _(retail_df):
    # Create retail_clean with all filters
    retail_clean = retail_df.copy()

    original_size = len(retail_clean)

    # Remove missing descriptions
    retail_clean = retail_clean[retail_clean['Description'].notna()]

    # Remove zero or negative quantities
    retail_clean = retail_clean[retail_clean['Quantity'] > 0]

    # Remove zero or negative prices
    retail_clean = retail_clean[retail_clean['UnitPrice'] > 0]

    # Remove cancelled orders
    retail_clean = retail_clean[~retail_clean['InvoiceNo'].astype(str).str.startswith('C')]

    cleaned_size = len(retail_clean)
    removed = original_size - cleaned_size

    print(f"Original dataset: {original_size:,} rows")
    print(f"Cleaned dataset: {cleaned_size:,} rows")
    print(f"Removed: {removed:,} rows ({removed/original_size*100:.1f}%)")
    return cleaned_size, original_size, removed, retail_clean


@app.cell
def _(mo):
    mo.md(r"""## Exercise 2.2: Handle Missing Customer IDs (SOLUTION)""")
    return


@app.cell
def _(retail_clean):
    # 1. Count missing CustomerID
    missing_cust_count = retail_clean['CustomerID'].isna().sum()
    print(f"Transactions with missing CustomerID: {missing_cust_count:,}")
    print()

    # 2. Calculate percentage
    missing_cust_pct = (missing_cust_count / len(retail_clean)) * 100
    print(f"Percentage: {missing_cust_pct:.2f}%")
    print()

    # 3. Create both datasets
    retail_with_customers = retail_clean[retail_clean['CustomerID'].notna()].copy()
    retail_no_customers = retail_clean[retail_clean['CustomerID'].isna()].copy()

    print(f"Transactions with CustomerID: {len(retail_with_customers):,}")
    print(f"Transactions without CustomerID: {len(retail_no_customers):,}")
    return (
        missing_cust_count,
        missing_cust_pct,
        retail_no_customers,
        retail_with_customers,
    )


@app.cell
def _(mo):
    mo.md(r"""# Part 3: Transformation (SOLUTIONS)""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 3.1: Add Calculated Columns (SOLUTION)""")
    return


@app.cell
def _(retail_with_customers):
    # Add all calculated columns
    retail_enhanced = retail_with_customers.copy()

    # 1. TotalPrice
    retail_enhanced['TotalPrice'] = retail_enhanced['Quantity'] * retail_enhanced['UnitPrice']

    # 2. ItemCategory - categorize by quantity
    def categorize_quantity(qty):
        if qty == 1:
            return "Single"
        elif qty <= 5:
            return "Small"
        elif qty <= 20:
            return "Medium"
        else:
            return "Bulk"

    retail_enhanced['ItemCategory'] = retail_enhanced['Quantity'].apply(categorize_quantity)

    # Display first few rows
    print("Enhanced dataset with calculated columns:")
    print(retail_enhanced[['InvoiceNo', 'Quantity', 'UnitPrice', 'TotalPrice', 'ItemCategory']].head(10))
    print()
    print("Distribution of ItemCategory:")
    print(retail_enhanced['ItemCategory'].value_counts())
    return categorize_quantity, retail_enhanced


@app.cell
def _(mo):
    mo.md(r"""## Exercise 3.2: Categorize Products (SOLUTION)""")
    return


@app.cell
def _(retail_enhanced):
    # 1. Define price_tier function
    def price_tier_solution(price):
        if price < 3:
            return "Budget"
        elif price < 10:
            return "Standard"
        else:
            return "Premium"

    # 2. Apply to create PriceTier column
    retail_enhanced['PriceTier'] = retail_enhanced['UnitPrice'].apply(price_tier_solution)

    # 3. Count items per tier
    tier_counts_solution = retail_enhanced['PriceTier'].value_counts()
    print("Items per price tier:")
    print(tier_counts_solution)
    print()
    print("Percentage breakdown:")
    print((tier_counts_solution / len(retail_enhanced) * 100).round(2))
    return price_tier_solution, tier_counts_solution


@app.cell
def _(mo):
    mo.md(r"""# Part 4: Aggregation & Analysis (SOLUTIONS)""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 4.1: Country Analysis (SOLUTION)""")
    return


@app.cell
def _(retail_enhanced):
    # 1-3. Revenue by country, sorted, top 10
    revenue_by_country = retail_enhanced.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)

    print("Top 10 countries by revenue:")
    print(revenue_by_country.head(10))
    print()

    # 4. UK percentage
    uk_revenue = revenue_by_country['United Kingdom']
    total_revenue = revenue_by_country.sum()
    uk_pct = (uk_revenue / total_revenue) * 100

    print(f"UK revenue: £{uk_revenue:,.2f}")
    print(f"Total revenue: £{total_revenue:,.2f}")
    print(f"UK percentage: {uk_pct:.2f}%")
    return revenue_by_country, total_revenue, uk_pct, uk_revenue


@app.cell
def _(mo):
    mo.md(r"""## Exercise 4.2: Product Performance (SOLUTION)""")
    return


@app.cell
def _(retail_enhanced):
    # Group by Description, aggregate Quantity and TotalPrice
    product_performance = retail_enhanced.groupby('Description').agg({
        'Quantity': 'sum',
        'TotalPrice': 'sum'
    }).sort_values('Quantity', ascending=False)

    product_performance.columns = ['TotalQuantity', 'TotalRevenue']

    print("Top 20 best-selling products:")
    print(product_performance.head(20))
    return (product_performance,)


@app.cell
def _(mo):
    mo.md(r"""## Exercise 4.3: Country & Item Category Analysis (SOLUTION)""")
    return


@app.cell
def _(retail_enhanced):
    # Group by Country and ItemCategory
    country_category_revenue = retail_enhanced.groupby(['Country', 'ItemCategory'])['TotalPrice'].sum()

    # Sort by revenue descending
    country_category_revenue = country_category_revenue.sort_values(ascending=False)

    print("Top 20 Country-ItemCategory combinations by revenue:")
    print(country_category_revenue.head(20))
    print()

    # Additional insight: which category dominates in UK?
    uk_by_category = retail_enhanced[retail_enhanced['Country'] == 'United Kingdom'].groupby('ItemCategory')['TotalPrice'].sum().sort_values(ascending=False)
    print("UK revenue by ItemCategory:")
    print(uk_by_category)
    return country_category_revenue, uk_by_category


@app.cell
def _(mo):
    mo.md(r"""## Exercise 4.4: Customer Segmentation (SOLUTION)""")
    return


@app.cell
def _(retail_enhanced):
    # Group by CustomerID
    customer_summary = retail_enhanced.groupby('CustomerID').agg({
        'TotalPrice': 'sum',
        'InvoiceNo': 'nunique'
    })

    customer_summary.columns = ['TotalRevenue', 'NumOrders']

    # Calculate average order value
    customer_summary['AvgOrderValue'] = customer_summary['TotalRevenue'] / customer_summary['NumOrders']

    # Sort by total revenue
    customer_summary = customer_summary.sort_values('TotalRevenue', ascending=False)

    print("Top 20 customers by revenue:")
    print(customer_summary.head(20))
    return (customer_summary,)


@app.cell
def _(mo):
    mo.md(r"""# Part 5: Executive Summary (SOLUTION)""")
    return


@app.cell
def _(retail_enhanced):
    # Create comprehensive country summary
    executive_summary = retail_enhanced.groupby('Country').agg({
        'TotalPrice': 'sum',
        'InvoiceNo': 'nunique',
        'CustomerID': 'nunique',
        'Quantity': 'sum'
    })

    executive_summary.columns = ['TotalRevenue', 'TotalTransactions', 'TotalCustomers', 'TotalItems']

    # Calculate derived metrics
    executive_summary['AvgOrderValue'] = executive_summary['TotalRevenue'] / executive_summary['TotalTransactions']
    executive_summary['AvgItemsPerOrder'] = executive_summary['TotalItems'] / executive_summary['TotalTransactions']

    # Sort by revenue
    executive_summary = executive_summary.sort_values('TotalRevenue', ascending=False)

    # Round for display
    executive_summary = executive_summary.round(2)

    print("Executive Summary - Top 15 Countries:")
    print(executive_summary.head(15))
    return (executive_summary,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    ## Summary

    **Congratulations!** You've completed all exercises with real-world data!

    **Key insights from the UCI Online Retail dataset:**
    - Handled ~540,000 transactions
    - Cleaned messy real-world data (missing values, returns, cancellations)
    - Analyzed sales across 38 countries
    - Identified best-selling products and top customers
    - Created comprehensive business reports

    **Skills mastered:**
    - ✓ Data loading from external sources
    - ✓ Data exploration and quality assessment
    - ✓ Data cleaning (missing values, filtering, validation)
    - ✓ Feature engineering (calculated columns)
    - ✓ Advanced aggregations and grouping
    - ✓ Business intelligence reporting

    **You're now ready for Day 3: Data Visualization & Advanced Analysis!**
    """
    )
    return


if __name__ == "__main__":
    app.run()
