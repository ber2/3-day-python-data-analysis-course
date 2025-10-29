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
    # Session 2 Reference: Advanced Pandas & Funnel Analysis

    This notebook contains all code examples from Session 2.
    Use it as a reference if you fall behind during live coding.
    """
    )
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go

    print(f"pandas version: {pd.__version__}")
    return go, np, pd, px


@app.cell
def _(mo):
    mo.md(r"""## Part 1: Merging and Joining Datasets""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Sample Data: Customers and Orders""")
    return


@app.cell
def _(pd):
    # Customers table
    customers_base = pd.DataFrame(
        {
            "customer_id": [1, 2, 3, 4, 5],
            "name": ["Alice", "Bob", "Carol", "David", "Eve"],
            "city": ["NYC", "LA", "Chicago", "Boston", "Seattle"],
        }
    )

    # Orders table
    orders_base = pd.DataFrame(
        {
            "order_id": [101, 102, 103, 104, 105, 106],
            "customer_id": [1, 1, 2, 3, 6, 2],  # Note: customer 6 doesn't exist!
            "amount": [100, 150, 200, 120, 300, 180],
            "order_date": [
                "2024-01-15",
                "2024-01-20",
                "2024-01-18",
                "2024-01-22",
                "2024-01-25",
                "2024-01-28",
            ],
        }
    )

    print("Customers:")
    print(customers_base)
    print("\nOrders:")
    print(orders_base)
    return customers_base, orders_base


@app.cell
def _(mo):
    mo.md(r"""### Inner Join""")
    return


