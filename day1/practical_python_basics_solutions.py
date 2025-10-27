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
    - Each exercise has a solution cell below (hidden initially)
    - Work at your own pace
    - Ask questions anytime!
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

    <!-- Image placeholder: "Warm up those coding fingers!" -->
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
def _(mo):
    mo.md(r"""### ✏️ Your Solution:""")
    return


@app.cell
def _():
    # Write your solution here
    def celsius_to_fahrenheit_exercise(celsius):
        # Your code here
        pass

    # Test your function
    # print(celsius_to_fahrenheit_exercise(0))
    # print(celsius_to_fahrenheit_exercise(100))
    # print(celsius_to_fahrenheit_exercise(37))
    return


@app.cell
def _(mo):
    mo.md(r"""### ✅ Solution:""")
    return


@app.cell
def _():
    def celsius_to_fahrenheit_solution(celsius):
        """Convert Celsius to Fahrenheit."""
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    print("Temperature conversions:")
    print(f"0°C = {celsius_to_fahrenheit_solution(0):.1f}°F")
    print(f"100°C = {celsius_to_fahrenheit_solution(100):.1f}°F")
    print(f"37°C = {celsius_to_fahrenheit_solution(37):.1f}°F")
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
def _(mo):
    mo.md(r"""### ✏️ Your Solution:""")
    return


@app.cell
def _():
    # Write your solution here
    def get_grade_exercise(score):
        # Your code here
        pass

    # Test cases
    # print(get_grade_exercise(95))
    # print(get_grade_exercise(85))
    # print(get_grade_exercise(72))
    # print(get_grade_exercise(65))
    # print(get_grade_exercise(45))
    return


@app.cell
def _(mo):
    mo.md(r"""### ✅ Solution:""")
    return


@app.cell
def _():
    def get_grade_solution(score):
        """Return letter grade for a numeric score."""
        if score < 0 or score > 100:
            return "Invalid score"
        elif score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    print("Grade examples:")
    test_scores_solution = [95, 85, 72, 65, 45, 105, -10]
    for score in test_scores_solution:
        grade = get_grade_solution(score)
        print(f"Score {score}: Grade {grade}")
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
def _(mo):
    mo.md(r"""### ✏️ Your Solution:""")
    return


@app.cell
def _():
    # Write your solution here
    def sum_even_numbers_exercise(numbers):
        # Your code here
        pass

    # Test
    # numbers_exercise = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(sum_even_numbers_exercise(numbers_exercise))
    return


@app.cell
def _(mo):
    mo.md(r"""### ✅ Solution:""")
    return


@app.cell
def _():
    def sum_even_numbers_solution(numbers):
        """Sum all even numbers in a list."""
        even_total = 0
        for num in numbers:
            if num % 2 == 0:  # Check if even
                even_total += num
        return even_total

    # Alternative solution using list comprehension
    def sum_even_numbers_alternative(numbers):
        return sum([num for num in numbers if num % 2 == 0])

    # Test both solutions
    test_numbers_even = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Numbers: {test_numbers_even}")
    print(f"Sum of even numbers: {sum_even_numbers_solution(test_numbers_even)}")
    print(f"Alternative solution: {sum_even_numbers_alternative(test_numbers_even)}")
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
def _(mo):
    mo.md(r"""### ✏️ Your Solution:""")
    return


@app.cell
def _():
    # Write your solution here
    cart_exercise = {}

    def add_to_cart_exercise(cart, product, quantity):
        # Your code here
        pass

    def get_total_items_exercise(cart):
        # Your code here
        pass

    def remove_from_cart_exercise(cart, product):
        # Your code here
        pass

    # Test your functions
    # add_to_cart_exercise(cart_exercise, "apple", 3)
    # add_to_cart_exercise(cart_exercise, "banana", 2)
    # print(cart_exercise)
    return


@app.cell
def _(mo):
    mo.md(r"""### ✅ Solution:""")
    return


