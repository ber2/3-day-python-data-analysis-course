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
    # Session 1 Reference: Data Visualization

    This notebook contains all code examples from Session 1.
    Use it as a reference if you fall behind during live coding.
    """
    )
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import seaborn as sns
    import matplotlib.pyplot as plt

    print(f"pandas version: {pd.__version__}")
    return np, pd, plt, px, sns


@app.cell
def _(mo):
    mo.md(r"""## Sample Data: Customer Analytics""")
    return


@app.cell
def _(np, pd):
    # Create sample customer dataset for examples
    np.random.seed(42)
    n = 200

    sample_data = pd.DataFrame({
        'customer_id': range(1, n+1),
        'age': np.random.randint(18, 70, n),
        'total_purchases': np.random.randint(1, 50, n),
        'total_spent': np.random.uniform(100, 5000, n).round(2),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n),
        'customer_tier': np.random.choice(['Bronze', 'Silver', 'Gold', 'Platinum'], n),
        'signup_month': np.random.choice(range(1, 13), n)
    })

    # Add calculated columns
    sample_data['avg_purchase_value'] = (sample_data['total_spent'] / sample_data['total_purchases']).round(2)
    sample_data['age_group'] = pd.cut(sample_data['age'], bins=[0, 30, 50, 100], labels=['Young', 'Adult', 'Senior'])

    print("Sample dataset created:")
    print(sample_data.head())
    return (sample_data,)


@app.cell
def _(mo):
    mo.md(r"""## Part 1: Plotly Express - Interactive Visualizations""")
    return


@app.cell
def _(sample_data):
    sample_data
    return


@app.cell
def _(mo):
    mo.md(r"""### Scatter Plot""")
    return


@app.cell
def _(px, sample_data):
    # Simple scatter plot
    fig_scatter_simple = px.scatter(
        sample_data,
        x='total_purchases',
        y='total_spent',
        title='Customer Purchases vs Spending'
    )
    fig_scatter_simple
    return


@app.cell
def _(px, sample_data):
    # Scatter plot with color and size
    fig_scatter_enhanced = px.scatter(
        sample_data,
        x='total_purchases',
        y='total_spent',
        color='age_group',
        size='avg_purchase_value',
        hover_data=['customer_id', 'region'],
        title='Customer Spending Analysis',
        labels={
            'total_purchases': 'Number of Purchases',
            'total_spent': 'Total Spent (£)',
            'avg_purchase_value': 'Avg Purchase Value'
        }
    )
    fig_scatter_enhanced
    return


app._unparsable_cell(
    r"""
    fig_scatter_enhanced.
    """,
    name="_"
)


@app.cell
def _(mo):
    mo.md(r"""### Bar Chart""")
    return


@app.cell
def _(px, sample_data):
    # Count of customers by region
    region_counts = sample_data['region'].value_counts().reset_index()
    region_counts.columns = ['region', 'count']

    fig_bar = px.bar(
        region_counts,
        x='region',
        y='count',
        title='Customers by Region',
        color='region'
    )
    fig_bar
    return


@app.cell
def _(px, sample_data):
    # Horizontal bar chart - average spending by tier
    tier_spending = sample_data.groupby('customer_tier')['total_spent'].mean() \
        .sort_values() \
        .reset_index()
    tier_spending.columns = ['tier', 'avg_spent']

    fig_bar_h = px.bar(
        tier_spending,
        x='avg_spent',
        y='tier',
        orientation='h',
        title='Average Spending by Customer Tier',
        labels={'avg_spent': 'Average Spent (£)', 'tier': 'Customer Tier'}
    )
    fig_bar_h
    return


@app.cell
def _(mo):
    mo.md(r"""### Line Chart (Time Series)""")
    return


@app.cell
def _(px, sample_data):
    # Monthly signup trend
    monthly_signups = sample_data.groupby('signup_month').size().reset_index()
    monthly_signups.columns = ['month', 'signups']

    fig_line = px.line(
        monthly_signups,
        x='month',
        y='signups',
        title='Customer Signups by Month',
        markers=True,
        labels={'month': 'Month', 'signups': 'Number of Signups'}
    )
    fig_line
    return


@app.cell
def _(mo):
    mo.md(r"""### Histogram""")
    return