@app.cell
def _(customers_base, orders_base, pd):
    # Inner join - only matching rows
    inner_merged = pd.merge(
        customers_base, orders_base, on="customer_id", how="inner"
    )
    print("Inner join (only matching customers):")
    print(inner_merged)
    print(
        f"\nRows: {len(inner_merged)} (customer 4, 5, and order from customer 6 excluded)"
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Left Join""")
    return


@app.cell
def _(customers_base, orders_base, pd):
    # Left join - all customers, matching orders
    left_merged = pd.merge(
        customers_base, orders_base, on="customer_id", how="left"
    )
    print("Left join (all customers):")
    print(left_merged)
    print("\nNote: David and Eve have NaN for order columns")
    return


@app.cell
def _(mo):
    mo.md(r"""### Right Join""")
    return


@app.cell
def _(customers_base, orders_base, pd):
    # Right join - all orders, matching customers
    right_merged = pd.merge(
        customers_base, orders_base, on="customer_id", how="right"
    )
    print("Right join (all orders):")
    print(right_merged)
    print(
        "\nNote: Order 105 from non-existent customer 6 has NaN for customer info"
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Outer Join""")
    return


@app.cell
def _(customers_base, orders_base, pd):
    # Outer join - all customers AND all orders
    outer_merged = pd.merge(
        customers_base, orders_base, on="customer_id", how="outer"
    )
    print("Outer join (everything):")
    print(outer_merged)
    print("\nNote: Includes customers without orders AND orders without customers")
    return


@app.cell
def _(mo):
    mo.md(r"""### Merge on Multiple Columns""")
    return


@app.cell
def _(pd):
    # Sales and targets by date and region
    sales_by_region = pd.DataFrame(
        {
            "date": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02"],
            "region": ["East", "West", "East", "West"],
            "sales": [1000, 1500, 1200, 1800],
        }
    )

    targets_by_region = pd.DataFrame(
        {
            "date": ["2024-01-01", "2024-01-01", "2024-01-02"],
            "region": ["East", "West", "East"],
            "target": [1100, 1400, 1300],
        }
    )

    # Merge on both columns
    merged_multi = pd.merge(
        sales_by_region, targets_by_region, on=["date", "region"], how="left"
    )
    print("Merged on date AND region:")
    print(merged_multi)
    return


@app.cell
def _(mo):
    mo.md(r"""### Concatenating DataFrames""")
    return


@app.cell
def _(pd):
    # January sales
    jan_sales = pd.DataFrame(
        {"date": ["2024-01-15", "2024-01-20"], "amount": [1000, 1200]}
    )

    # February sales
    feb_sales = pd.DataFrame(
        {"date": ["2024-02-10", "2024-02-15"], "amount": [1100, 1300]}
    )

    # Concatenate vertically
    all_sales = pd.concat([jan_sales, feb_sales], ignore_index=True)
    print("Concatenated sales data:")
    print(all_sales)
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 2: Advanced Grouping and Pivoting""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Pivot Table""")
    return


@app.cell
def _(pd):
    # Sales data for pivoting
    sales_data = pd.DataFrame(
        {
            "date": [
                "2024-01",
                "2024-01",
                "2024-01",
                "2024-02",
                "2024-02",
                "2024-02",
            ],
            "region": ["East", "West", "East", "East", "West", "East"],
            "product": ["A", "A", "B", "A", "A", "B"],
            "sales": [1000, 1500, 800, 1200, 1800, 900],
        }
    )

    print("Original data:")
    print(sales_data)
    return (sales_data,)


@app.cell
def _(sales_data):
    # Pivot table: date x region, sum sales
    pivot_simple = sales_data.pivot_table(
        index="date", columns="region", values="sales", aggfunc="sum", fill_value=0
    )

    print("\nPivot table (date × region):")
    print(pivot_simple)
    return


@app.cell
def _(sales_data):
    # More complex pivot: region x product
    pivot_complex = sales_data.pivot_table(
        index="region",
        columns="product",
        values="sales",
        aggfunc="sum",
        fill_value=0,
    )

    print("Pivot table (region × product):")
    print(pivot_complex)
    return


@app.cell
def _(mo):
    mo.md(r"""### Crosstab""")
    return


@app.cell
def _(pd):
    # Customer tier and product category
    orders_data = pd.DataFrame(
        {
            "customer_tier": [
                "Gold",
                "Silver",
                "Gold",
                "Bronze",
                "Silver",
                "Gold",
                "Bronze",
                "Silver",
            ],
            "product_category": [
                "Electronics",
                "Clothing",
                "Electronics",
                "Home",
                "Clothing",
                "Home",
                "Electronics",
                "Electronics",
            ],
        }
    )

    # Crosstab - count of each combination
    crosstab_result = pd.crosstab(
        orders_data["customer_tier"], orders_data["product_category"]
    )

    print("Crosstab (tier × category):")
    print(crosstab_result)
    return (orders_data,)


@app.cell
def _(orders_data, pd):
    # Crosstab with percentages
    crosstab_pct = pd.crosstab(
        orders_data["customer_tier"],
        orders_data["product_category"],
        normalize="index",  # Row percentages
    )

    print("\nCrosstab with row percentages:")
    print(crosstab_pct.round(2))
    return


@app.cell
def _(mo):
    mo.md(r"""### Multi-Index from GroupBy""")
    return


@app.cell
def _(sales_data):
    # GroupBy with multiple columns creates multi-index
    multi_grouped = sales_data.groupby(["region", "product"])["sales"].sum()

    print("Multi-index result:")
    print(multi_grouped)
    print(f"\nIndex levels: {multi_grouped.index.names}")
    return (multi_grouped,)


@app.cell
def _(multi_grouped):
    # Reset index to flatten
    flattened = multi_grouped.reset_index()

    print("Flattened (regular DataFrame):")
    print(flattened)
    return


@app.cell
def _(mo):
    mo.md(r"""### Window Functions""")
    return


@app.cell
def _(np, pd):
    # Daily sales for window functions
    daily_data = pd.DataFrame(
        {
            "date": pd.date_range("2024-01-01", periods=30, freq="D"),
            "sales": np.random.randint(800, 1500, 30),
        }
    )

    # Rolling 7-day average
    daily_data["7day_avg"] = daily_data["sales"].rolling(window=7).mean()

    # Cumulative sum
    daily_data["cumulative"] = daily_data["sales"].cumsum()

    print("Sales with rolling average and cumulative sum:")
    print(daily_data.head(10))
    return (daily_data,)


@app.cell
def _(daily_data, px):
    # Visualize rolling average
    fig_rolling = px.line(
        daily_data,
        x="date",
        y=["sales", "7day_avg"],
        title="Daily Sales with 7-Day Moving Average",
    )
    fig_rolling
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 3: Time Series Basics""")
    return


@app.cell
def _(mo):
    mo.md(r"""### DateTime Accessor""")
    return


@app.cell
def _(np, pd):
    # Sample datetime data
    datetime_df = pd.DataFrame(
        {
            "timestamp": pd.date_range("2024-01-01 09:00", periods=100, freq="h"),
            "sales": np.random.randint(500, 2000, 100),
        }
    )

    # Extract datetime components
    datetime_df["year"] = datetime_df["timestamp"].dt.year
    datetime_df["month"] = datetime_df["timestamp"].dt.month
    datetime_df["day"] = datetime_df["timestamp"].dt.day
    datetime_df["hour"] = datetime_df["timestamp"].dt.hour
    datetime_df["day_of_week"] = datetime_df["timestamp"].dt.day_name()
    datetime_df["quarter"] = datetime_df["timestamp"].dt.quarter

    print("DateTime features extracted:")
    print(datetime_df.head())
    return (datetime_df,)


@app.cell
def _(mo):
    mo.md(r"""### DateTime Filtering""")
    return


@app.cell
def _(datetime_df):
    # Filter by date range
    jan_only_dt = datetime_df[
        (datetime_df["timestamp"] >= "2024-01-01")
        & (datetime_df["timestamp"] < "2024-02-01")
    ]

    print(f"January data: {len(jan_only_dt)} rows")

    # Filter by day of week
    weekends_dt = datetime_df[datetime_df["timestamp"].dt.dayofweek >= 5]
    print(f"Weekend data: {len(weekends_dt)} rows")
    return


@app.cell
def _(mo):
    mo.md(r"""### Resampling""")
    return


@app.cell
def _(datetime_df):
    # Set timestamp as index for resampling
    datetime_indexed = datetime_df.set_index("timestamp")

    # Resample to daily totals
    daily_totals = datetime_indexed["sales"].resample("D").sum()

    print("Daily totals (from hourly data):")
    print(daily_totals.head())
    return


@app.cell
def _(mo):
    mo.md(r"""### Time-based Aggregations""")
    return


@app.cell
def _(datetime_df):
    # Group by hour of day
    by_hour = datetime_df.groupby(datetime_df["timestamp"].dt.hour)["sales"].mean()

    print("Average sales by hour:")
    print(by_hour)
    return


@app.cell
def _(datetime_df):
    # Group by day of week
    by_weekday = datetime_df.groupby(datetime_df["timestamp"].dt.day_name())[
        "sales"
    ].mean()

    print("\nAverage sales by day of week:")
    print(by_weekday)
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 4: Funnel Analysis""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Customer Lifecycle Funnel""")
    return


@app.cell
def _(np, pd):
    # Customer data with lifecycle stages
    np.random.seed(42)
    n_customers = 1000

    funnel_data = pd.DataFrame(
        {
            "customer_id": range(1, n_customers + 1),
            "registered": [True] * n_customers,
            "first_purchase": [True] * 600 + [False] * 400,
            "repeat_purchase": [True] * 300 + [False] * 700,
            "loyal_customer": [True] * 150 + [False] * 850,
        }
    )

    print(f"Total customers: {len(funnel_data)}")
    return (funnel_data,)


@app.cell
def _(funnel_data):
    funnel_data
    return


@app.cell
def _(funnel_data):
    # Count at each stage
    funnel_counts = {
        "Registered": funnel_data["registered"].sum(),
        "First Purchase": funnel_data["first_purchase"].sum(),
        "Repeat Purchase": funnel_data["repeat_purchase"].sum(),
        "Loyal Customer": funnel_data["loyal_customer"].sum(),
    }

    print("Funnel counts:")
    for stage, count in funnel_counts.items():
        print(f"  {stage}: {count}")
    return (funnel_counts,)


@app.cell
def _(mo):
    mo.md(r"""### Conversion Rates""")
    return


@app.cell
def _(funnel_counts, pd):
    # Create funnel DataFrame
    funnel_df = pd.DataFrame(
        {"stage": list(funnel_counts.keys()), "count": list(funnel_counts.values())}
    )

    # Calculate conversion rates
    funnel_df["conversion_rate"] = (
        funnel_df["count"] / funnel_df["count"].shift(1) * 100
    )

    # Overall conversion from first to last
    overall_conversion = (
        funnel_df.iloc[-1]["count"] / funnel_df.iloc[0]["count"]
    ) * 100

    print("Funnel with conversion rates:")
    print(funnel_df)
    print(f"\nOverall conversion (Registered → Loyal): {overall_conversion:.1f}%")
    return (funnel_df,)


@app.cell
def _(mo):
    mo.md(r"""### Visualizing the Funnel""")
    return


@app.cell
def _(funnel_df, go):
    # Funnel chart with Plotly
    fig_funnel = go.Figure(
        go.Funnel(
            y=funnel_df["stage"],
            x=funnel_df["count"],
            textinfo="value+percent previous",
        )
    )

    fig_funnel.update_layout(title="Customer Lifecycle Funnel", height=500)

    fig_funnel
    return


@app.cell
def _(mo):
    mo.md(r"""### Event-Based Funnel""")
    return


@app.cell
def _(pd):
    # User events data
    events = pd.DataFrame(
        {
            "user_id": [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5],
            "event": [
                "view",
                "cart",
                "purchase",
                "view",
                "cart",
                "view",
                "cart",
                "purchase",
                "view",
                "view",
                "view",
            ],
        }
    )

    # Count unique users at each event type
    event_funnel = {
        "Viewed Product": events[events["event"] == "view"]["user_id"].nunique(),
        "Added to Cart": events[events["event"] == "cart"]["user_id"].nunique(),
        "Purchased": events[events["event"] == "purchase"]["user_id"].nunique(),
    }

    print("Event-based funnel:")
    for stg, cnt in event_funnel.items():
        print(f"  {stg}: {cnt} users")
    return (events,)


@app.cell
def _(events):
    events
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Summary

    **Key concepts covered:**
    - **Merging**: Inner, left, right, outer joins (like SQL)
    - **Pivot Tables**: Reshape data for analysis
    - **Multi-Index**: Handle hierarchical groupings
    - **Window Functions**: Rolling averages, cumulative sums
    - **DateTime**: Extract features, filter, resample
    - **Funnel Analysis**: Measure conversion through stages

    **Next**: Capstone project - put it all together!
    """
    )
    return


if __name__ == "__main__":
    app.run()
