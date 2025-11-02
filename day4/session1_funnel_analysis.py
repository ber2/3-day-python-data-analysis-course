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
    # Day 4, Session 1: Deep Dive into Funnel Analysis

    ## Three-Day Data Analysis with Python Course

    **Learning Objectives:**
    - Build multi-stage conversion funnels
    - Calculate and interpret drop-off rates
    - Create segmented funnels by customer dimensions
    - Translate funnel insights into business actions
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Setup: Load Required Libraries""")
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go

    print(f"pandas version: {pd.__version__}")
    return go, pd


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Recap: What is a Funnel?

    A **funnel** represents the customer journey through different stages, showing how many users progress from one stage to the next.

    **Common funnel types:**
    - **Customer lifecycle**: All customers → Repeat → Frequent → VIP
    - **Purchase flow**: Browse → Add to cart → Checkout → Purchase
    - **Engagement stages**: Sign up → Activated → Regular user → Power user

    **Why funnels matter:**
    - Identify where customers drop off
    - Measure conversion rates between stages
    - Guide optimization efforts and experiments
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 1: Load and Prepare the Dataset""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 1.1: Load the UCI Online Retail Dataset

    We'll use the same dataset from Day 3. The code below downloads and loads it.
    """
    )
    return


@app.cell
def _(pd):
    import urllib.request
    import zipfile
    from io import BytesIO

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
    return (retail_df,)


@app.cell
def _(mo):
    mo.md(r"""## Step 1.2: Clean the Dataset""")
    return


@app.cell
def _(retail_df):
    # Clean the dataset
    retail_clean = retail_df.copy()
    original_size = len(retail_clean)

    # Remove missing descriptions
    retail_clean = retail_clean[retail_clean["Description"].notna()]

    # Remove zero or negative quantities
    retail_clean = retail_clean[retail_clean["Quantity"] > 0]

    # Remove zero or negative prices
    retail_clean = retail_clean[retail_clean["UnitPrice"] > 0]

    # Remove cancelled orders
    retail_clean = retail_clean[
        ~retail_clean["InvoiceNo"].astype(str).str.startswith("C")
    ]

    # Remove missing CustomerID
    retail_clean = retail_clean[retail_clean["CustomerID"].notna()]

    cleaned_size = len(retail_clean)
    removed = original_size - cleaned_size

    print(f"Original: {original_size:,} rows")
    print(f"Cleaned: {cleaned_size:,} rows")
    print(f"Removed: {removed:,} rows ({removed / original_size * 100:.1f}%)")
    return (retail_clean,)


@app.cell
def _(mo):
    mo.md(r"""## Step 1.3: Create Customer Summary Table""")
    return


@app.cell
def _(retail_clean):
    # Create customer summary
    customer_summary = retail_clean.groupby("CustomerID").agg(
        {
            "InvoiceNo": "nunique",
            "Quantity": "sum",
            "InvoiceDate": ["min", "max"],
            "Country": lambda x: x.mode()[0] if not x.mode().empty else None,
        }
    )

    customer_summary.columns = [
        "NumOrders",
        "TotalItems",
        "FirstPurchase",
        "LastPurchase",
        "Country",
    ]
    customer_summary = customer_summary.reset_index()

    print(f"Total customers: {len(customer_summary):,}")
    customer_summary.head()
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 2: Building Multi-Stage Funnels""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2.1: Define Funnel Stages

    We'll create a more detailed funnel than Day 3:

    1. **All Customers**: Made at least 1 purchase
    2. **Multiple Item Purchasers**: Bought >5 items in a single order
    3. **Repeat Customers**: Made 2+ orders
    4. **Frequent Buyers**: Made 5+ orders
    5. **VIP Customers**: Made 10+ orders

    **Your task:** Calculate how many customers are in each stage.
    """
    )
    return


@app.cell
def _():
    # TODO: Calculate the number of customers in each funnel stage

    # Stage 1: All Customers
    all_customers = None  # Replace with your code

    # Stage 2: Multiple Item Purchasers (Quantity > 5 in a single order)
    # Hint: Group retail_clean by InvoiceNo, check max Quantity per order,
    # then count unique CustomerIDs
    multiple_item_purchasers = None  # Replace with your code

    # Stage 3: Repeat Customers (2+ orders)
    repeat_customers = None  # Replace with your code

    # Stage 4: Frequent Buyers (5+ orders)
    frequent_buyers = None  # Replace with your code

    # Stage 5: VIP Customers (10+ orders)
    vip_customers = None  # Replace with your code

    # Print results (uncomment when ready)
    # print("Funnel stages:")
    # print(f"  All Customers: {all_customers:,}")
    # print(f"  Multiple Item Purchasers: {multiple_item_purchasers:,}")
    # print(f"  Repeat Customers: {repeat_customers:,}")
    # print(f"  Frequent Buyers: {frequent_buyers:,}")
    # print(f"  VIP Customers: {vip_customers:,}")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2.2: Create Funnel DataFrame

    **Your task:** Create a DataFrame with the funnel stages and counts.
    """
    )
    return


