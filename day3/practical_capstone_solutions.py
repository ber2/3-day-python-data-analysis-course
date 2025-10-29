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
    # Day 3, Capstone Project: E-commerce Analytics (SOLUTIONS)

    ## Three-Day Data Analysis with Python Course

    **This notebook contains complete solutions to the capstone project.**
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
    return go, pd, plt, px, sns


@app.cell
def _(mo):
    mo.md(r"""# Part 1: Advanced Data Preparation (SOLUTIONS)""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Step 1.1: Load the Dataset (SOLUTION)""")
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
    mo.md(r"""## Step 1.3: Extract Datetime Features (SOLUTION)""")
    return


@app.cell
def _(retail_clean):
    # Extract datetime features
    retail_clean["Year"] = retail_clean["InvoiceDate"].dt.year
    retail_clean["Month"] = retail_clean["InvoiceDate"].dt.month
    retail_clean["Quarter"] = retail_clean["InvoiceDate"].dt.quarter
    retail_clean["DayOfWeek"] = retail_clean["InvoiceDate"].dt.day_name()
    retail_clean["Hour"] = retail_clean["InvoiceDate"].dt.hour

    print("Datetime features extracted:")
    print(
        retail_clean[
            ["InvoiceDate", "Year", "Month", "Quarter", "DayOfWeek", "Hour"]
        ].head()
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Step 1.4: Create Calculated Columns (SOLUTION)""")
    return


@app.cell
def _(retail_clean):
    # Create calculated columns
    retail_clean["TotalPrice"] = (
        retail_clean["Quantity"] * retail_clean["UnitPrice"]
    )
    retail_clean["InvoiceYearMonth"] = (
        retail_clean["InvoiceDate"].dt.to_period("M").astype(str)
    )

    print("Calculated columns created:")
    print(
        retail_clean[
            ["Quantity", "UnitPrice", "TotalPrice", "InvoiceYearMonth"]
        ].head()
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Step 1.5: Calculate RFM Metrics (SOLUTION)""")
    return


@app.cell
def _(retail_clean):
    # Calculate RFM
    reference_date = retail_clean["InvoiceDate"].max()

    rfm_data = retail_clean.groupby("CustomerID").agg(
        {
            "InvoiceDate": lambda x: (reference_date - x.max()).days,
            "InvoiceNo": "nunique",
            "TotalPrice": "sum",
        }
    )

    rfm_data.columns = ["Recency", "Frequency", "Monetary"]
    rfm_data = rfm_data.reset_index()

    print("RFM metrics calculated:")
    print(rfm_data.head(10))
    print(f"\nTotal customers: {len(rfm_data):,}")
    return (rfm_data,)


@app.cell
def _(mo):
    mo.md(r"""# Part 2: Multi-Dataset Analysis (SOLUTIONS)""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Step 2.1: Create Customer Summary Table (SOLUTION)""")
    return


@app.cell
def _(retail_clean):
    # Customer summary
    customer_summary = retail_clean.groupby("CustomerID").agg(
        {
            "InvoiceNo": "nunique",
            "Quantity": "sum",
            "TotalPrice": "sum",
            "InvoiceDate": ["min", "max"],
            "Country": lambda x: x.mode()[0] if not x.mode().empty else None,
        }
    )

    customer_summary.columns = [
        "NumOrders",
        "TotalItems",
        "TotalRevenue",
        "FirstPurchase",
        "LastPurchase",
        "Country",
    ]
    customer_summary = customer_summary.reset_index()

    print("Customer summary created:")
    print(customer_summary.head())
    return (customer_summary,)


@app.cell
def _(mo):
    mo.md(r"""## Step 2.2: Create Product Summary Table (SOLUTION)""")
    return


