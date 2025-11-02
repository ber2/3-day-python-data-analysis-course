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
    # Day 4, Session 1: Deep Dive into Funnel Analysis (SOLUTIONS)

    ## Three-Day Data Analysis with Python Course

    **This notebook contains complete solutions to Session 1 exercises.**
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
    return go, pd, px


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
    mo.md(r"""## Step 1.1: Load the UCI Online Retail Dataset (SOLUTION)""")
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
    mo.md(r"""## Step 1.2: Clean the Dataset (SOLUTION)""")
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
    mo.md(r"""## Step 1.3: Create Customer Summary Table (SOLUTION)""")
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
    return (customer_summary,)


@app.cell
def _(mo):
    mo.md(r"""# Part 2: Building Multi-Stage Funnels""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 2.1: Define Funnel Stages (SOLUTION)""")
    return


@app.cell
def _(customer_summary, retail_clean):
    # Stage 1: All Customers
    all_customers = len(customer_summary)

    # Stage 2: Multiple Item Purchasers (Quantity > 5 in a single order)
    orders_with_multiple_items = (
        retail_clean.groupby("InvoiceNo")["Quantity"].max().reset_index()
    )
    orders_multiple = orders_with_multiple_items[
        orders_with_multiple_items["Quantity"] > 5
    ]
    invoices_multiple = orders_multiple["InvoiceNo"].unique()
    customers_multiple = retail_clean[
        retail_clean["InvoiceNo"].isin(invoices_multiple)
    ]["CustomerID"].nunique()
    multiple_item_purchasers = customers_multiple

    # Stage 3: Repeat Customers (2+ orders)
    repeat_customers = len(customer_summary[customer_summary["NumOrders"] >= 2])

    # Stage 4: Frequent Buyers (5+ orders)
    frequent_buyers = len(customer_summary[customer_summary["NumOrders"] >= 5])

    # Stage 5: VIP Customers (10+ orders)
    vip_customers = len(customer_summary[customer_summary["NumOrders"] >= 10])

    print("Funnel stages:")
    print(f"  All Customers: {all_customers:,}")
    print(f"  Multiple Item Purchasers: {multiple_item_purchasers:,}")
    print(f"  Repeat Customers: {repeat_customers:,}")
    print(f"  Frequent Buyers: {frequent_buyers:,}")
    print(f"  VIP Customers: {vip_customers:,}")
    return (
        all_customers,
        frequent_buyers,
        multiple_item_purchasers,
        repeat_customers,
        vip_customers,
    )


@app.cell
def _(mo):
    mo.md(r"""## Exercise 2.2: Create Funnel DataFrame (SOLUTION)""")
    return


@app.cell
def _(
    all_customers,
    frequent_buyers,
    multiple_item_purchasers,
    pd,
    repeat_customers,
    vip_customers,
):
    # Create funnel DataFrame
    funnel_df = pd.DataFrame(
        {
            "stage": [
                "All Customers",
                "Multiple Item Purchasers",
                "Repeat Customers",
                "Frequent Buyers",
                "VIP Customers",
            ],
            "count": [
                all_customers,
                multiple_item_purchasers,
                repeat_customers,
                frequent_buyers,
                vip_customers,
            ],
        }
    )

    funnel_df
    return (funnel_df,)


@app.cell
def _(mo):
    mo.md(r"""## Exercise 2.3: Calculate Conversion Rates (SOLUTION)""")
    return


@app.cell
def _(funnel_df):
    # Calculate conversion rates
    funnel_df["conversion_rate"] = (
        funnel_df["count"] / funnel_df["count"].shift(1) * 100
    )

    # Calculate overall conversion (All → VIP)
    overall_conversion = (
        funnel_df.iloc[-1]["count"] / funnel_df.iloc[0]["count"]
    ) * 100

    print("Funnel with conversion rates:")
    print(funnel_df)
    print(f"\nOverall conversion (All → VIP): {overall_conversion:.2f}%")
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 2.4: Visualize the Funnel (SOLUTION)""")
    return


@app.cell
def _(funnel_df, go):
    # Create funnel visualization
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
    mo.md(r"""# Part 3: Segmented Funnel Analysis""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 3.1: Funnel by Geography (SOLUTION)""")
    return


