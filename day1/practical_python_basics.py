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
    # Day 1, Practical Session: Hands-on Python Basics

    ## Three-Day Data Analysis with Python Course

    **Goal:** Apply everything learned today to solve real data problems!
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Practical Session Overview

    This session is **hands-on practice**. We'll work through:

    1. **Warm-up Exercises**
       - Variables, functions, control flow

    2. **Data Structure Challenges**
       - Lists, dictionaries, and practical problems

    3. **NumPy Statistics Practice**
       - Working with arrays and calculations

    4. **Mini-Project: Sales Analysis**
       - Load data, clean it, analyze it, answer business questions

    5. **Wrap-up & Discussion**

    ---

    **Instructions:**
    - Try to solve each exercise yourself first
    - Work at your own pace
    - Ask questions anytime!
    - Solutions will be shared at the end of the day
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 1: Warm-up Exercises

    Let's start with some quick exercises to reinforce the basics.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1.1: Temperature Converter

    **Task:** Write a function that converts Celsius to Fahrenheit.

    **Formula:** `F = (C × 9/5) + 32`

    **Requirements:**
    - Function should take celsius as parameter
    - Return the fahrenheit value
    - Test with: 0°C, 100°C, 37°C
    """
    )
    return


@app.cell
def _():
    # Write your solution here
    def celsius_to_fahrenheit(celsius):
        # Your code here
        pass

    # Test your function
    # print(celsius_to_fahrenheit(0))
    # print(celsius_to_fahrenheit(100))
    # print(celsius_to_fahrenheit(37))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1.2: Grade Calculator

    **Task:** Write a function that takes a score (0-100) and returns a letter grade.

    **Grading scale:**
    - A: 90-100
    - B: 80-89
    - C: 70-79
    - D: 60-69
    - F: 0-59

    **Bonus:** Handle invalid inputs (scores outside 0-100)
    """
    )
    return


@app.cell
def _():
    # Write your solution here
    def get_grade(score):
        # Your code here
        pass

    # Test cases
    # print(get_grade(95))
    # print(get_grade(85))
    # print(get_grade(72))
    # print(get_grade(65))
    # print(get_grade(45))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1.3: Sum of Even Numbers

    **Task:** Write a function that calculates the sum of all even numbers in a list.

    **Example:**
    - Input: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
    - Output: `30` (2+4+6+8+10)
    """
    )
    return


@app.cell
def _():
    # Write your solution here
    def sum_even_numbers(numbers):
        # Your code here
        pass

    # Test
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(sum_even_numbers(numbers))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 2: Data Structure Challenges

    Now let's work with lists, dictionaries, and real-world data scenarios.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2.1: Shopping Cart

    **Task:** Create a shopping cart system using a dictionary.

    **Requirements:**
    1. Start with an empty cart (dictionary)
    2. Add items: `{"product": quantity}`
    3. Update quantities if item already exists
    4. Calculate total number of items
    5. Remove an item

    **Example:**
    ```python
    cart = {}
    add_to_cart(cart, "apple", 3)
    add_to_cart(cart, "banana", 2)
    add_to_cart(cart, "apple", 2)  # Should have 5 apples now
    ```
    """
    )
    return