@app.cell
def _(retail_clean):
    # Product summary
    product_summary = retail_clean.groupby(["StockCode", "Description"]).agg(
        {
            "Quantity": "sum",
            "TotalPrice": "sum",
            "CustomerID": "nunique",
            "UnitPrice": "mean",
        }
    )

    product_summary.columns = [
        "TotalQuantity",
        "TotalRevenue",
        "UniqueCustomers",
        "AvgUnitPrice",
    ]
    product_summary = product_summary.reset_index()

    print("Product summary created:")
    print(product_summary.head())
    return (product_summary,)


@app.cell
def _(mo):
    mo.md(r"""## Step 2.3: Merge Customer Summary with RFM (SOLUTION)""")
    return


@app.cell
def _(customer_summary, pd, rfm_data):
    # Merge customer summary with RFM
    customer_enriched = pd.merge(
        customer_summary, rfm_data, on="CustomerID", how="inner"
    )

    print("Customer enriched dataset:")
    print(customer_enriched.head())
    print(f"\nShape: {customer_enriched.shape}")
    return (customer_enriched,)


@app.cell
def _(mo):
    mo.md(r"""## Step 2.4: Create Pivot Table (SOLUTION)""")
    return


@app.cell
def _(retail_clean):
    # Pivot table: Country × Quarter
    country_quarter_pivot = retail_clean.pivot_table(
        index="Country",
        columns="Quarter",
        values="TotalPrice",
        aggfunc="sum",
        fill_value=0,
    )

    print("Revenue by Country and Quarter:")
    print(country_quarter_pivot.head(10))
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 3: Interactive Visualizations (SOLUTIONS)""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Visualization 1: Revenue Trends Over Time (SOLUTION)""")
    return


@app.cell
def _(px, retail_clean):
    # Monthly revenue trend
    monthly_revenue_sol = (
        retail_clean.groupby("InvoiceYearMonth")["TotalPrice"].sum().reset_index()
    )
    monthly_revenue_sol.columns = ["Month", "Revenue"]

    fig_revenue_trend = px.line(
        monthly_revenue_sol,
        x="Month",
        y="Revenue",
        title="Monthly Revenue Trend",
        markers=True,
        labels={"Revenue": "Revenue (£)", "Month": "Year-Month"},
    )
    fig_revenue_trend
    return


@app.cell
def _(mo):
    mo.md(r"""## Visualization 2: Top 15 Countries by Revenue (SOLUTION)""")
    return


@app.cell
def _(px, retail_clean):
    # Top countries by revenue
    country_revenue_sol = (
        retail_clean.groupby("Country")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )
    country_revenue_sol.columns = ["Country", "Revenue"]

    fig_top_countries = px.bar(
        country_revenue_sol,
        x="Revenue",
        y="Country",
        orientation="h",
        title="Top 15 Countries by Revenue",
        labels={"Revenue": "Total Revenue (£)"},
        color="Revenue",
        color_continuous_scale="Viridis",
    )
    fig_top_countries
    return


@app.cell
def _(mo):
    mo.md(r"""## Visualization 3: Customer Segmentation (RFM) (SOLUTION)""")
    return


@app.cell
def _(customer_enriched, px):
    # RFM scatter plot
    fig_rfm = px.scatter(
        customer_enriched,
        x="Recency",
        y="Monetary",
        size="Frequency",
        color="Frequency",
        hover_data=["CustomerID", "NumOrders"],
        title="Customer Segmentation (RFM Analysis)",
        labels={
            "Recency": "Days Since Last Purchase",
            "Monetary": "Total Spent (£)",
            "Frequency": "Number of Orders",
        },
        color_continuous_scale="RdYlGn_r",
    )
    fig_rfm
    return


@app.cell
def _(mo):
    mo.md(r"""## Visualization 4: Sales by Hour of Day (SOLUTION)""")
    return


