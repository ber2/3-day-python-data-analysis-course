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
    # Day 4, Session 2: A/B Testing in Practice (SOLUTIONS)

    ## Three-Day Data Analysis with Python Course

    **This notebook contains complete solutions to Session 2 exercises.**
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
    mo.md(r"""## Step 1.1: Load the Dataset (SOLUTION)""")
    return


@app.cell
def _(pd):
    import urllib.request

    # Download gaming dataset
    print("Downloading dataset...")
    url = "https://raw.githubusercontent.com/ber2/3-day-python-data-analysis-course/refs/heads/main/day4/online_gaming_behavior_dataset.csv"

    with urllib.request.urlopen(url) as response:
        gaming_df = pd.read_csv(response)

    print(
        f"✓ Dataset loaded: {gaming_df.shape[0]:,} rows × {gaming_df.shape[1]} columns"
    )
    gaming_df
    return (gaming_df,)


@app.cell
def _(mo):
    mo.md(r"""## Step 1.2: Quick Data Exploration (SOLUTION)""")
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
    mo.md(r"""## Step 2.2: Split Data into Groups (SOLUTION)""")
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
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""## Step 2.3: Calculate Descriptive Statistics (SOLUTION)""")
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
    mo.md(r"""## Step 2.4: Visualize Distributions (SOLUTION)""")
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
        labels={
            "InGamePurchases": "Made Purchase",
            "PlayTimeHours": "Play Time (Hours)",
        },
        opacity=0.7,
        color_discrete_map={0: "#e74c3c", 1: "#2ecc71"},
    )
    fig_hist
    return


@app.cell
def _(mo):
    mo.md(r"""## Step 2.5: Run Statistical Test (SOLUTION)""")
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
    ## Exercise 3.1: Compare Engagement by Purchase Status (SOLUTION)

    **Task:** Test whether purchasers have different SessionsPerWeek than non-purchasers.
    """
    )
    return


@app.cell
def _(purchasers):
    purchasers.SessionsPerWeek.describe()
    return


@app.cell
def _(non_purchasers):
    non_purchasers.SessionsPerWeek.describe()
    return


@app.cell
def _(non_purchasers, purchasers):
    # Calculate descriptive statistics
    print("SessionsPerWeek - Descriptive Statistics:\n")

    print("Purchasers:")
    print(f"  Mean: {purchasers['SessionsPerWeek'].mean():.2f} sessions")
    print(f"  Median: {purchasers['SessionsPerWeek'].median():.2f} sessions")
    print(f"  Std Dev: {purchasers['SessionsPerWeek'].std():.2f} sessions")

    print("\nNon-Purchasers:")
    print(f"  Mean: {non_purchasers['SessionsPerWeek'].mean():.2f} sessions")
    print(f"  Median: {non_purchasers['SessionsPerWeek'].median():.2f} sessions")
    print(f"  Std Dev: {non_purchasers['SessionsPerWeek'].std():.2f} sessions")

    print(
        f"\nDifference in means: {purchasers['SessionsPerWeek'].mean() - non_purchasers['SessionsPerWeek'].mean():.2f} sessions"
    )
    return


@app.cell
def _(gaming_df, sns):
    sns.kdeplot(gaming_df, x="SessionsPerWeek", hue="InGamePurchases")
    return


@app.cell
def _(gaming_df, px):
    # Visualization
    fig_sessions = px.box(
        gaming_df,
        x="InGamePurchases",
        y="SessionsPerWeek",
        title="Sessions Per Week: Purchasers vs Non-Purchasers",
        labels={
            "InGamePurchases": "Made Purchase",
            "SessionsPerWeek": "Sessions Per Week",
        },
        color="InGamePurchases",
        color_discrete_map={0: "#e74c3c", 1: "#2ecc71"},
    )
    fig_sessions.update_layout(showlegend=False)
    fig_sessions
    return


@app.cell
def _(non_purchasers, purchasers, stats):
    # Run t-test
    t_stat_sessions, p_val_sessions = stats.ttest_ind(
        purchasers["SessionsPerWeek"], non_purchasers["SessionsPerWeek"]
    )

    print("T-Test Results (SessionsPerWeek):")
    print(f"  t-statistic: {t_stat_sessions:.4f}")
    print(f"  p-value: {p_val_sessions:.4f}")

    if p_val_sessions < 0.05:
        print("\n✓ STATISTICALLY SIGNIFICANT")
        print(
            "  Purchasers and non-purchasers have significantly different session frequencies."
        )
    else:
        print("\n✗ NOT STATISTICALLY SIGNIFICANT")
        print("  No significant difference in session frequency.")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.2: Compare Play Time by Difficulty Level (SOLUTION)

    **Task:** Test whether players on different difficulty levels have different PlayTimeHours.
    """
    )
    return