@app.cell
def _(customer_summary):
    # UK funnel
    uk_customers = customer_summary[customer_summary["Country"] == "United Kingdom"]

    uk_funnel = {
        "All": len(uk_customers),
        "Repeat (2+)": len(uk_customers[uk_customers["NumOrders"] >= 2]),
        "Frequent (5+)": len(uk_customers[uk_customers["NumOrders"] >= 5]),
        "VIP (10+)": len(uk_customers[uk_customers["NumOrders"] >= 10]),
    }

    # International funnel
    intl_customers = customer_summary[
        customer_summary["Country"] != "United Kingdom"
    ]

    intl_funnel = {
        "All": len(intl_customers),
        "Repeat (2+)": len(intl_customers[intl_customers["NumOrders"] >= 2]),
        "Frequent (5+)": len(intl_customers[intl_customers["NumOrders"] >= 5]),
        "VIP (10+)": len(intl_customers[intl_customers["NumOrders"] >= 10]),
    }

    # print("UK Funnel:")
    # for stage, count in uk_funnel.items():
        # print(f"  {stage}: {count:,}")

    # print("\nInternational Funnel:")
    # for stage, count in intl_funnel.items():
        # print(f"  {stage}: {count:,}")
    return intl_funnel, uk_funnel


@app.cell
def _(mo):
    mo.md(r"""## Exercise 3.2: Compare Conversion Rates (SOLUTION)""")
    return


@app.cell
def _(intl_funnel, pd, uk_funnel):
    # Calculate conversion rates for each segment
    uk_stages = list(uk_funnel.keys())
    uk_counts = list(uk_funnel.values())
    uk_conversion = [100.0] + [
        (uk_counts[i] / uk_counts[i - 1] * 100) for i in range(1, len(uk_counts))
    ]

    intl_stages = list(intl_funnel.keys())
    intl_counts = list(intl_funnel.values())
    intl_conversion = [100.0] + [
        (intl_counts[i] / intl_counts[i - 1] * 100)
        for i in range(1, len(intl_counts))
    ]

    # Create comparison DataFrame
    comparison_df = pd.DataFrame(
        {
            "Stage": uk_stages,
            "UK_Count": uk_counts,
            "UK_Conversion": uk_conversion,
            "Intl_Count": intl_counts,
            "Intl_Conversion": intl_conversion,
        }
    )

    comparison_df
    return (comparison_df,)


@app.cell
def _(mo):
    mo.md(r"""## Exercise 3.3: Visualize Side-by-Side Funnels (SOLUTION)""")
    return


@app.cell
def _(comparison_df, pd, px):
    # Prepare data for grouped bar chart
    funnel_comparison_data = pd.DataFrame(
        {
            "Stage": list(comparison_df.Stage) + list(comparison_df.Stage),
            "Count": list(comparison_df.UK_Count) + list(comparison_df.Intl_Count),
            "Perc": list(comparison_df.UK_Conversion)
            + list(comparison_df.Intl_Conversion),
            "Segment": ["UK"] * len(comparison_df)
            + ["International"] * len(comparison_df),
        }
    )

    fig_comparison = px.funnel(
        funnel_comparison_data,
        x="Stage",
        y="Perc",
        color="Segment",
        # barmode="group",
        title="Customer Funnel: UK vs International",
        labels={"Count": "Number of Customers", "Stage": "Funnel Stage"},
    )

    fig_comparison.update_layout(height=500)
    fig_comparison
    return (funnel_comparison_data,)