@app.cell
def _(px, sample_data):
    # Age distribution
    fig_hist = px.histogram(
        sample_data,
        x='age',
        nbins=20,
        title='Age Distribution of Customers',
        labels={'age': 'Customer Age'}
    )
    fig_hist
    return


@app.cell
def _(px, sample_data):
    # Overlapping histograms by group
    fig_hist_group = px.histogram(
        sample_data,
        x='total_spent',
        color='age_group',
        nbins=30,
        title='Spending Distribution by Age Group',
        labels={'total_spent': 'Total Spent (£)'},
        barmode='overlay',  # or 'group', 'stack'
        opacity=0.7
    )
    fig_hist_group
    return


@app.cell
def _(mo):
    mo.md(r"""### Box Plot""")
    return


@app.cell
def _(px, sample_data):
    # Box plot of spending by region
    fig_box = px.box(
        sample_data,
        x='region',
        y='total_spent',
        color='region',
        title='Spending Distribution by Region',
        labels={'total_spent': 'Total Spent (£)'}
    )
    fig_box
    return


@app.cell
def _(mo):
    mo.md(r"""### Violin Plot""")
    return


@app.cell
def _(px, sample_data):
    # Violin plot (box + distribution shape)
    fig_violin = px.violin(
        sample_data,
        x='customer_tier',
        y='total_spent',
        color='customer_tier',
        box=True,  # Show box plot inside
        title='Spending Distribution by Tier',
        labels={'total_spent': 'Total Spent (£)', 'customer_tier': 'Tier'}
    )
    fig_violin
    return


@app.cell
def _(mo):
    mo.md(r"""### Faceting (Subplots)""")
    return


@app.cell
def _(px, sample_data):
    # Scatter plot faceted by region
    fig_facet = px.scatter(
        sample_data,
        x='total_purchases',
        y='total_spent',
        color='age_group',
        facet_col='region',
        title='Purchases vs Spending by Region',
        labels={
            'total_purchases': 'Purchases',
            'total_spent': 'Spent (£)'
        }
    )
    fig_facet
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 2: Seaborn - Statistical Graphics""")
    return


@app.cell
def _(sns):
    # Set Seaborn theme for beautiful defaults
    sns.set_theme(style='whitegrid')
    sns.set_palette('husl')
    return


@app.cell
def _(mo):
    mo.md(r"""### Distribution Plots""")
    return


@app.cell
def _(plt, sample_data, sns):
    # Histogram with KDE
    plt.figure(figsize=(10, 6))
    sns.histplot(data=sample_data, x='age', kde=True, bins=20)
    plt.title('Age Distribution (with KDE)')
    plt.xlabel('Age')
    plt.ylabel('Count')
    fig_age_kde = plt.gca()
    fig_age_kde
    return


@app.cell
def _(plt, sample_data, sns):
    # Distribution by group
    plt.figure(figsize=(10, 6))
    sns.histplot(data=sample_data, x='total_spent', hue='age_group', bins=30, kde=True, alpha=0.6)
    plt.title('Spending Distribution by Age Group')
    plt.xlabel('Total Spent (£)')
    fig_spending_dist = plt.gca()
    fig_spending_dist
    return


@app.cell
def _(mo):
    mo.md(r"""### Box Plots and Violin Plots""")
    return


@app.cell
def _(plt, sample_data, sns):
    # Box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=sample_data, x='region', y='total_spent')
    plt.title('Spending by Region (Box Plot)')
    plt.ylabel('Total Spent (£)')
    fig_sns_box = plt.gca()
    fig_sns_box
    return


@app.cell
def _(plt, sample_data, sns):
    # Violin plot
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=sample_data, x='customer_tier', y='total_spent')
    plt.title('Spending by Tier (Violin Plot)')
    plt.ylabel('Total Spent (£)')
    plt.xlabel('Customer Tier')
    fig_sns_violin = plt.gca()
    fig_sns_violin
    return


@app.cell
def _(mo):
    mo.md(r"""### Categorical Plots""")
    return


@app.cell
def _(plt, sample_data, sns):
    # Count plot
    plt.figure(figsize=(10, 6))
    sns.countplot(data=sample_data, x='customer_tier', order=['Bronze', 'Silver', 'Gold', 'Platinum'])
    plt.title('Customer Count by Tier')
    plt.xlabel('Tier')
    plt.ylabel('Count')
    fig_count = plt.gca()
    fig_count
    return


