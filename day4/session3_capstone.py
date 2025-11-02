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
    # Day 4, Session 3: Gaming Insights Capstone Project

    ## Three-Day Data Analysis with Python Course

    **Project Goal:** Combine Session 2's A/B testing analysis with funnel analysis to create a comprehensive gaming analytics report.

    **Deliverable:** Answer 3 key business questions with data and visualizations.
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
    from scipy import stats

    print(f"pandas version: {pd.__version__}")
    return go, pd, px


@app.cell
def _(mo):
    mo.md(r"""## Load Gaming Dataset""")
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
    mo.md(r"""# Part 1: Guided Funnel Analysis (35 min)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 1.1: Define Engagement Funnel Stages

    We'll create a funnel based on SessionsPerWeek:
    - **All Players**: Everyone in the dataset
    - **Active Players**: SessionsPerWeek ≥ 5
    - **Highly Engaged**: SessionsPerWeek ≥ 10
    - **Super Users**: SessionsPerWeek ≥ 15
    """
    )
    return


@app.cell
def _(gaming_df):
    # Calculate funnel stages
    all_players = len(gaming_df)
    active_players = len(gaming_df[gaming_df["SessionsPerWeek"] >= 5])
    highly_engaged = len(gaming_df[gaming_df["SessionsPerWeek"] >= 10])
    super_users = len(gaming_df[gaming_df["SessionsPerWeek"] >= 15])

    print("Engagement Funnel:")
    print(f"  All Players: {all_players:,}")
    print(f"  Active Players (5+ sessions): {active_players:,}")
    print(f"  Highly Engaged (10+ sessions): {highly_engaged:,}")
    print(f"  Super Users (15+ sessions): {super_users:,}")
    return active_players, all_players, highly_engaged, super_users


@app.cell
def _(mo):
    mo.md(
        r"""## Step 1.2: Create Funnel DataFrame and Calculate Conversion Rates"""
    )
    return


@app.cell
def _(active_players, all_players, highly_engaged, pd, super_users):
    # Create funnel DataFrame
    engagement_funnel_df = pd.DataFrame(
        {
            "stage": [
                "All Players",
                "Active (5+)",
                "Highly Engaged (10+)",
                "Super Users (15+)",
            ],
            "count": [all_players, active_players, highly_engaged, super_users],
        }
    )

    # Calculate conversion rates
    engagement_funnel_df["conversion_rate"] = (
        engagement_funnel_df["count"] / engagement_funnel_df["count"].shift(1) * 100
    )

    # Overall conversion
    overall_engagement_conversion = (super_users / all_players) * 100

    print("Funnel with conversion rates:")
    print(engagement_funnel_df)
    print(
        f"\nOverall conversion (All → Super Users): {overall_engagement_conversion:.2f}%"
    )
    return (engagement_funnel_df,)


@app.cell
def _(mo):
    mo.md(r"""## Step 1.3: Visualize the Engagement Funnel""")
    return


@app.cell
def _(engagement_funnel_df, go):
    # Create engagement funnel visualization
    fig_engagement_funnel = go.Figure(
        go.Funnel(
            y=engagement_funnel_df["stage"],
            x=engagement_funnel_df["count"],
            textinfo="value+percent previous",
            marker={"color": ["#3498db", "#2ecc71", "#f39c12", "#e74c3c"]},
        )
    )

    fig_engagement_funnel.update_layout(
        title="Player Engagement Funnel", height=500
    )

    fig_engagement_funnel
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 1.4: Segment the Funnel by InGamePurchases

    Let's compare funnels for purchasers vs non-purchasers.
    """
    )
    return


@app.cell
def _(gaming_df):
    # Purchaser funnel
    purchasers = gaming_df[gaming_df["InGamePurchases"] == 1]

    purchaser_funnel = {
        "All": len(purchasers),
        "Active (5+)": len(purchasers[purchasers["SessionsPerWeek"] >= 5]),
        "Highly Engaged (10+)": len(
            purchasers[purchasers["SessionsPerWeek"] >= 10]
        ),
        "Super Users (15+)": len(purchasers[purchasers["SessionsPerWeek"] >= 15]),
    }

    # Non-purchaser funnel
    non_purchasers = gaming_df[gaming_df["InGamePurchases"] == 0]

    non_purchaser_funnel = {
        "All": len(non_purchasers),
        "Active (5+)": len(non_purchasers[non_purchasers["SessionsPerWeek"] >= 5]),
        "Highly Engaged (10+)": len(
            non_purchasers[non_purchasers["SessionsPerWeek"] >= 10]
        ),
        "Super Users (15+)": len(
            non_purchasers[non_purchasers["SessionsPerWeek"] >= 15]
        ),
    }

    print("Purchaser Funnel:")
    for stage, count in purchaser_funnel.items():
        print(f"  {stage}: {count:,}")

    print("\nNon-Purchaser Funnel:")
    for stage, count in non_purchaser_funnel.items():
        print(f"  {stage}: {count:,}")
    return non_purchaser_funnel, purchaser_funnel


@app.cell
def _(mo):
    mo.md(r"""## Step 1.5: Visualize Segmented Funnels""")
    return


