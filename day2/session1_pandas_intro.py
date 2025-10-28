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
    # Session 1 Reference: Introduction to Pandas

    This notebook contains all the code examples from Session 1.
    Use it as a reference if you fall behind during live coding.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Importing Pandas""")
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
    mo.md(r"""## Part 1: Series - One-Dimensional Labeled Arrays""")
    return


@app.cell
def _(pd):
    # Create a Series from a list
    sales = pd.Series([1200, 1450, 1100, 1800, 2100])
    print("Simple Series:")
    print(sales)
    print()
    return (sales,)


@app.cell
def _(pd):
    # Create a Series with custom index
    daily_sales = pd.Series(
        [1200, 1450, 1100, 1800, 2100], index=["Mon", "Tue", "Wed", "Thu", "Fri"]
    )
    print("Series with custom index:")
    print(daily_sales)
    print()

    # Access by index
    print(f"Monday sales: ${daily_sales['Mon']}")
    return (daily_sales,)


@app.cell
def _(pd):
    # Series from dictionary
    prices = pd.Series(
        {"Laptop": 999.99, "Mouse": 29.99, "Keyboard": 79.99, "Monitor": 299.99}
    )
    print("Series from dictionary:")
    print(prices)
    print()

    # Series attributes
    print(f"Index: {prices.index.tolist()}")
    print(f"Values: {prices.values}")
    print(f"Data type: {prices.dtype}")
    return (prices,)


@app.cell
def _(mo):
    mo.md(r"""## Part 2: DataFrames - Two-Dimensional Labeled Data""")
    return


@app.cell
def _(pd):
    # DataFrame from dictionary of lists
    product_data = {
        "product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
        "price": [999.99, 29.99, 79.99, 299.99],
        "stock": [15, 120, 45, 30],
        "category": ["Computer", "Accessory", "Accessory", "Computer"],
    }

    df = pd.DataFrame(product_data)
    print("DataFrame from dictionary:")
    print(df)
    return product_data, df


@app.cell
def _(pd):
    # DataFrame from list of dictionaries
    customers_list = [
        {"id": 101, "name": "Alice", "city": "NYC", "purchases": 15},
        {"id": 102, "name": "Bob", "city": "LA", "purchases": 8},
        {"id": 103, "name": "Carol", "city": "Chicago", "purchases": 22},
    ]

    customers_df = pd.DataFrame(customers_list)
    print("DataFrame from list of dictionaries:")
    print(customers_df)
    return customers_list, customers_df


@app.cell
def _(mo):
    mo.md(r"""## Part 3: Data Loading and Inspection""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Creating Sample Data

    Let's create a sample CSV-style dataset in memory for demonstration:
    """
    )
    return


@app.cell
def _(np, pd):
    # Create sample customer data
    np.random.seed(42)
    n_customers = 100

    sample_customers = pd.DataFrame(
        {
            "id": range(101, 101 + n_customers),
            "name": [f"Customer_{i}" for i in range(n_customers)],
            "email": [
                f"customer{i}@example.com" if i % 20 != 0 else None
                for i in range(n_customers)
            ],
            "city": np.random.choice(["NYC", "LA", "Chicago", "Boston"], n_customers),
            "purchases": np.random.randint(1, 36, n_customers),
            "total": np.random.uniform(150, 5000, n_customers).round(2),
        }
    )

    print("Sample customer dataset created!")
    print(f"Shape: {sample_customers.shape}")
    return n_customers, sample_customers


@app.cell
def _(mo):
    mo.md(r"""### Basic Inspection Methods""")
    return


@app.cell
def _(sample_customers):
    # .head() - first 5 rows
    print("First 5 rows:")
    print(sample_customers.head())
    return


@app.cell
def _(sample_customers):
    # .tail() - last 5 rows
    print("Last 5 rows:")
    print(sample_customers.tail())
    return


@app.cell
def _(sample_customers):
    # .info() - column information
    print("DataFrame info:")
    sample_customers.info()
    return


@app.cell
def _(sample_customers):
    # .describe() - statistical summary
    print("Statistical summary:")
    print(sample_customers.describe())
    return


@app.cell
def _(sample_customers):
    # Shape and size
    num_rows, num_cols = sample_customers.shape
    print(f"Rows: {num_rows}, Columns: {num_cols}")
    print(f"Total elements: {sample_customers.size}")
    print(f"Row count: {len(sample_customers)}")
    return num_cols, num_rows


@app.cell
def _(sample_customers):
    # Column names and types
    print("Columns:")
    print(sample_customers.columns.tolist())
    print("\nData types:")
    print(sample_customers.dtypes)
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 4: Data Selection and Indexing""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Selecting Columns""")
    return


@app.cell
def _(sample_customers):
    # Single column (returns Series)
    names = sample_customers["name"]
    print(f"Type: {type(names)}")
    print(names.head())
    return (names,)


@app.cell
def _(sample_customers):
    # Multiple columns (returns DataFrame)
    subset = sample_customers[["name", "email", "city"]]
    print(f"Type: {type(subset)}")
    print(subset.head())
    return (subset,)


@app.cell
def _(sample_customers):
    # Calculate on a column
    total_purchases = sample_customers["purchases"].sum()
    avg_purchases = sample_customers["purchases"].mean()
    max_total = sample_customers["total"].max()

    print(f"Total purchases: {total_purchases}")
    print(f"Average purchases per customer: {avg_purchases:.2f}")
    print(f"Highest customer total: ${max_total:.2f}")
    return avg_purchases, max_total, total_purchases


@app.cell
def _(mo):
    mo.md(r"""### Selecting Rows by Position (.iloc)""")
    return