@app.cell
def _(gaming_df):
    # Split data by difficulty level
    easy_players = gaming_df[gaming_df["GameDifficulty"] == "Easy"]
    medium_players = gaming_df[gaming_df["GameDifficulty"] == "Medium"]
    hard_players = gaming_df[gaming_df["GameDifficulty"] == "Hard"]

    print("PlayTimeHours by Difficulty Level:\n")

    print(f"Easy (n={len(easy_players):,}):")
    print(f"  Mean: {easy_players['PlayTimeHours'].mean():.2f} hours")
    print(f"  Median: {easy_players['PlayTimeHours'].median():.2f} hours")

    print(f"\nMedium (n={len(medium_players):,}):")
    print(f"  Mean: {medium_players['PlayTimeHours'].mean():.2f} hours")
    print(f"  Median: {medium_players['PlayTimeHours'].median():.2f} hours")

    print(f"\nHard (n={len(hard_players):,}):")
    print(f"  Mean: {hard_players['PlayTimeHours'].mean():.2f} hours")
    print(f"  Median: {hard_players['PlayTimeHours'].median():.2f} hours")
    return easy_players, hard_players, medium_players


@app.cell
def _(gaming_df, sns):
    sns.kdeplot(gaming_df, x="PlayTimeHours", hue="GameDifficulty")
    return


@app.cell
def _(gaming_df, px):
    # Visualization
    fig_difficulty = px.box(
        gaming_df,
        x="GameDifficulty",
        y="PlayTimeHours",
        title="Play Time by Difficulty Level",
        labels={
            "GameDifficulty": "Difficulty Level",
            "PlayTimeHours": "Play Time (Hours)",
        },
        color="GameDifficulty",
        color_discrete_map={
            "Easy": "#2ecc71",
            "Medium": "#f39c12",
            "Hard": "#e74c3c",
        },
    )
    fig_difficulty
    return


@app.cell
def _(easy_players, hard_players, medium_players, stats):
    # Run ANOVA test
    f_statistic, p_value_anova = stats.f_oneway(
        easy_players["PlayTimeHours"],
        medium_players["PlayTimeHours"],
        hard_players["PlayTimeHours"],
    )

    print("ANOVA Test Results (PlayTimeHours by Difficulty):")
    print(f"  F-statistic: {f_statistic:.4f}")
    print(f"  p-value: {p_value_anova:.4f}")

    if p_value_anova < 0.05:
        print("\n✓ STATISTICALLY SIGNIFICANT")
        print(
            "  At least one difficulty level has significantly different play time."
        )
    else:
        print("\n✗ NOT STATISTICALLY SIGNIFICANT")
        print("  No significant difference in play time across difficulty levels.")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.3: Compare Engagement Levels by Region (SOLUTION)

    **Task:** Test whether players from different regions have different EngagementLevel distributions.

    We'll use approach #1: Convert to numeric and use ANOVA
    """
    )
    return


@app.cell
def _(gaming_df):
    # Convert EngagementLevel to numeric
    engagement_mapping = {"Low": 1, "Medium": 2, "High": 3}
    gaming_df["EngagementScore"] = gaming_df["EngagementLevel"].map(
        engagement_mapping
    )

    # Split by region
    usa_players = gaming_df[gaming_df["Location"] == "USA"]
    europe_players = gaming_df[gaming_df["Location"] == "Europe"]
    asia_players = gaming_df[gaming_df["Location"] == "Asia"]
    other_players = gaming_df[gaming_df["Location"] == "Other"]

    print("Engagement Score by Region:\n")

    print(f"USA (n={len(usa_players):,}):")
    print(f"  Mean: {usa_players['EngagementScore'].mean():.2f}")
    print(
        f"  High engagement %: {(usa_players['EngagementLevel'] == 'High').sum() / len(usa_players) * 100:.1f}%"
    )

    print(f"\nEurope (n={len(europe_players):,}):")
    print(f"  Mean: {europe_players['EngagementScore'].mean():.2f}")
    print(
        f"  High engagement %: {(europe_players['EngagementLevel'] == 'High').sum() / len(europe_players) * 100:.1f}%"
    )

    print(f"\nAsia (n={len(asia_players):,}):")
    print(f"  Mean: {asia_players['EngagementScore'].mean():.2f}")
    print(
        f"  High engagement %: {(asia_players['EngagementLevel'] == 'High').sum() / len(asia_players) * 100:.1f}%"
    )

    print(f"\nOther (n={len(other_players):,}):")
    print(f"  Mean: {other_players['EngagementScore'].mean():.2f}")
    print(
        f"  High engagement %: {(other_players['EngagementLevel'] == 'High').sum() / len(other_players) * 100:.1f}%"
    )
    return asia_players, europe_players, other_players, usa_players


@app.cell
def _(gaming_df, px):
    # Visualization - stacked bar chart
    engagement_by_region = (
        gaming_df.groupby(["Location", "EngagementLevel"])
        .size()
        .reset_index(name="Count")
    )

    fig_region = px.bar(
        engagement_by_region,
        x="Location",
        y="Count",
        color="EngagementLevel",
        title="Engagement Level Distribution by Region",
        labels={"Count": "Number of Players", "Location": "Region"},
        color_discrete_map={
            "Low": "#e74c3c",
            "Medium": "#f39c12",
            "High": "#2ecc71",
        },
        barmode="group",
    )
    fig_region
    return


@app.cell
def _(asia_players, europe_players, other_players, stats, usa_players):
    # Run ANOVA on engagement scores
    f_stat_region, p_val_region = stats.f_oneway(
        usa_players["EngagementScore"],
        europe_players["EngagementScore"],
        asia_players["EngagementScore"],
        other_players["EngagementScore"],
    )

    print("ANOVA Test Results (Engagement by Region):")
    print(f"  F-statistic: {f_stat_region:.4f}")
    print(f"  p-value: {p_val_region:.4f}")

    if p_val_region < 0.05:
        print("\n✓ STATISTICALLY SIGNIFICANT")
        print(
            "  At least one region has significantly different engagement levels."
        )
    else:
        print("\n✗ NOT STATISTICALLY SIGNIFICANT")
        print("  No significant difference in engagement across regions.")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.4: Free Exploration (SOLUTION)

    **Example:** Do different game genres have different average achievements unlocked?
    """
    )
    return


