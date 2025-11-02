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
    # Day 4, Session 2: A/B Testing in Practice

    ## Three-Day Data Analysis with Python Course

    **Learning Objectives:**
    - Apply hypothesis testing methodology to real data
    - Compare groups using statistical tests
    - Interpret p-values and statistical significance
    - Make data-driven business recommendations
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
    import seaborn as sns
    import matplotlib.pyplot as plt
    from scipy import stats

    print(f"pandas version: {pd.__version__}")
    return pd, px, sns, stats


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Quick Recap: Hypothesis Testing

    **The Process:**
    1. **State hypotheses:**
       - Null hypothesis (H₀): No difference between groups
       - Alternative hypothesis (H₁): There is a difference

    2. **Collect data:** Measure the metric for both groups

    3. **Run statistical test:** Calculate test statistic and p-value

    4. **Interpret results:**
       - p-value < 0.05: Reject null hypothesis (statistically significant difference)
       - p-value ≥ 0.05: Fail to reject null hypothesis (no significant difference)

    **Common tests:**
    - **t-test**: Compare means of two groups
    - **ANOVA**: Compare means of 3+ groups
    - **Chi-square**: Compare categorical distributions
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 1: Load and Explore Gaming Dataset""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 1.1: Load the Dataset

    We'll load the gaming behavior dataset directly from the data folder.
    """
    )
    return


@app.cell
def _(pd):
    import urllib.request

    # Download gaming dataset
    print("Downloading dataset...")
    url = "https://raw.githubusercontent.com/ber2/3-day-python-data-analysis-course/refs/heads/main/day4/online_gaming_behavior_dataset.csv"

    with urllib.request.urlopen(url) as response:
        gaming_df = pd.read_csv(response)

    print(f"✓ Dataset loaded: {gaming_df.shape[0]:,} rows × {gaming_df.shape[1]} columns")
    gaming_df
    return (gaming_df,)


@app.cell
def _(mo):
    mo.md(r"""## Step 1.2: Quick Data Exploration""")
    return


@app.cell
def _(gaming_df):
    # Display dataset info
    print("Dataset Info:")
    print(gaming_df.info())
    print("\nSummary Statistics:")
    print(gaming_df.describe())
    return


@app.cell
def _(gaming_df):
    # Check key columns
    print("Engagement Levels:")
    print(gaming_df["EngagementLevel"].value_counts())

    print("\nIn-Game Purchases:")
    print(gaming_df["InGamePurchases"].value_counts())

    print("\nGame Difficulty:")
    print(gaming_df["GameDifficulty"].value_counts())
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 2: Guided Analysis - Purchasers vs Non-Purchasers""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Research Question: Do players who make purchases engage differently?

    We'll walk through a complete A/B test analysis together.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 2.1: Define Hypotheses

    **Null Hypothesis (H₀):** Players who purchase and players who don't purchase have the same average play time.

    **Alternative Hypothesis (H₁):** Players who purchase have different average play time than players who don't purchase.

    **Metric:** PlayTimeHours
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Step 2.2: Split Data into Groups""")
    return


@app.cell
def _(gaming_df):
    # Split into purchasers and non-purchasers
    purchasers = gaming_df[gaming_df["InGamePurchases"] == 1]
    non_purchasers = gaming_df[gaming_df["InGamePurchases"] == 0]

    print(f"Purchasers: {len(purchasers):,}")
    print(f"Non-purchasers: {len(non_purchasers):,}")
    return non_purchasers, purchasers


@app.cell
def _(mo):
    mo.md(r"""## Step 2.3: Calculate Descriptive Statistics""")
    return


@app.cell
def _(purchasers):
    purchasers.PlayTimeHours.describe()
    return


@app.cell
def _(non_purchasers):
    non_purchasers.PlayTimeHours.describe()
    return