@app.cell
def _():
    def add_to_cart_solution(cart, product, quantity):
        """Add item to cart or update quantity."""
        if product in cart:
            cart[product] += quantity
        else:
            cart[product] = quantity
        print(f"Added {quantity} {product}(s). Cart now has {cart[product]} {product}(s).")

    def get_total_items_solution(cart):
        """Get total number of items in cart."""
        return sum(cart.values())

    def remove_from_cart_solution(cart, product):
        """Remove item from cart."""
        if product in cart:
            removed_qty = cart.pop(product)
            print(f"Removed {removed_qty} {product}(s) from cart.")
        else:
            print(f"{product} not in cart.")

    # Test the shopping cart
    shopping_cart = {}

    print("=== Shopping Cart Demo ===\n")
    add_to_cart_solution(shopping_cart, "apple", 3)
    add_to_cart_solution(shopping_cart, "banana", 2)
    add_to_cart_solution(shopping_cart, "apple", 2)
    add_to_cart_solution(shopping_cart, "orange", 5)

    print(f"\nCurrent cart: {shopping_cart}")
    print(f"Total items: {get_total_items_solution(shopping_cart)}")

    print("\nRemoving banana...")
    remove_from_cart_solution(shopping_cart, "banana")
    print(f"Cart after removal: {shopping_cart}")
    print(f"Total items: {get_total_items_solution(shopping_cart)}")
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
def _(mo):
    mo.md(r"""### ✏️ Your Solution:""")
    return