@app.cell
def _(sample_customers):
    # First row
    print("First customer:")
    print(sample_customers.iloc[0])
    return


@app.cell
def _(sample_customers):
    # First 5 rows
    print("First 5 customers:")
    print(sample_customers.iloc[0:5])
    return


@app.cell
def _(sample_customers):
    # Last row
    print("Last customer:")
    print(sample_customers.iloc[-1])
    return


@app.cell
def _(sample_customers):
    # Specific rows
    print("Customers at positions 0, 10, 20:")
    print(sample_customers.iloc[[0, 10, 20]])
    return


@app.cell
def _(mo):
    mo.md(r"""### Selecting Rows by Label (.loc)""")
    return


@app.cell
def _(sample_customers):
    # Set index to customer ID
    customers_indexed = sample_customers.set_index("id")
    print("DataFrame with custom index:")
    print(customers_indexed.head())
    return (customers_indexed,)


@app.cell
def _(customers_indexed):
    # Select by index label
    print("Customer with ID 105:")
    print(customers_indexed.loc[105])
    return


@app.cell
def _(customers_indexed):
    # Select range of labels
    print("Customers 101 to 105:")
    print(customers_indexed.loc[101:105])
    return


@app.cell
def _(mo):
    mo.md(r"""### Boolean Indexing (Filtering)""")
    return


@app.cell
def _(sample_customers):
    # Filter rows where purchases > 20
    active_customers = sample_customers[sample_customers["purchases"] > 20]
    print(f"Active customers (>20 purchases): {len(active_customers)}")
    print(active_customers.head())
    return (active_customers,)


@app.cell
def _(sample_customers):
    # Filter with multiple conditions
    premium = sample_customers[
        (sample_customers["purchases"] > 15) & (sample_customers["total"] > 2000)
    ]
    print(f"Premium customers: {len(premium)}")
    print(premium.head())
    return (premium,)


@app.cell
def _(sample_customers):
    # Filter by string matching
    nyc_customers = sample_customers[sample_customers["city"] == "NYC"]
    print(f"NYC customers: {len(nyc_customers)}")
    print(nyc_customers.head())
    return (nyc_customers,)


@app.cell
def _(sample_customers):
    # Complex filter
    active_nyc = sample_customers[
        (sample_customers["purchases"] > 10) & (sample_customers["city"] == "NYC")
    ]
    print(f"Active NYC customers: {len(active_nyc)}")
    print(active_nyc[["name", "city", "purchases", "total"]].head())
    return (active_nyc,)


@app.cell
def _(mo):
    mo.md(r"""### Combining Selection Methods""")
    return


@app.cell
def _(sample_customers):
    # .loc with row filter and column selection
    high_value_subset = sample_customers.loc[
        sample_customers["total"] > 3000, ["name", "city", "total"]
    ]
    print("High-value customers (specific columns):")
    print(high_value_subset.head())
    return (high_value_subset,)


@app.cell
def _(sample_customers):
    # .iloc with positions
    subset_positions = sample_customers.iloc[0:10, 0:4]
    print("First 10 rows, first 4 columns:")
    print(subset_positions)
    return (subset_positions,)


@app.cell
def _(mo):
    mo.md(r"""## Practical Example: Customer Segmentation""")
    return


@app.cell
def _(sample_customers):
    # Segment 1: VIP customers
    vip = sample_customers[
        (sample_customers["purchases"] > 25) & (sample_customers["total"] > 3000)
    ]

    # Segment 2: At-risk customers
    at_risk = sample_customers[
        (sample_customers["purchases"] < 5) & (sample_customers["total"] < 500)
    ]

    # Segment 3: Active customers
    active = sample_customers[
        (sample_customers["purchases"] >= 10) & (sample_customers["purchases"] <= 25)
    ]

    # Print segment analysis
    total_customers = len(sample_customers)
    print(f"Total customers: {total_customers}")
    print()
    print(f"VIP customers: {len(vip)} ({len(vip)/total_customers*100:.1f}%)")
    print(f"  Average spending: ${vip['total'].mean():.2f}")
    print()
    print(f"At-risk customers: {len(at_risk)} ({len(at_risk)/total_customers*100:.1f}%)")
    print(f"  Average spending: ${at_risk['total'].mean():.2f}")
    print()
    print(f"Active customers: {len(active)} ({len(active)/total_customers*100:.1f}%)")
    print(f"  Average spending: ${active['total'].mean():.2f}")
    return active, at_risk, total_customers, vip


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Summary

    Key concepts covered:
    - **Series**: One-dimensional labeled arrays
    - **DataFrames**: Two-dimensional labeled data structures
    - **Loading data**: Creating DataFrames from various sources
    - **Inspection**: `.head()`, `.tail()`, `.info()`, `.describe()`, `.shape`
    - **Selection**: Column selection, `.loc[]`, `.iloc[]`
    - **Filtering**: Boolean indexing for powerful data filtering
    """
    )
    return


if __name__ == "__main__":
    app.run()