@app.cell
def _(non_purchasers, purchasers):
    # Calculate summary statistics
    print("PlayTimeHours - Descriptive Statistics:\n")

    print("Purchasers:")
    print(f"  Mean: {purchasers['PlayTimeHours'].mean():.2f} hours")
    print(f"  Median: {purchasers['PlayTimeHours'].median():.2f} hours")
    print(f"  Std Dev: {purchasers['PlayTimeHours'].std():.2f} hours")

    print("\nNon-Purchasers:")
    print(f"  Mean: {non_purchasers['PlayTimeHours'].mean():.2f} hours")
    print(f"  Median: {non_purchasers['PlayTimeHours'].median():.2f} hours")
    print(f"  Std Dev: {non_purchasers['PlayTimeHours'].std():.2f} hours")

    print(
        f"\nDifference in means: {purchasers['PlayTimeHours'].mean() - non_purchasers['PlayTimeHours'].mean():.2f} hours"
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Step 2.4: Visualize Distributions""")
    return


@app.cell
def _(gaming_df, sns):
    sns.kdeplot(gaming_df, x="PlayTimeHours", hue="InGamePurchases")
    return


@app.cell
def _(gaming_df, px):
    # Box plot comparison
    fig_box = px.box(
        gaming_df,
        x="InGamePurchases",
        y="PlayTimeHours",
        title="Play Time Distribution: Purchasers vs Non-Purchasers",
        labels={
            "InGamePurchases": "Made Purchase",
            "PlayTimeHours": "Play Time (Hours)",
        },
        color="InGamePurchases",
        color_discrete_map={0: "#e74c3c", 1: "#2ecc71"},
    )
    fig_box.update_layout(showlegend=False)
    fig_box
    return


@app.cell
def _(gaming_df, px):
    # Histogram comparison
    fig_hist = px.histogram(
        gaming_df,
        x="PlayTimeHours",
        color="InGamePurchases",
        barmode="overlay",
        title="Play Time Distribution by Purchase Status",
        labels={"InGamePurchases": "Made Purchase", "PlayTimeHours": "Play Time (Hours)"},
        opacity=0.7,
        color_discrete_map={0: "#e74c3c", 1: "#2ecc71"},
    )
    fig_hist
    return


@app.cell
def _(mo):
    mo.md(r"""## Step 2.5: Run Statistical Test (t-test)""")
    return


@app.cell
def _(non_purchasers, purchasers, stats):
    # Independent samples t-test
    t_statistic, p_value = stats.ttest_ind(
        purchasers["PlayTimeHours"], non_purchasers["PlayTimeHours"]
    )

    print("T-Test Results:")
    print(f"  t-statistic: {t_statistic:.4f}")
    print(f"  p-value: {p_value:.4f}")

    if p_value < 0.05:
        print("\n✓ Result: STATISTICALLY SIGNIFICANT")
        print(
            "  We reject the null hypothesis. Purchasers and non-purchasers have significantly different play times."
        )
    else:
        print("\n✗ Result: NOT STATISTICALLY SIGNIFICANT")
        print(
            "  We fail to reject the null hypothesis. No significant difference in play time."
        )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 2.6: Business Interpretation

    **What does this mean?**

    If the test is significant (p < 0.05):
    - Purchasers genuinely play more (or less) than non-purchasers
    - This difference is unlikely to be due to random chance
    - **Action:** Consider this when designing monetization strategies

    If not significant (p ≥ 0.05):
    - Any observed difference could be due to random variation
    - We don't have enough evidence to say purchase behavior affects play time
    - **Action:** Look at other metrics or investigate further
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 3: Hands-on Practice - Multiple Comparisons""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.1: Compare Engagement by Purchase Status

    **Your task:** Test whether purchasers have different SessionsPerWeek than non-purchasers.
    """
    )
    return


@app.cell
def _():
    # TODO: Compare SessionsPerWeek between purchasers and non-purchasers

    # Calculate descriptive statistics
    # Your code here

    # Create visualizations (box plot)
    # Your code here

    # Run t-test
    # Your code here

    # Interpret results
    # Your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.2: Compare Play Time by Difficulty Level

    **Your task:** Test whether players on different difficulty levels (Easy/Medium/Hard) have different PlayTimeHours.

    **Hint:** For 3+ groups, use ANOVA instead of t-test: `stats.f_oneway(group1, group2, group3)`
    """
    )
    return


@app.cell
def _():
    # TODO: Split data by difficulty level
    easy_players = None  # gaming_df[gaming_df['GameDifficulty'] == 'Easy']
    medium_players = None
    hard_players = None

    # TODO: Calculate descriptive statistics for each group
    # Your code here

    # TODO: Create visualizations (box plot or violin plot)
    # Your code here

    # TODO: Run ANOVA test
    # f_statistic, p_value = stats.f_oneway(...)
    # Your code here

    # TODO: Interpret results
    # Your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.3: Compare Engagement Levels by Region

    **Your task:** Test whether players from different regions (USA, Europe, Asia) have different EngagementLevel distributions.

    **Challenge:** EngagementLevel is categorical (Low/Medium/High). How would you analyze this?

    **Options:**
    1. Create numeric scores (Low=1, Medium=2, High=3) and use ANOVA
    2. Use a chi-square test for categorical association
    3. Compare proportions of High engagement across regions
    """
    )
    return


@app.cell
def _():
    # TODO: Analyze engagement by region
    # Choose your approach and implement it

    # Your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.4: Free Exploration

    **Your task:** Pick any two groups to compare on any metric. Formulate a hypothesis and test it!

    **Ideas:**
    - Do male vs female players differ in achievements unlocked?
    - Do different game genres attract different session durations?
    - Do younger vs older players prefer different difficulty levels?
    """
    )
    return


@app.cell
def _():
    # TODO: Your own analysis
    # 1. State your hypothesis
    # 2. Define your groups
    # 3. Calculate statistics
    # 4. Visualize
    # 5. Run appropriate test
    # 6. Interpret

    # Your code here
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 4: Wrap-up Discussion""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Key Findings from Today's Analysis

    **Discuss with your partner:**

    1. Which comparisons showed statistically significant differences?

    2. Which findings were most surprising?

    3. If you were a product manager for this game, which findings would you act on? What would you do?

    **Example insights to consider:**
    - If purchasers play more, focus retention efforts on high-engagement players
    - If difficulty level affects engagement, adjust difficulty recommendations
    - If certain regions have higher engagement, investigate what's working there
    - If age correlates with spending, target marketing accordingly
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Important Reminders

    **Statistical Significance ≠ Practical Significance**
    - A difference can be statistically significant but too small to matter
    - Always consider the magnitude of the effect, not just the p-value

    **Correlation ≠ Causation**
    - Just because purchasers play more doesn't mean purchasing causes more play
    - Could be reverse: playing more causes purchasing
    - Or a third factor: engagement drives both

    **Multiple Comparisons Problem**
    - If you test 20 hypotheses at p < 0.05, you'll get 1 false positive by chance
    - Be cautious when running many tests
    - Focus on hypotheses that matter for business decisions
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    ## Summary

    In this session, you learned to:
    - ✓ Apply hypothesis testing to real datasets
    - ✓ Compare groups using t-tests and ANOVA
    - ✓ Interpret p-values and statistical significance
    - ✓ Visualize group differences effectively
    - ✓ Connect statistical findings to business decisions

    **Next up:** Session 3 - Gaming Insights Capstone Project

    In Session 3, we'll combine today's A/B testing analysis with funnel analysis to create a comprehensive gaming analytics report!
    """
    )
    return


if __name__ == "__main__":
    app.run()
