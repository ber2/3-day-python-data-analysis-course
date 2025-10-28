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
    # Session 2 Reference: Data Manipulation

    This notebook contains all the code examples from Session 2.
    Use it as a reference if you fall behind during live coding.
    """
    )
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np

    print(f"pandas version: {pd.__version__}")
    return np, pd


@app.cell
def _(mo):
    mo.md(r"""## Part 1: Data Cleaning""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Handling Missing Values""")
    return


@app.cell
def _(pd):
    # Sample data with missing values
    missing_data = {
        "name": ["Alice", "Bob", None, "David", "Eve"],
        "age": [25, 30, 35, None, 28],
        "city": ["NYC", "LA", "Chicago", "NYC", None],
        "salary": [50000, 60000, 55000, 65000, 52000],
    }
    df_missing = pd.DataFrame(missing_data)

    print("DataFrame with missing values:")
    print(df_missing)
    print()
    print("Missing values per column:")
    print(df_missing.isna().sum())
    return missing_data, df_missing


@app.cell
def _(df_missing):
    # Detecting missing values
    print("Missing value locations (True = missing):")
    print(df_missing.isna())
    print()

    # Total missing values
    total_missing = df_missing.isna().sum().sum()
    print(f"Total missing values: {total_missing}")
    print()

    # Percentage of missing values
    print("Percentage missing:")
    print((df_missing.isna().sum() / len(df_missing)) * 100)
    return (total_missing,)


@app.cell
def _(df_missing):
    # Strategy 1: Drop rows with missing values
    df_dropped = df_missing.dropna()
    print("After dropping rows with ANY missing values:")
    print(df_dropped)
    print(f"Rows remaining: {len(df_dropped)} out of {len(df_missing)}")
    return (df_dropped,)


@app.cell
def _(df_missing):
    # Strategy 2: Fill missing values
    df_filled = df_missing.copy()
    df_filled["age"].fillna(df_missing["age"].median(), inplace=True)
    df_filled["city"].fillna("Unknown", inplace=True)
    df_filled["name"].fillna("Anonymous", inplace=True)

    print("After filling missing values:")
    print(df_filled)
    print()
    print("Missing values remaining:")
    print(df_filled.isna().sum())
    return (df_filled,)


@app.cell
def _(mo):
    mo.md(r"""### Removing Duplicates""")
    return


@app.cell
def _(pd):
    # Data with duplicates
    transactions_dup = pd.DataFrame(
        {
            "transaction_id": [1, 2, 3, 2, 4, 5, 3],
            "customer": ["Alice", "Bob", "Carol", "Bob", "David", "Eve", "Carol"],
            "amount": [100, 150, 200, 150, 120, 180, 200],
        }
    )

    print("Transactions with duplicates:")
    print(transactions_dup)
    print()
    print(f"Number of duplicates: {transactions_dup.duplicated().sum()}")
    return (transactions_dup,)


@app.cell
def _(transactions_dup):
    # Remove duplicates
    clean_transactions = transactions_dup.drop_duplicates(subset=["transaction_id"])

    print("After removing duplicates:")
    print(clean_transactions)
    print(f"Rows remaining: {len(clean_transactions)} out of {len(transactions_dup)}")
    return (clean_transactions,)


@app.cell
def _(mo):
    mo.md(r"""### String Operations""")
    return


@app.cell
def _(pd):
    # Messy customer data
    messy_customers = pd.DataFrame(
        {
            "name": [" Alice ", "bob", "CAROL ", " david"],
            "email": [
                "ALICE@GMAIL.COM",
                "bob@yahoo.com",
                "carol@GMAIL.COM",
                "david@outlook.com",
            ],
            "phone": ["123-456-7890", "234.567.8901", "345 678 9012", "456-567-8901"],
        }
    )

    print("Original messy data:")
    print(messy_customers)
    return (messy_customers,)