@app.cell
def _():
    # TODO: Create a funnel DataFrame
    # Columns: 'stage' (stage name), 'count' (number of customers)

    funnel_df = None  # Replace with your code

    # Display the funnel (uncomment when ready)
    # funnel_df
    return (funnel_df,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2.3: Calculate Conversion Rates

    **Your task:** Calculate the conversion rate from each stage to the next.

    **Formula:** `conversion_rate = (current_stage_count / previous_stage_count) * 100`
    """
    )
    return


@app.cell
def _():
    # TODO: Add a 'conversion_rate' column to funnel_df
    # Hint: Use .shift(1) to get the previous row's count

    # Calculate conversion rates
    # funnel_df['conversion_rate'] = ...

    # Calculate overall conversion (All → VIP)
    # overall_conversion = ...

    # Display results (uncomment when ready)
    # print("Funnel with conversion rates:")
    # print(funnel_df)
    # print(f"\nOverall conversion (All → VIP): {overall_conversion:.2f}%")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2.4: Visualize the Funnel

    **Your task:** Create a funnel chart using Plotly.
    """
    )
    return


@app.cell
def _(funnel_df, go):
    # TODO: Create a funnel visualization
    # Hint: Use go.Figure(go.Funnel(...))

    fig_funnel = go.Figure(
        go.Funnel(
            y=funnel_df["stage"],
            x=funnel_df["count"],
            textinfo="value+percent previous",
            marker={
                "color": ["#3498db", "#2ecc71", "#f39c12", "#e67e22", "#e74c3c"]
            },
        )
    )

    fig_funnel.update_layout(
        title="Customer Lifecycle Funnel - Multi-Stage Analysis", height=500
    )

    fig_funnel
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Part 3: Segmented Funnel Analysis

    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.1: Funnel by Geography (UK vs International)

    **Your task:** Create separate funnels for UK vs International customers.

    We'll use a simplified funnel for segmentation:
    - All Customers
    - Repeat Customers (2+)
    - Frequent Buyers (5+)
    - VIP Customers (10+)
    """
    )
    return


@app.cell
def _():
    # TODO: Create UK funnel
    uk_customers = None  # Filter customer_summary for Country == 'United Kingdom'

    # Calculate UK funnel stages
    uk_funnel = {
        "All": None,  # len(uk_customers)
        "Repeat (2+)": None,  # len(uk_customers[uk_customers['NumOrders'] >= 2])
        "Frequent (5+)": None,  # etc.
        "VIP (10+)": None,
    }

    # TODO: Create International funnel
    intl_customers = None  # Filter customer_summary for Country != 'United Kingdom'

    intl_funnel = {
        "All": None,
        "Repeat (2+)": None,
        "Frequent (5+)": None,
        "VIP (10+)": None,
    }

    # Print results (uncomment when ready)
    # print("UK Funnel:")
    # for stage, count in uk_funnel.items():
    #     print(f"  {stage}: {count:,}")
    #
    # print("\nInternational Funnel:")
    # for stage, count in intl_funnel.items():
    #     print(f"  {stage}: {count:,}")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.2: Compare Conversion Rates

    **Your task:** Calculate and compare conversion rates for UK vs International.
    """
    )
    return


@app.cell
def _():
    # TODO: Create comparison DataFrame

    comparison_df = None  # Create DataFrame with UK and Intl conversion rates

    # Display (uncomment when ready)
    # comparison_df
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.3: Visualize Side-by-Side Funnels

    **Your task:** Create a grouped bar chart comparing UK vs International funnels.
    """
    )
    return


@app.cell
def _():
    # TODO: Create side-by-side funnel comparison
    # Hint: Use px.bar with barmode='group'

    fig_comparison = None  # Replace with your code

    # Display (uncomment when ready)
    # fig_comparison
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 4: Funnel Insights & Business Actions""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Discussion Questions

    Based on your funnel analysis, discuss with your partner:

    1. **Biggest Drop-off:** Which stage has the largest drop-off? What might be causing this?

    2. **Geographic Differences:** Do UK and International customers behave differently? Why might this be?

    3. **Business Actions:** What are 2-3 specific actions the business could take to improve conversions?

    **Example insights to consider:**
    - If many customers make only 1 purchase, consider email remarketing campaigns
    - If UK customers convert better, investigate what's different (shipping, product selection, marketing?)
    - If the drop from Repeat → Frequent is large, consider a loyalty program
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Challenge: Funnel by Time Period

    **Optional challenge:** Create funnels for different quarters and compare how conversion rates changed over time.

    **Hint:** You'll need to add a Quarter column to retail_clean and group customers by their first purchase quarter.
    """
    )
    return


@app.cell
def _():
    # Your code here (optional challenge)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    ## Summary

    In this session, you learned to:
    - ✓ Build multi-stage conversion funnels
    - ✓ Calculate drop-off and conversion rates
    - ✓ Segment funnels by customer dimensions
    - ✓ Visualize funnels for comparison
    - ✓ Translate funnel metrics into business insights

    **Next up:** Session 2 - A/B Testing in Practice
    """
    )
    return


if __name__ == "__main__":
    app.run()