@app.cell
def _(plt, retail_clean, sns):
    # Hourly sales pattern
    hourly_sales_sol = (
        retail_clean.groupby("Hour")["TotalPrice"].sum().reset_index()
    )

    plt.figure(figsize=(12, 6))
    sns.barplot(data=hourly_sales_sol, x="Hour", y="TotalPrice", palette="viridis")
    plt.title("Sales by Hour of Day", fontsize=16)
    plt.xlabel("Hour of Day")
    plt.ylabel("Total Revenue (£)")
    plt.xticks(range(24))
    plt.grid(axis="y", alpha=0.3)
    fig_hourly = plt.gca()
    fig_hourly
    return


@app.cell
def _(mo):
    mo.md(r"""## Visualization 5: Product Performance (SOLUTION)""")
    return


@app.cell
def _(product_summary, px):
    # Top 20 products by revenue
    top_products_sol = product_summary.sort_values(
        "TotalRevenue", ascending=False
    ).head(20)

    fig_products = px.bar(
        top_products_sol,
        x="TotalRevenue",
        y="Description",
        orientation="h",
        title="Top 20 Products by Revenue",
        labels={"TotalRevenue": "Revenue (£)", "Description": "Product"},
        color="TotalRevenue",
        color_continuous_scale="Blues",
    )
    fig_products.update_layout(height=600)
    fig_products
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 4: Funnel Analysis (SOLUTIONS)""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Step 4.1: Define Funnel Stages (SOLUTION)""")
    return


@app.cell
def _(customer_summary):
    # Define funnel stages based on number of orders
    funnel_counts = {
        "All Customers": len(customer_summary),
        "Repeat Customers (2+)": len(
            customer_summary[customer_summary["NumOrders"] >= 2]
        ),
        "Frequent Customers (5+)": len(
            customer_summary[customer_summary["NumOrders"] >= 5]
        ),
        "VIP Customers (10+)": len(
            customer_summary[customer_summary["NumOrders"] >= 10]
        ),
    }

    print("Funnel counts:")
    for stage, count in funnel_counts.items():
        print(f"  {stage}: {count:,}")
    return (funnel_counts,)


@app.cell
def _(mo):
    mo.md(r"""## Step 4.2: Calculate Conversion Rates (SOLUTION)""")
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

    # Overall conversion
    overall_conversion = (
        funnel_df.iloc[-1]["count"] / funnel_df.iloc[0]["count"]
    ) * 100

    print("Funnel with conversion rates:")
    print(funnel_df)
    print(f"\nOverall conversion (All → VIP): {overall_conversion:.2f}%")
    return funnel_df, overall_conversion


@app.cell
def _(mo):
    mo.md(r"""## Step 4.3: Visualize the Funnel (SOLUTION)""")
    return


@app.cell
def _(funnel_df, go):
    # Funnel visualization
    fig_funnel = go.Figure(
        go.Funnel(
            y=funnel_df["stage"],
            x=funnel_df["count"],
            textinfo="value+percent previous",
            marker={"color": ["#3498db", "#2ecc71", "#f39c12", "#e74c3c"]},
        )
    )

    fig_funnel.update_layout(title="Customer Lifecycle Funnel", height=500)

    fig_funnel
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 5: Executive Summary Dashboard (SOLUTION)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Key Performance Indicators

    Below are the key metrics for the business:
    """
    )
    return


@app.cell
def _(overall_conversion, retail_clean):
    # Calculate KPIs
    total_revenue = retail_clean["TotalPrice"].sum()
    total_transactions = retail_clean["InvoiceNo"].nunique()
    total_customers = retail_clean["CustomerID"].nunique()
    avg_order_value = total_revenue / total_transactions
    avg_customer_value = total_revenue / total_customers

    print("📊 KEY PERFORMANCE INDICATORS")
    print("=" * 50)
    print(f"Total Revenue:           £{total_revenue:,.2f}")
    print(f"Total Transactions:      {total_transactions:,}")
    print(f"Total Customers:         {total_customers:,}")
    print(f"Average Order Value:     £{avg_order_value:,.2f}")
    print(f"Customer Lifetime Value: £{avg_customer_value:,.2f}")
    print(f"VIP Conversion Rate:     {overall_conversion:.2f}%")
    print("=" * 50)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Interactive Dashboard

    Use the controls below to filter and explore the data interactively.
    """
    )
    return