@app.cell
def _(messy_customers):
    # Clean up strings
    cleaned_customers = messy_customers.copy()
    cleaned_customers["name"] = cleaned_customers["name"].str.strip().str.title()
    cleaned_customers["email"] = cleaned_customers["email"].str.lower()
    cleaned_customers["phone"] = cleaned_customers["phone"].str.replace(
        r"[.\-\s]", "", regex=True
    )

    print("Cleaned data:")
    print(cleaned_customers)
    return (cleaned_customers,)


@app.cell
def _(mo):
    mo.md(r"""### Type Conversion""")
    return


@app.cell
def _(pd):
    # Data with wrong types
    sales_wrong_types = pd.DataFrame(
        {
            "date": ["2024-01-15", "2024-01-16", "2024-01-17"],
            "amount": ["1000", "1500", "1200"],
            "category": ["A", "B", "A"],
        }
    )

    print("Original types:")
    print(sales_wrong_types.dtypes)
    print()
    print(sales_wrong_types)
    return (sales_wrong_types,)


@app.cell
def _(sales_wrong_types, pd):
    # Convert to correct types
    sales_correct_types = sales_wrong_types.copy()
    sales_correct_types["date"] = pd.to_datetime(sales_correct_types["date"])
    sales_correct_types["amount"] = pd.to_numeric(sales_correct_types["amount"])
    sales_correct_types["category"] = sales_correct_types["category"].astype("category")

    print("Converted types:")
    print(sales_correct_types.dtypes)
    print()
    print(sales_correct_types)
    return (sales_correct_types,)


@app.cell
def _(mo):
    mo.md(r"""## Part 2: Data Transformation""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Adding New Columns""")
    return


@app.cell
def _(pd):
    # Sales data
    sales_data = pd.DataFrame(
        {
            "product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
            "quantity": [5, 50, 30, 10],
            "unit_price": [999.99, 29.99, 79.99, 299.99],
            "cost": [700, 15, 40, 200],
        }
    )

    print("Original sales data:")
    print(sales_data)
    return (sales_data,)


@app.cell
def _(sales_data):
    # Calculate derived columns
    sales_with_calcs = sales_data.copy()
    sales_with_calcs["total_revenue"] = (
        sales_with_calcs["quantity"] * sales_with_calcs["unit_price"]
    )
    sales_with_calcs["total_cost"] = (
        sales_with_calcs["quantity"] * sales_with_calcs["cost"]
    )
    sales_with_calcs["profit"] = (
        sales_with_calcs["total_revenue"] - sales_with_calcs["total_cost"]
    )
    sales_with_calcs["margin_pct"] = (
        sales_with_calcs["profit"] / sales_with_calcs["total_revenue"]
    ) * 100

    print("With calculated columns:")
    print(sales_with_calcs)
    return (sales_with_calcs,)


@app.cell
def _(mo):
    mo.md(r"""### Removing and Renaming Columns""")
    return


@app.cell
def _(sales_with_calcs):
    # Drop columns
    sales_simplified = sales_with_calcs.drop(["cost", "unit_price"], axis=1)
    print("After dropping columns:")
    print(sales_simplified)
    return (sales_simplified,)


@app.cell
def _(sales_data):
    # Rename columns
    sales_renamed = sales_data.rename(
        columns={"unit_price": "price", "quantity": "qty"}
    )
    print("After renaming columns:")
    print(sales_renamed)
    return (sales_renamed,)


@app.cell
def _(mo):
    mo.md(r"""### Applying Functions""")
    return


@app.cell
def _(pd):
    # Customer data for function application
    customers_for_func = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Carol", "David"],
            "age": [25, 45, 35, 60],
            "purchases": [5, 15, 8, 25],
        }
    )

    print("Customer data:")
    print(customers_for_func)
    return (customers_for_func,)


@app.cell
def _(customers_for_func):
    # Apply function to categorize by age
    def age_group(age):
        if age < 30:
            return "Young"
        elif age < 50:
            return "Middle"
        else:
            return "Senior"

    customers_with_age_group = customers_for_func.copy()
    customers_with_age_group["age_group"] = customers_with_age_group["age"].apply(
        age_group
    )

    print("With age groups:")
    print(customers_with_age_group)
    return age_group, customers_with_age_group