@app.cell
def _(non_purchaser_funnel, pd, purchaser_funnel, px):
    # Create comparison data
    funnel_comparison = pd.DataFrame(
        {
            "Stage": list(purchaser_funnel.keys())
            + list(non_purchaser_funnel.keys()),
            "Count": list(purchaser_funnel.values())
            + list(non_purchaser_funnel.values()),
            "Segment": ["Purchasers"] * len(purchaser_funnel)
            + ["Non-Purchasers"] * len(non_purchaser_funnel),
        }
    )

    fig_funnel_comparison = px.bar(
        funnel_comparison,
        x="Stage",
        y="Count",
        color="Segment",
        barmode="group",
        title="Engagement Funnel: Purchasers vs Non-Purchasers",
        labels={"Count": "Number of Players", "Stage": "Funnel Stage"},
        color_discrete_map={"Purchasers": "#2ecc71", "Non-Purchasers": "#e74c3c"},
    )

    fig_funnel_comparison.update_layout(height=500)
    fig_funnel_comparison
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 1.6: Segment by Difficulty Level (Optional)

    Quick exploration: Does difficulty level affect the engagement funnel?
    """
    )
    return


@app.cell
def _(gaming_df):
    # Calculate conversion to Super Users by difficulty
    for difficulty in ["Easy", "Medium", "Hard"]:
        difficulty_players = gaming_df[gaming_df["GameDifficulty"] == difficulty]
        total = len(difficulty_players)
        super_users_difficulty = len(
            difficulty_players[difficulty_players["SessionsPerWeek"] >= 15]
        )
        conversion = (super_users_difficulty / total * 100) if total > 0 else 0
        print(
            f"{difficulty}: {super_users_difficulty:,} / {total:,} = {conversion:.1f}%"
        )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 2: Synthesis & Recommendations (35 min)

    **Work independently or in pairs to answer the 3 business questions below.**

    Use the insights from:
    - Session 2's A/B testing analysis
    - Part 1's funnel analysis above

    Create visualizations and write brief answers (2-3 sentences each).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Question 1: Player Segmentation

    **What are the key player segments and how do they differ?**

    Consider:
    - Purchasers vs non-purchasers
    - Different engagement levels (Low/Medium/High)
    - Different difficulty preferences
    - Regional differences

    **Your analysis:**
    """
    )
    return


@app.cell
def _():
    # TODO: Your code here
    # Examples:
    # - Create summary statistics by segment
    # - Visualize distributions
    # - Identify the most valuable segment

    # Your code here
    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Your answer:**

    [Write 2-3 sentences summarizing key player segments]
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Question 2: Engagement Funnel

    **Where do we lose players? What characterizes players who progress through the funnel?**

    Consider:
    - Which stage has the biggest drop-off?
    - What traits do Super Users have vs casual players?
    - Are there differences between purchaser and non-purchaser funnels?

    **Your analysis:**
    """
    )
    return


@app.cell
def _():
    # TODO: Your code here
    # Examples:
    # - Compare characteristics of players at different funnel stages
    # - Identify patterns in who becomes a Super User
    # - Visualize differences

    # Your code here
    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Your answer:**

    [Write 2-3 sentences about funnel insights]
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Question 3: Monetization

    **What factors correlate with in-game purchases?**

    Consider:
    - Do purchasers play more? Have more sessions?
    - Do they prefer certain difficulty levels or genres?
    - Are they more or less likely to be highly engaged?

    **Your analysis:**
    """
    )
    return


@app.cell
def _():
    # TODO: Your code here
    # Examples:
    # - Compare metrics between purchasers and non-purchasers
    # - Test statistical significance
    # - Identify purchase drivers

    # Your code here
    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Your answer:**

    [Write 2-3 sentences about monetization insights]
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Summary: Business Recommendations

    Based on your analysis, what are 3-5 actionable recommendations for the game developer?

    **Your recommendations:**

    1. [Recommendation 1]

    2. [Recommendation 2]

    3. [Recommendation 3]

    4. [Recommendation 4 - optional]

    5. [Recommendation 5 - optional]
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    ## Optional: Create a Simple Dashboard

    If you have extra time, create an interactive dashboard with a filter.

    **Example:** Add a dropdown to filter by game genre and show metrics for that genre.
    """
    )
    return


@app.cell
def _(gaming_df, mo):
    # Example: Genre filter
    genre_filter = mo.ui.dropdown(
        options=["All"] + sorted(gaming_df["GameGenre"].unique().tolist()),
        value="All",
        label="Select Genre:",
    )
    genre_filter
    return (genre_filter,)


@app.cell
def _(gaming_df, genre_filter):
    # Filter data based on selection
    if genre_filter.value == "All":
        filtered_df = gaming_df
    else:
        filtered_df = gaming_df[gaming_df["GameGenre"] == genre_filter.value]

    # Display metrics
    print(f"📊 {genre_filter.value} - Key Metrics:")
    print(f"  Total Players: {len(filtered_df):,}")
    print(f"  Avg Play Time: {filtered_df['PlayTimeHours'].mean():.1f} hours")
    print(f"  Avg Sessions/Week: {filtered_df['SessionsPerWeek'].mean():.1f}")
    print(
        f"  Purchase Rate: {(filtered_df['InGamePurchases'].sum() / len(filtered_df) * 100):.1f}%"
    )
    return (filtered_df,)


@app.cell
def _(filtered_df, px):
    # Example reactive chart
    fig_genre_engagement = px.histogram(
        filtered_df,
        x="EngagementLevel",
        title=f"Engagement Distribution",
        color="EngagementLevel",
        color_discrete_map={
            "Low": "#e74c3c",
            "Medium": "#f39c12",
            "High": "#2ecc71",
        },
    )
    fig_genre_engagement
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    ## Congratulations! 🎉

    You've completed the Day 4 capstone project!

    """
    )
    return


if __name__ == "__main__":
    app.run()