@app.cell
def _():
    # Write your solution here
    my_cart = {}

    def add_to_cart_user(cart, product, quantity):
        # Your code here
        pass

    def get_total_items_user(cart):
        # Your code here
        pass

    def remove_from_cart_user(cart, product):
        # Your code here
        pass

    # Test your functions
    # add_to_cart_user(my_cart, "apple", 3)
    # add_to_cart_user(my_cart, "banana", 2)
    # print(my_cart)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2.2: Student Records

    **Task:** Work with a list of student dictionaries.

    **Given data:**
    ```python
    students = [
        {"name": "Alice", "age": 20, "grades": [85, 90, 88]},
        {"name": "Bob", "age": 21, "grades": [78, 82, 80]},
        {"name": "Carol", "age": 19, "grades": [92, 95, 93]},
        {"name": "David", "age": 20, "grades": [70, 75, 72]}
    ]
    ```

    **Tasks:**
    1. Calculate average grade for each student
    2. Find the student with highest average
    3. Count students with average > 85
    """
    )
    return


@app.cell
def _():
    students_data = [
        {"name": "Alice", "age": 20, "grades": [85, 90, 88]},
        {"name": "Bob", "age": 21, "grades": [78, 82, 80]},
        {"name": "Carol", "age": 19, "grades": [92, 95, 93]},
        {"name": "David", "age": 20, "grades": [70, 75, 72]}
    ]

    # Write your solution here
    # Calculate averages
    # Find top student
    # Count high achievers
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2.3: Word Frequency Counter

    **Task:** Count how many times each word appears in a sentence.

    **Requirements:**
    - Use a dictionary to store counts
    - Make it case-insensitive
    - Ignore punctuation

    **Example:**
    - Input: `"The quick brown fox jumps over the lazy dog the fox"`
    - Output: `{"the": 3, "quick": 1, "brown": 1, "fox": 2, ...}`
    """
    )
    return


@app.cell
def _():
    # Write your solution here
    def count_words(sentence):
        # Your code here
        pass

    # Test
    # text = "The quick brown fox jumps over the lazy dog the fox"
    # print(count_words(text))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 3: NumPy Statistics Practice

    Time to work with numerical data and NumPy arrays!
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.1: Sales Performance Analysis

    **Task:** Analyze weekly sales data using NumPy.

    **Given:** Daily sales for 4 weeks (28 days)

    **Calculate:**
    1. Weekly totals
    2. Best and worst week
    3. Daily average across all weeks
    4. Days that exceeded the average
    """
    )
    return


@app.cell
def _():
    import numpy as np

    # Daily sales for 4 weeks
    daily_sales_user = np.array([
        1200, 1450, 1100, 1800, 2100, 950, 1350,   # Week 1
        1500, 1600, 1400, 1900, 2200, 1050, 1400,  # Week 2
        1300, 1550, 1200, 1750, 2000, 1000, 1300,  # Week 3
        1400, 1500, 1350, 1850, 2150, 1100, 1450   # Week 4
    ])

    # Write your solution here
    # Hint: Use reshape to organize by weeks
    # sales_by_week = daily_sales_user.reshape(4, 7)
    return (np,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3.2: Temperature Data

    **Task:** Analyze temperature data and detect anomalies.

    **Given:** Daily temperatures for a month

    **Find:**
    1. Average, min, and max temperature
    2. Standard deviation
    3. Days with "extreme" temperatures (> 2 std deviations from mean)
    """
    )
    return