@app.cell
def _(customers_for_func):
    # Apply function row-wise
    def calculate_discount(row):
        if row["purchases"] > 20:
            return 0.15  # 15% discount
        elif row["purchases"] > 10:
            return 0.10  # 10% discount
        else:
            return 0.05  # 5% discount

    customers_with_discount = customers_for_func.copy()
    customers_with_discount["discount_rate"] = customers_with_discount.apply(
        calculate_discount, axis=1
    )

    print("With discount rates:")
    print(customers_with_discount)
    return calculate_discount, customers_with_discount


@app.cell
def _(mo):
    mo.md(r"""### Mapping Values""")
    return


@app.cell
def _(pd):
    # Status codes to full names
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5],
            "status": ["A", "I", "P", "A", "P"],
            "amount": [100, 200, 150, 300, 250],
        }
    )

    print("Orders with status codes:")
    print(orders)
    return (orders,)


@app.cell
def _(orders):
    # Map status codes
    status_map = {"A": "Active", "I": "Inactive", "P": "Pending"}

    orders_with_status = orders.copy()
    orders_with_status["status_full"] = orders_with_status["status"].map(status_map)

    print("With full status names:")
    print(orders_with_status)
    return orders_with_status, status_map


@app.cell
def _(mo):
    mo.md(r"""### Sorting Data""")
    return


@app.cell
def _(pd):
    # Sales data for sorting
    sales_for_sorting = pd.DataFrame(
        {
            "region": ["East", "West", "East", "North", "West"],
            "sales": [1200, 1800, 900, 1500, 2100],
            "profit": [200, 350, 150, 280, 420],
        }
    )

    print("Original:")
    print(sales_for_sorting)
    return (sales_for_sorting,)


@app.cell
def _(sales_for_sorting):
    # Sort by sales (descending)
    print("Sorted by sales (highest first):")
    print(sales_for_sorting.sort_values("sales", ascending=False))
    return


@app.cell
def _(sales_for_sorting):
    # Sort by multiple columns
    print("Sorted by region, then profit:")
    print(sales_for_sorting.sort_values(["region", "profit"], ascending=[True, False]))
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 3: Basic Aggregations""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Simple GroupBy""")
    return


@app.cell
def _(np, pd):
    # Transaction data for groupby
    np.random.seed(42)
    transactions_groupby = pd.DataFrame(
        {
            "date": pd.date_range("2024-01-01", periods=20, freq="D"),
            "region": np.random.choice(["East", "West", "North"], 20),
            "product": np.random.choice(["A", "B", "C"], 20),
            "sales": np.random.randint(500, 2000, 20),
            "quantity": np.random.randint(5, 20, 20),
        }
    )

    print("Transaction data:")
    print(transactions_groupby.head(10))
    return (transactions_groupby,)


@app.cell
def _(transactions_groupby):
    # Total sales by region
    sales_by_region = transactions_groupby.groupby("region")["sales"].sum()
    print("Total sales by region:")
    print(sales_by_region)
    return (sales_by_region,)


@app.cell
def _(transactions_groupby):
    # Average quantity by product
    avg_qty_by_product = transactions_groupby.groupby("product")["quantity"].mean()
    print("Average quantity by product:")
    print(avg_qty_by_product)
    return (avg_qty_by_product,)


@app.cell
def _(transactions_groupby):
    # Count of transactions by region
    count_by_region = transactions_groupby.groupby("region").size()
    print("Transaction count by region:")
    print(count_by_region)
    return (count_by_region,)


@app.cell
def _(mo):
    mo.md(r"""### Multiple Aggregations with .agg()""")
    return


@app.cell
def _(transactions_groupby):
    # Multiple aggregations on one column
    sales_summary = transactions_groupby.groupby("region")["sales"].agg(
        ["sum", "mean", "count"]
    )
    print("Sales summary by region:")
    print(sales_summary)
    return (sales_summary,)