@app.cell
def _(gaming_df):
    # Hypothesis: Different genres attract players with different achievement-hunting behavior

    print("Achievements Unlocked by Game Genre:\n")

    for genre in gaming_df["GameGenre"].unique():
        genre_data = gaming_df[gaming_df["GameGenre"] == genre]
        print(f"{genre} (n={len(genre_data):,}):")
        print(
            f"  Mean achievements: {genre_data['AchievementsUnlocked'].mean():.1f}"
        )
        print(
            f"  Median achievements: {genre_data['AchievementsUnlocked'].median():.1f}"
        )
        print()
    return


@app.cell
def _(gaming_df, px):
    # Visualization
    fig_genre = px.box(
        gaming_df,
        x="GameGenre",
        y="AchievementsUnlocked",
        title="Achievements Unlocked by Game Genre",
        labels={
            "GameGenre": "Game Genre",
            "AchievementsUnlocked": "Achievements Unlocked",
        },
        color="GameGenre",
    )
    fig_genre
    return


@app.cell
def _(gaming_df, stats):
    # Split by genre
    genres = gaming_df["GameGenre"].unique()
    genre_groups = [
        gaming_df[gaming_df["GameGenre"] == genre]["AchievementsUnlocked"]
        for genre in genres
    ]

    # Run ANOVA
    f_stat_genre, p_val_genre = stats.f_oneway(*genre_groups)

    print("ANOVA Test Results (Achievements by Genre):")
    print(f"  F-statistic: {f_stat_genre:.4f}")
    print(f"  p-value: {p_val_genre:.4f}")

    if p_val_genre < 0.05:
        print("\n✓ STATISTICALLY SIGNIFICANT")
        print("  Different genres show different achievement rates (p < 0.05).")
        print("\n  Note: Statistical significance does not necessarily indicate practical importance.")
    else:
        print("\n✗ NOT STATISTICALLY SIGNIFICANT")
        print("  No significant difference in achievements across genres.")
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 4: Wrap-up Discussion""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Important Reminders

    **Statistical Significance ≠ Practical Significance**
    - A difference can be statistically significant but too small to matter
    - Always consider the magnitude of the effect, not just the p-value
    - Example: A 0.1 hour difference in play time might be significant but not meaningful

    **Correlation ≠ Causation**
    - Just because purchasers play more doesn't mean purchasing causes more play
    - Could be reverse: playing more causes purchasing
    - Or a third factor: engagement drives both
    - Need controlled experiments to establish causation

    **Multiple Comparisons Problem**
    - If you test 20 hypotheses at p < 0.05, you'll get 1 false positive by chance
    - Be cautious when running many tests
    - Focus on hypotheses that matter for business decisions
    - Consider Bonferroni correction: use p < 0.05/n for n tests
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
    - ✓ Recognize limitations of statistical tests

    **Next up:** Session 3 - Gaming Insights Capstone Project

    In Session 3, we'll combine today's A/B testing analysis with funnel analysis to create a comprehensive gaming analytics report!
    """
    )
    return


if __name__ == "__main__":
    app.run()