@app.cell
def _(plt, sample_data, sns):
    # Bar plot (with aggregation)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=sample_data, x='region', y='total_spent', estimator='mean', errorbar='sd')
    plt.title('Average Spending by Region (with std dev)')
    plt.ylabel('Average Spent (£)')
    fig_sns_bar = plt.gca()
    fig_sns_bar
    return


@app.cell
def _(mo):
    mo.md(r"""### Relationship Plots""")
    return


@app.cell
def _(plt, sample_data, sns):
    # Scatter with regression line
    plt.figure(figsize=(10, 6))
    sns.regplot(data=sample_data, x='total_purchases', y='total_spent', scatter_kws={'alpha': 0.5})
    plt.title('Purchases vs Spending (with trend)')
    plt.xlabel('Total Purchases')
    plt.ylabel('Total Spent (£)')
    fig_regplot = plt.gca()
    fig_regplot
    return


@app.cell
def _(sample_data, sns):
    # Pairplot (matrix of relationships)
    pairplot_data = sample_data[['age', 'total_purchases', 'total_spent', 'avg_purchase_value', 'age_group']]
    fig_pairplot = sns.pairplot(pairplot_data, hue='age_group', diag_kind='kde')
    fig_pairplot
    return


@app.cell
def _(mo):
    mo.md(r"""### Heatmap (Correlation Matrix)""")
    return


@app.cell
def _(plt, sample_data, sns):
    # Calculate correlations
    corr_data = sample_data[['age', 'total_purchases', 'total_spent', 'avg_purchase_value']]
    corr_matrix = corr_data.corr()

    # Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix,
                annot=True,
                fmt='.2f',
                cmap='coolwarm',
                center=0,
                vmin=-1,
                vmax=1,
                square=True,
                linewidths=1)
    plt.title('Feature Correlation Matrix')
    fig_heatmap = plt.gca()
    fig_heatmap
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 3: Marimo Interactive Elements""")
    return


@app.cell
def _(mo, sample_data):
    # Dropdown to select region
    region_selector = mo.ui.dropdown(
        options=['All'] + sorted(sample_data['region'].unique().tolist()),
        value='All',
        label='Select Region:'
    )
    region_selector
    return (region_selector,)


@app.cell
def _(region_selector, sample_data):
    # Filter data based on selection
    if region_selector.value == 'All':
        filtered_data = sample_data
    else:
        filtered_data = sample_data[sample_data['region'] == region_selector.value]

    print(f"Showing data for: {region_selector.value}")
    print(f"Number of customers: {len(filtered_data)}")
    return (filtered_data,)


@app.cell
def _(filtered_data, px):
    # Plot updates automatically when region changes!
    fig_interactive = px.scatter(
        filtered_data,
        x='total_purchases',
        y='total_spent',
        color='age_group',
        title=f'Customer Analysis',
        labels={
            'total_purchases': 'Purchases',
            'total_spent': 'Spent (£)'
        }
    )
    fig_interactive
    return


@app.cell
def _(mo):
    # Slider for age range
    age_slider = mo.ui.range_slider(
        start=18,
        stop=70,
        value=[18, 70],
        label='Age Range:'
    )
    age_slider
    return (age_slider,)


@app.cell
def _(age_slider, sample_data):
    # Filter by age range
    age_filtered = sample_data[
        (sample_data['age'] >= age_slider.value[0]) &
        (sample_data['age'] <= age_slider.value[1])
    ]

    print(f"Customers aged {age_slider.value[0]}-{age_slider.value[1]}: {len(age_filtered)}")
    return (age_filtered,)


@app.cell
def _(age_filtered, px):
    # Age distribution (updates with slider)
    fig_age_dist = px.histogram(
        age_filtered,
        x='age',
        nbins=20,
        title='Age Distribution (Interactive Filter)'
    )
    fig_age_dist
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Summary

    **Key concepts covered:**
    - **Plotly Express**: Interactive visualizations with simple syntax
    - **Seaborn**: Statistical plots with beautiful defaults
    - **DataFrame-based plotting**: Pass df, specify columns by name
    - **Chart types**: Scatter, line, bar, histogram, box, violin, heatmap
    - **Customization**: Colors, sizes, labels, titles, facets
    - **Marimo UI**: Reactive dashboards with dropdowns, sliders

    **Next**: Practice session - create visualizations for business insights!
    """
    )
    return


if __name__ == "__main__":
    app.run()