@app.cell
def _(transactions_groupby):
    # Different aggregations for different columns
    full_summary = transactions_groupby.groupby("region").agg(
        {"sales": ["sum", "mean"], "quantity": "sum"}
    )
    print("Full summary by region:")
    print(full_summary)
    return (full_summary,)


@app.cell
def _(transactions_groupby):
    # Custom aggregation names
    custom_summary = transactions_groupby.groupby("region")["sales"].agg(
        [("total", "sum"), ("average", "mean"), ("count", "count")]
    )
    print("Custom named aggregations:")
    print(custom_summary)
    return (custom_summary,)


@app.cell
def _(mo):
    mo.md(r"""### GroupBy with Multiple Columns""")
    return


@app.cell
def _(transactions_groupby):
    # Group by region and product
    region_product_sales = transactions_groupby.groupby(["region", "product"])[
        "sales"
    ].sum()
    print("Sales by region and product:")
    print(region_product_sales)
    return (region_product_sales,)


@app.cell
def _(transactions_groupby):
    # Multiple aggregations with multiple groupby columns
    detailed_summary = transactions_groupby.groupby(["region", "product"]).agg(
        {"sales": "sum", "quantity": "sum"}
    )
    print("Detailed summary:")
    print(detailed_summary)
    return (detailed_summary,)


@app.cell
def _(detailed_summary):
    # Reset index to flatten multi-index
    detailed_summary_flat = detailed_summary.reset_index()
    print("Flattened summary:")
    print(detailed_summary_flat)
    return (detailed_summary_flat,)


@app.cell
def _(mo):
    mo.md(r"""### Practical Example: Sales Analysis""")
    return


@app.cell
def _(np, pd):
    # Create comprehensive sales dataset
    np.random.seed(42)
    n_sales_records = 100

    comprehensive_sales = pd.DataFrame(
        {
            "region": np.random.choice(["East", "West", "North", "South"], n_sales_records),
            "product": np.random.choice(["A", "B", "C"], n_sales_records),
            "category": np.random.choice(["Electronics", "Clothing", "Home"], n_sales_records),
            "sales": np.random.randint(500, 2000, n_sales_records),
            "quantity": np.random.randint(5, 20, n_sales_records),
        }
    )

    print("Comprehensive sales dataset created:")
    print(comprehensive_sales.head())
    return comprehensive_sales, n_sales_records


@app.cell
def _(comprehensive_sales):
    # Sales by region and product
    regional_product = comprehensive_sales.groupby(["region", "product"])["sales"].sum()
    print("Sales by region and product:")
    print(regional_product.head(12))
    return (regional_product,)


@app.cell
def _(comprehensive_sales):
    # Product performance
    product_performance = comprehensive_sales.groupby("product").agg(
        {"sales": ["sum", "mean", "count"], "quantity": "sum"}
    )
    print("Product performance:")
    print(product_performance)
    return (product_performance,)


@app.cell
def _(comprehensive_sales):
    # Best performing region
    best_region = comprehensive_sales.groupby("region")["sales"].sum().idxmax()
    best_region_sales = comprehensive_sales.groupby("region")["sales"].sum().max()

    print(f"Best performing region: {best_region}")
    print(f"Total sales: ${best_region_sales:,}")
    return best_region, best_region_sales


@app.cell
def _(comprehensive_sales):
    # Regional summary with multiple metrics
    regional_summary = comprehensive_sales.groupby("region").agg(
        {
            "sales": ["sum", "mean", "count"],
            "quantity": ["sum", "mean"],
        }
    )

    print("Complete regional summary:")
    print(regional_summary)
    return (regional_summary,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Summary

    Key concepts covered:
    - **Data Cleaning**: `.isna()`, `.fillna()`, `.dropna()`, `.drop_duplicates()`
    - **String Operations**: `.str` accessor for vectorized string operations
    - **Type Conversion**: `pd.to_datetime()`, `pd.to_numeric()`, `.astype()`
    - **Transformation**: Adding columns, `.apply()`, `.map()`, `.sort_values()`
    - **Aggregation**: `.groupby()`, `.agg()`, multiple aggregations
    """
    )
    return


if __name__ == "__main__":
    app.run()