@app.cell
def _(mo, retail_clean):
    # Country filter
    country_filter = mo.ui.dropdown(
        options=["All"] + sorted(retail_clean["Country"].unique().tolist()),
        value="United Kingdom",
        label="Select Country:",
    )
    country_filter
    return (country_filter,)


@app.cell
def _(country_filter, retail_clean):
    # Filter data
    if country_filter.value == "All":
        dashboard_df = retail_clean
    else:
        dashboard_df = retail_clean[retail_clean["Country"] == country_filter.value]

    # Calculate metrics for selected country
    country_revenue = dashboard_df["TotalPrice"].sum()
    country_transactions = dashboard_df["InvoiceNo"].nunique()
    country_customers = dashboard_df["CustomerID"].nunique()

    print(f"📍 {country_filter.value}")
    print(f"Revenue: £{country_revenue:,.2f}")
    print(f"Transactions: {country_transactions:,}")
    print(f"Customers: {country_customers:,}")
    return (dashboard_df,)


@app.cell
def _(dashboard_df, px):
    # Reactive chart
    monthly_by_country_dash = (
        dashboard_df.groupby("InvoiceYearMonth")["TotalPrice"].sum().reset_index()
    )

    fig_dashboard = px.line(
        monthly_by_country_dash,
        x="InvoiceYearMonth",
        y="TotalPrice",
        title=f"Monthly Revenue Trend",
        markers=True,
    )
    fig_dashboard
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    ## Business Insights & Recommendations

    Based on the analysis, here are the key findings:

    ### 1. Revenue Trends
    - Revenue shows strong growth in Q4 (holiday season)
    - Identify and replicate success factors from peak months

    ### 2. Geographic Performance
    - United Kingdom dominates revenue (>80%)
    - Opportunity to expand in underperforming markets
    - Consider localization strategies for top 5 countries

    ### 3. Customer Segmentation
    - VIP customers (10+ orders) represent small % but high value
    - Focus retention efforts on this segment
    - Create loyalty program to convert frequent → VIP

    ### 4. Product Insights
    - Top 20 products drive significant revenue
    - Ensure inventory availability for best-sellers
    - Cross-sell opportunities with related products

    ### 5. Timing Patterns
    - Peak shopping hours: 10am-3pm
    - Lower activity in early morning/late evening
    - Optimize customer support for peak hours

    ### Funnel Analysis
    - Conversion from All → VIP: ~3-4%
    - Biggest drop-off: All → Repeat (many one-time buyers)
    - **Action:** Implement email campaigns targeting first-time buyers

    ---

    ## Next Steps

    1. **Immediate Actions:**
       - Launch retention campaign for first-time buyers
       - Ensure stock levels for top 20 products
       - A/B test promotions during off-peak hours

    2. **Strategic Initiatives:**
       - Develop VIP loyalty program
       - Expand marketing in top 5 non-UK countries
       - Investigate Q4 success factors for year-round application

    3. **Further Analysis:**
       - Customer cohort analysis (by signup month)
       - Product category performance deep-dive
       - Seasonal patterns and forecasting
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    ## Congratulations! 🎉

    You've completed the entire capstone project!

    **What you've demonstrated:**
    - ✓ End-to-end data analysis workflow
    - ✓ Advanced pandas techniques (merging, pivoting, time series)
    - ✓ Business-focused visualizations (Plotly + Seaborn)
    - ✓ RFM customer segmentation
    - ✓ Funnel analysis with conversion metrics
    - ✓ Interactive dashboards with marimo
    - ✓ Executive communication skills

    **You are now a data analyst!** 📊

    Keep practicing with real datasets and building your portfolio.
    The skills you've learned are in high demand!
    """
    )
    return


if __name__ == "__main__":
    app.run()