@app.cell
def _():
    students_exercise = [
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
    mo.md(r"""### ✅ Solution:""")
    return


@app.cell
def _():
    students_solution = [
        {"name": "Alice", "age": 20, "grades": [85, 90, 88]},
        {"name": "Bob", "age": 21, "grades": [78, 82, 80]},
        {"name": "Carol", "age": 19, "grades": [92, 95, 93]},
        {"name": "David", "age": 20, "grades": [70, 75, 72]}
    ]

    print("=== Student Records Analysis ===\n")

    # Task 1: Calculate averages
    print("1. Student Averages:")
    for student in students_solution:
        avg = sum(student["grades"]) / len(student["grades"])
        student["average"] = avg  # Add to dictionary
        print(f"   {student['name']}: {avg:.2f}")

    # Task 2: Find highest average
    top_student = max(students_solution, key=lambda s: s["average"])
    print(f"\n2. Top Student: {top_student['name']} with average {top_student['average']:.2f}")

    # Task 3: Count high achievers
    high_achievers = [s for s in students_solution if s["average"] > 85]
    print(f"\n3. Students with average > 85: {len(high_achievers)}")
    for student in high_achievers:
        print(f"   - {student['name']}: {student['average']:.2f}")
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
def _(mo):
    mo.md(r"""### ✏️ Your Solution:""")
    return


@app.cell
def _():
    # Write your solution here
    def count_words_exercise(sentence):
        # Your code here
        pass

    # Test
    # text_exercise = "The quick brown fox jumps over the lazy dog the fox"
    # print(count_words_exercise(text_exercise))
    return


@app.cell
def _(mo):
    mo.md(r"""### ✅ Solution:""")
    return


@app.cell
def _():
    def count_words_solution(sentence):
        """Count word frequency in a sentence."""
        # Convert to lowercase and split into words
        words = sentence.lower().split()

        # Count occurrences
        word_count = {}
        for word in words:
            # Remove basic punctuation
            word = word.strip(".,!?;:")
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        return word_count

    # Test
    sample_text = "The quick brown fox jumps over the lazy dog the fox"
    print(f"Text: {sample_text}")
    print(f"\nWord frequency:")

    word_counts = count_words_solution(sample_text)
    for word, count in sorted(word_counts.items()):
        print(f"  '{word}': {count}")

    # Find most common word
    most_common = max(word_counts.items(), key=lambda x: x[1])
    print(f"\nMost common word: '{most_common[0]}' appears {most_common[1]} times")
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
def _(mo):
    mo.md(r"""### ✏️ Your Solution:""")
    return


@app.cell
def _():
    import numpy as np

    # Daily sales for 4 weeks
    daily_sales_exercise = np.array([
        1200, 1450, 1100, 1800, 2100, 950, 1350,   # Week 1
        1500, 1600, 1400, 1900, 2200, 1050, 1400,  # Week 2
        1300, 1550, 1200, 1750, 2000, 1000, 1300,  # Week 3
        1400, 1500, 1350, 1850, 2150, 1100, 1450   # Week 4
    ])

    # Write your solution here
    # Hint: Use reshape to organize by weeks
    # sales_by_week_exercise = daily_sales_exercise.reshape(4, 7)
    return (np,)


@app.cell
def _(mo):
    mo.md(r"""### ✅ Solution:""")
    return


@app.cell
def _(np):
    # Daily sales for 4 weeks
    daily_sales_solution = np.array([
        1200, 1450, 1100, 1800, 2100, 950, 1350,   # Week 1
        1500, 1600, 1400, 1900, 2200, 1050, 1400,  # Week 2
        1300, 1550, 1200, 1750, 2000, 1000, 1300,  # Week 3
        1400, 1500, 1350, 1850, 2150, 1100, 1450   # Week 4
    ])

    print("=== Sales Performance Analysis ===\n")

    # Reshape to weeks (4 weeks × 7 days)
    sales_by_week_solution = daily_sales_solution.reshape(4, 7)

    # Task 1: Weekly totals
    weekly_totals_solution = sales_by_week_solution.sum(axis=1)  # Sum along columns (days)
    print("1. Weekly Totals:")
    for week_num, total in enumerate(weekly_totals_solution, 1):
        print(f"   Week {week_num}: ${total:,}")

    # Task 2: Best and worst week
    best_week_solution = np.argmax(weekly_totals_solution) + 1
    worst_week_solution = np.argmin(weekly_totals_solution) + 1
    print(f"\n2. Best week: Week {best_week_solution} (${weekly_totals_solution[best_week_solution-1]:,})")
    print(f"   Worst week: Week {worst_week_solution} (${weekly_totals_solution[worst_week_solution-1]:,})")

    # Task 3: Daily average
    daily_average_solution = daily_sales_solution.mean()
    print(f"\n3. Daily average: ${daily_average_solution:.2f}")

    # Task 4: Days exceeding average
    above_average_solution = daily_sales_solution > daily_average_solution
    num_above_solution = above_average_solution.sum()
    print(f"\n4. Days exceeding average: {num_above_solution} out of {len(daily_sales_solution)}")
    return


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
def _(mo):
    mo.md(r"""### ✏️ Your Solution:""")
    return


@app.cell
def _(np):
    # Daily temperatures (Celsius)
    temperatures_exercise = np.array([
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
    mo.md(r"""### ✅ Solution:""")
    return


@app.cell
def _(np):
    temperatures_solution = np.array([
        22, 24, 23, 25, 26, 24, 23,
        25, 27, 28, 29, 30, 28, 26,
        24, 23, 22, 21, 20, 19, 18,
        20, 22, 35, 23, 24, 25, 26,
        27, 5
    ])

    print("=== Temperature Analysis ===\n")

    # Task 1: Basic statistics
    mean_temp_solution = temperatures_solution.mean()
    min_temp_solution = temperatures_solution.min()
    max_temp_solution = temperatures_solution.max()

    print(f"1. Temperature Statistics:")
    print(f"   Average: {mean_temp_solution:.2f}°C")
    print(f"   Minimum: {min_temp_solution}°C")
    print(f"   Maximum: {max_temp_solution}°C")

    # Task 2: Standard deviation
    std_temp_solution = temperatures_solution.std()
    print(f"\n2. Standard Deviation: {std_temp_solution:.2f}°C")

    # Task 3: Find extreme temperatures
    lower_bound_solution = mean_temp_solution - 2 * std_temp_solution
    upper_bound_solution = mean_temp_solution + 2 * std_temp_solution

    print(f"\n3. Normal range: {lower_bound_solution:.2f}°C to {upper_bound_solution:.2f}°C")

    extreme_days_solution = np.where((temperatures_solution < lower_bound_solution) |
                            (temperatures_solution > upper_bound_solution))[0]

    print(f"\n   Extreme temperature days:")
    for day in extreme_days_solution:
        print(f"   Day {day + 1}: {temperatures_solution[day]}°C")
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

    <!-- Image placeholder: "Time to become a data analyst!" -->
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
    transaction_ids_mini = list(range(1, 101))
    products_mini = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
    categories_mini = ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics"]

    # Random product selection
    product_choices_mini = [products_mini[i] for i in np.random.randint(0, 5, 100)]

    # Sales amounts with some variation
    base_prices_mini = {"Laptop": 999, "Mouse": 25, "Keyboard": 75, "Monitor": 350, "Headphones": 150}
    amounts_mini = [base_prices_mini[p] * np.random.uniform(0.8, 1.2) for p in product_choices_mini]

    # Quantities
    quantities_mini = np.random.randint(1, 5, 100)

    # Add some "bad" data intentionally
    amounts_mini[10] = -50  # Negative value (error)
    amounts_mini[25] = 0    # Zero value (cancelled?)
    amounts_mini[50] = None # Missing value

    # Create the dataset as a list of dictionaries
    sales_data_mini = []
    for i in range(100):
        sales_data_mini.append({
            "transaction_id": transaction_ids_mini[i],
            "product": product_choices_mini[i],
            "quantity": int(quantities_mini[i]),
            "amount": amounts_mini[i]
        })

    print(f"✓ Created dataset with {len(sales_data_mini)} transactions")
    print(f"\nFirst 3 transactions:")
    for i in range(3):
        print(f"  {sales_data_mini[i]}")
    return (sales_data_mini,)


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
def _(mo):
    mo.md(r"""### ✏️ Your Solution:""")
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
    mo.md(r"""### ✅ Solution:""")
    return


@app.cell
def _(sales_data_mini):
    print("=== Data Inspection ===\n")

    # Basic info
    print(f"Total transactions: {len(sales_data_mini)}")

    # Unique products
    unique_products_inspect = set([t["product"] for t in sales_data_mini])
    print(f"Unique products: {unique_products_inspect}")

    # Sample transaction
    print(f"\nSample transaction:")
    print(sales_data_mini[0])

    # Check for data issues
    print(f"\n=== Data Quality Check ===")

    # Count None/null values
    none_count_inspect = sum([1 for t in sales_data_mini if t["amount"] is None])
    print(f"Transactions with missing amounts: {none_count_inspect}")

    # Count negative or zero amounts
    invalid_count_inspect = sum([1 for t in sales_data_mini
                         if t["amount"] is not None and t["amount"] <= 0])
    print(f"Transactions with invalid amounts: {invalid_count_inspect}")
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
def _(mo):
    mo.md(r"""### ✏️ Your Solution:""")
    return


@app.cell
def _():
    # Clean the data here
    clean_sales_data_exercise = []

    # Your code here
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""### ✅ Solution:""")
    return


@app.cell
def _(sales_data_mini):
    print("=== Data Cleaning ===\n")

    # Clean the data
    clean_data_solution = []
    removed_count_clean = 0

    for transaction in sales_data_mini:
        # Check if amount is valid
        if transaction["amount"] is not None and transaction["amount"] > 0:
            clean_data_solution.append(transaction)
        else:
            removed_count_clean += 1

    print(f"Original transactions: {len(sales_data_mini)}")
    print(f"Removed: {removed_count_clean}")
    print(f"Clean transactions: {len(clean_data_solution)}")
    print(f"\nData cleaning complete! ✓")
    return (clean_data_solution,)


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
def _(mo):
    mo.md(r"""### ✏️ Your Solution:""")
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
    mo.md(r"""### ✅ Solution:""")
    return


@app.cell
def _(clean_data_solution):
    print("=== Business Questions Analysis ===\n")

    # Q1: Total revenue
    total_revenue_analysis = sum([t["amount"] for t in clean_data_solution])
    print(f"Q1. Total Revenue: ${total_revenue_analysis:,.2f}")

    # Q2: Average transaction value
    avg_transaction_analysis = total_revenue_analysis / len(clean_data_solution)
    print(f"Q2. Average Transaction: ${avg_transaction_analysis:.2f}")

    # Q3: Revenue by product
    print(f"\nQ3. Revenue by Product:")
    product_revenue_analysis = {}
    for t in clean_data_solution:
        product = t["product"]
        if product in product_revenue_analysis:
            product_revenue_analysis[product] += t["amount"]
        else:
            product_revenue_analysis[product] = t["amount"]

    # Sort by revenue (highest first)
    sorted_products_analysis = sorted(product_revenue_analysis.items(), key=lambda x: x[1], reverse=True)
    for product, revenue in sorted_products_analysis:
        print(f"   {product}: ${revenue:,.2f}")

    print(f"\n   → Top product: {sorted_products_analysis[0][0]} (${sorted_products_analysis[0][1]:,.2f})")

    # Q4: Units sold by product
    print(f"\nQ4. Units Sold by Product:")
    product_units_analysis = {}
    for t in clean_data_solution:
        product = t["product"]
        if product in product_units_analysis:
            product_units_analysis[product] += t["quantity"]
        else:
            product_units_analysis[product] = t["quantity"]

    for product, units in sorted(product_units_analysis.items()):
        print(f"   {product}: {units} units")

    # Q5: Top 3 transactions
    print(f"\nQ5. Top 3 Transactions:")
    sorted_transactions_analysis = sorted(clean_data_solution, key=lambda x: x["amount"], reverse=True)
    for i, t in enumerate(sorted_transactions_analysis[:3], 1):
        print(f"   #{i}: {t['product']} - ${t['amount']:.2f} (ID: {t['transaction_id']})")
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
def _(mo):
    mo.md(r"""### ✏️ Your Solution:""")
    return


@app.cell
def _(clean_data_solution, np):
    # Convert amounts to NumPy array
    amounts_array_exercise = np.array([t["amount"] for t in clean_data_solution])

    # Your statistical analysis here
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""### ✅ Solution:""")
    return


@app.cell
def _(clean_data_solution, np):
    print("=== Statistical Analysis ===\n")

    # Convert to NumPy array
    amounts_np_stats = np.array([t["amount"] for t in clean_data_solution])

    # Basic statistics
    print("Transaction Amount Statistics:")
    print(f"  Mean: ${np.mean(amounts_np_stats):.2f}")
    print(f"  Median: ${np.median(amounts_np_stats):.2f}")
    print(f"  Std Dev: ${np.std(amounts_np_stats):.2f}")
    print(f"  Min: ${np.min(amounts_np_stats):.2f}")
    print(f"  Max: ${np.max(amounts_np_stats):.2f}")

    # Percentiles
    p25_stats = np.percentile(amounts_np_stats, 25)
    p50_stats = np.percentile(amounts_np_stats, 50)
    p75_stats = np.percentile(amounts_np_stats, 75)

    print(f"\nPercentiles:")
    print(f"  25th: ${p25_stats:.2f}")
    print(f"  50th (median): ${p50_stats:.2f}")
    print(f"  75th: ${p75_stats:.2f}")

    # Transactions above median
    above_median_stats = amounts_np_stats > p50_stats
    num_above_median_stats = above_median_stats.sum()
    print(f"\nTransactions above median: {num_above_median_stats} ({num_above_median_stats/len(amounts_np_stats)*100:.1f}%)")

    # High value transactions (top 10%)
    p90_stats = np.percentile(amounts_np_stats, 90)
    high_value_stats = amounts_np_stats > p90_stats
    print(f"High-value transactions (top 10%): {high_value_stats.sum()}")
    print(f"  Threshold: ${p90_stats:.2f}")
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
    - File operations, basic classes

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