@app.cell
def _(np):
    # Daily temperatures (Celsius)
    temperatures_user = np.array([
        22, 24, 23, 25, 26, 24, 23,
        25, 27, 28, 29, 30, 28, 26,
        24, 23, 22, 21, 20, 19, 18,
        20, 22, 35, 23, 24, 25, 26,
        27, 5
    ])

    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Part 4: Mini-Project - Sales Data Analysis

    **Scenario:** You're a data analyst for a retail company. Your manager gave you sales data and needs answers to business questions.

    **Your tasks:**
    1. Load and inspect the data
    2. Clean the data (handle missing/invalid values)
    3. Answer business questions
    4. Calculate key metrics

    Let's begin!
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 1: Create Sample Dataset

    First, let's create a realistic sales dataset to work with.
    """
    )
    return


@app.cell
def _(np):
    # Create sample sales data
    np.random.seed(42)  # For reproducibility

    # Generate data for 100 transactions
    transaction_ids_data = list(range(1, 101))
    products_data = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
    categories_data = ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics"]

    # Random product selection
    product_choices_data = [products_data[i] for i in np.random.randint(0, 5, 100)]

    # Sales amounts with some variation
    base_prices_data = {"Laptop": 999, "Mouse": 25, "Keyboard": 75, "Monitor": 350, "Headphones": 150}
    amounts_data = [base_prices_data[p] * np.random.uniform(0.8, 1.2) for p in product_choices_data]

    # Quantities
    quantities_data = np.random.randint(1, 5, 100)

    # Add some "bad" data intentionally
    amounts_data[10] = -50  # Negative value (error)
    amounts_data[25] = 0    # Zero value (cancelled?)
    amounts_data[50] = None # Missing value

    # Create the dataset as a list of dictionaries
    sales_data_project = []
    for i in range(100):
        sales_data_project.append({
            "transaction_id": transaction_ids_data[i],
            "product": product_choices_data[i],
            "quantity": int(quantities_data[i]),
            "amount": amounts_data[i]
        })

    print(f"✓ Created dataset with {len(sales_data_project)} transactions")
    print(f"\nFirst 3 transactions:")
    for i in range(3):
        print(f"  {sales_data_project[i]}")
    return (sales_data_project,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 2: Inspect the Data

    **Task:** Write code to understand the data structure.

    Questions to answer:
    - How many transactions?
    - What products do we have?
    - What's the range of amounts?
    """
    )
    return


@app.cell
def _():
    # Inspect the data here
    # Hint: Use len(), loops, sets, etc.

    # Your code here
    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 3: Clean the Data

    **Task:** Remove or fix bad data.

    Requirements:
    - Remove transactions with missing amounts (None)
    - Remove transactions with amount <= 0
    - Create a new "clean" dataset
    """
    )
    return


@app.cell
def _():
    # Clean the data here
    clean_sales_data_user = []

    # Your code here
    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 4: Answer Business Questions

    Now use the clean data to answer these questions:

    **Q1:** What is the total revenue?

    **Q2:** What is the average transaction value?

    **Q3:** Which product generated the most revenue?

    **Q4:** How many units of each product were sold?

    **Q5:** What are the top 3 transactions by amount?
    """
    )
    return


@app.cell
def _():
    # Answer the business questions here

    # Q1: Total revenue
    # Your code here

    # Q2: Average transaction
    # Your code here

    # Q3: Revenue by product
    # Your code here

    # Q4: Units sold by product
    # Your code here

    # Q5: Top 3 transactions
    # Your code here
    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Step 5: Statistical Analysis with NumPy

    **Task:** Convert the clean data to NumPy arrays and calculate statistics.

    Calculate:
    1. Mean, median, std deviation of transaction amounts
    2. 25th, 50th, 75th percentiles
    3. Number of transactions above median
    """
    )
    return


@app.cell
def _(np):
    # Convert amounts to NumPy array
    # amounts_array_user = np.array([t["amount"] for t in clean_data_user])

    # Your statistical analysis here
    pass
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---

    # Wrap-up & Reflection

    ## What We Accomplished Today

    ✅ **Session 1:** Python fundamentals
    - Variables, operators, control flow, functions

    ✅ **Session 2:** Data structures and NumPy
    - Lists, dicts, tuples, sets
    - NumPy arrays and statistics
    - File operations

    ✅ **Practical Session:** Real-world data analysis
    - Data cleaning
    - Statistical analysis
    - Answering business questions

    ## Key Takeaways

    1. **Python basics** are the foundation for everything
    2. **Data structures** help organize information
    3. **NumPy** makes numerical work efficient
    4. **Real data is messy** - cleaning is essential
    5. **Code + business questions** = valuable insights
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Questions & Discussion

    - What was challenging today?
    - What concepts need more practice?
    - Any questions about today's material?

    ---

    **Optional Practice:**
    - Review today's notebooks
    - Try modifying the mini-project with your own questions
    - Experiment with the exercises
    """
    )
    return


if __name__ == "__main__":
    app.run()