@app.cell
def _(funnel_comparison_data, px):
    fig_comparison_stacked = px.bar(
        funnel_comparison_data,
        x="Segment",
        y="Perc",
        color="Stage",
        barmode="stack",
        title="Customer Funnel: UK vs International",
        labels={"Count": "Number of Customers", "Stage": "Funnel Stage"},
        # color_discrete_map={"UK": "#3498db", "International": "#e74c3c"},
    )

    fig_comparison_stacked.update_layout(height=500)
    fig_comparison_stacked
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 4: Funnel Insights & Business Actions""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Key Insights from the Analysis

    Based on the funnel analysis, here are some example observations:

    ### 1. Drop-off Patterns
    - The funnel shows drop-offs at each stage, though differences between stages are relatively modest
    - Many customers make only a few purchases before stopping

    ### 2. Geographic Patterns
    - UK and International customers show similar funnel patterns
    - Any observed differences may be within normal variation

    ### 3. Overall Conversion Rate
    - A small percentage of customers become VIPs (10+ orders)
    - Most customers make fewer than 5 orders

    ### 4. Considerations for Further Analysis
    - Statistical testing would be needed to determine if observed differences are meaningful
    - Additional data on time periods, customer cohorts, or external factors could provide more context
    - Any business actions should be validated with controlled experiments
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Challenge: Funnel by Time Period (SOLUTION)""")
    return


@app.cell
def _(customer_summary):
    # Add quarter information based on first purchase
    customer_summary["FirstPurchaseQuarter"] = customer_summary[
        "FirstPurchase"
    ].dt.to_period("Q")

    # Calculate funnel for each quarter
    quarters = sorted(customer_summary["FirstPurchaseQuarter"].unique())

    quarterly_funnels = {}
    for quarter in quarters:
        q_customers = customer_summary[
            customer_summary["FirstPurchaseQuarter"] == quarter
        ]
        quarterly_funnels[str(quarter)] = {
            "All": len(q_customers),
            "Repeat (2+)": len(q_customers[q_customers["NumOrders"] >= 2]),
            "Frequent (5+)": len(q_customers[q_customers["NumOrders"] >= 5]),
            "VIP (10+)": len(q_customers[q_customers["NumOrders"] >= 10]),
        }

    # Display results for first 4 quarters
    # print("Quarterly Funnels:")
    # for quarter, funnel in list(quarterly_funnels.items())[:4]:
    #     print(f"\n{quarter}:")
    #     for stage, count in funnel.items():
    #         print(f"  {stage}: {count:,}")
    return (quarterly_funnels,)


@app.cell
def _(pd, px, quarterly_funnels):
    # Visualize quarterly trends
    quarterly_data = []
    for _quarter, funnel in quarterly_funnels.items():
        for stage, count in funnel.items():
            quarterly_data.append(
                {"Quarter": _quarter, "Stage": stage, "Count": count}
            )

    quarterly_df = pd.DataFrame(quarterly_data)

    # Calculate conversion rates
    quarterly_pivot = quarterly_df.pivot(
        index="Quarter", columns="Stage", values="Count"
    )
    quarterly_pivot["Conversion_to_VIP"] = (
        quarterly_pivot["VIP (10+)"] / quarterly_pivot["All"] * 100
    )

    fig_quarterly = px.line(
        quarterly_pivot.reset_index(),
        x="Quarter",
        y="Conversion_to_VIP",
        title="VIP Conversion Rate Over Time",
        labels={
            "Conversion_to_VIP": "Conversion Rate to VIP (%)",
            "Quarter": "Cohort Quarter",
        },
        markers=True,
    )

    fig_quarterly.update_layout(height=400)
    fig_quarterly
    return


app._unparsable_cell(
    r"""
    px.funnel(quarterly_df, x=\"Stage\", y=\"Count\", color=\"
    """,
    name="_"
)


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

    **Key Takeaways:**
    - Funnels help identify where customers drop off
    - Segmented funnels reveal different behavior patterns
    - Small conversion improvements compound across stages
    - Always connect funnel metrics to actionable business decisions

    **Next up:** Session 2 - A/B Testing in Practice
    """
    )
    return


if __name__ == "__main__":
    app.run()
