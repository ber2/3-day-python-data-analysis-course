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
    # Session 1 Reference: Python Basics

    This notebook contains all the code examples from Session 1.
    Use it as a reference if you fall behind during live coding.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 1: Variables and Data Types""")
    return


@app.cell
def _():
    # Our first Python code!
    print("Hello, Data Analysts!")
    return


@app.cell
def _():
    # Creating variables
    sales_amount = 1500
    product_name = "Laptop"
    is_in_stock = True
    discount_rate = 0.15

    print(f"Product: {product_name}")
    print(f"Sales: ${sales_amount}")
    print(f"In stock: {is_in_stock}")
    print(f"Discount: {discount_rate * 100}%")
    return


@app.cell
def _():
    # Checking data types
    revenue = 50000
    growth_rate = 0.23
    company_name = "DataCorp"
    profitable = True

    print(f"revenue is type: {type(revenue)}")
    print(f"growth_rate is type: {type(growth_rate)}")
    print(f"company_name is type: {type(company_name)}")
    print(f"profitable is type: {type(profitable)}")
    return


@app.cell
def _():
    # Calculate total price after discount
    base_price = 100
    discount = 0.20  # 20% discount for early customers

    """
    This is a multi-line comment.
    We can write longer explanations here.
    """

    final_price = base_price * (1 - discount)
    print(f"Final price: ${final_price}")
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 2: Operators and Expressions""")
    return


@app.cell
def _():
    # Arithmetic operators: calculating business metrics
    total_sales = 45000
    num_transactions = 150

    average_transaction = total_sales / num_transactions
    print(f"Average transaction value: ${average_transaction:.2f}")

    # Growth calculation
    previous_sales = 40000
    growth = ((total_sales - previous_sales) / previous_sales) * 100
    print(f"Sales growth: {growth:.1f}%")
    return


@app.cell
def _():
    # Comparison operators
    target_revenue = 50000
    actual_revenue = 48000

    met_target = actual_revenue >= target_revenue
    print(f"Met revenue target: {met_target}")

    customer_age = 25
    is_adult = customer_age >= 18
    print(f"Customer is adult: {is_adult}")
    return


@app.cell
def _():
    # Logical operators: customer segmentation
    age = 28
    premium_member = True
    purchase_amount = 150

    # Complex condition
    eligible_for_bonus = (age >= 18) and (premium_member or purchase_amount > 100)
    print(f"Eligible for bonus: {eligible_for_bonus}")

    # Using not
    is_minor = not (age >= 18)
    print(f"Is minor: {is_minor}")
    return


@app.cell
def _():
    # String operations
    first_name = "Alice"
    last_name = "Johnson"

    # Concatenation
    full_name = first_name + " " + last_name
    print(f"Full name: {full_name}")

    # Repetition
    separator = "-" * 20
    print(separator)

    # String formatting (f-strings)
    customer_id = 12345
    message = f"Welcome, {full_name}! Your ID is {customer_id}"
    print(message)

    # Useful string methods
    print(f"Uppercase: {full_name.upper()}")
    print(f"Lowercase: {full_name.lower()}")
    print(f"Length: {len(full_name)} characters")
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 3: Control Flow""")
    return


@app.cell
def _():
    # If/else: Sales performance evaluation
    monthly_sales = 75000

    if monthly_sales >= 100000:
        performance = "Excellent"
        bonus = monthly_sales * 0.10
    elif monthly_sales >= 75000:
        performance = "Good"
        bonus = monthly_sales * 0.05
    elif monthly_sales >= 50000:
        performance = "Fair"
        bonus = monthly_sales * 0.02
    else:
        performance = "Needs Improvement"
        bonus = 0

    print(f"Performance: {performance}")
    print(f"Bonus: ${bonus:,.2f}")
    return


@app.cell
def _():
    # For loop: iterating over a range
    print("Daily sales totals:")
    for day in range(1, 8):  # Days 1 through 7
        print(f"  Day {day}: $X,XXX")
    return


@app.cell
def _():
    # For loop: processing a list of values
    daily_sales = [1200, 1450, 1100, 1800, 2100, 950, 1350]

    total = 0
    for sale in daily_sales:
        total += sale  # Same as: total = total + sale

    average = total / len(daily_sales)
    print(f"Total weekly sales: ${total:,.2f}")
    print(f"Average daily sales: ${average:,.2f}")
    return


@app.cell
def _():
    # For loop with conditions: applying discounts
    purchases = [45.99, 120.50, 89.99, 200.00, 15.75]

    # Apply discount to purchases over $100
    discounted_purchases = []

    for purchase in purchases:
        if purchase > 100:
            discounted_price = purchase * 0.90  # 10% discount
            discounted_purchases.append(discounted_price)
            print(f"${purchase:.2f} → ${discounted_price:.2f} (10% off)")
        else:
            discounted_purchases.append(purchase)
            print(f"${purchase:.2f} (no discount)")

    print(f"\nOriginal total: ${sum(purchases):.2f}")
    print(f"Discounted total: ${sum(discounted_purchases):.2f}")
    return


@app.cell
def _():
    # While loop: compound interest calculation
    initial_investment = 10000
    target_amount = 15000
    annual_rate = 0.07

    current_amount = initial_investment
    years = 0

    while current_amount < target_amount:
        current_amount = current_amount * (1 + annual_rate)
        years += 1
        print(f"Year {years}: ${current_amount:,.2f}")

    print(f"\nReached target in {years} years!")
    return


@app.cell
def _():
    # Break: find first high-value transaction
    transactions = [45, 120, 67, 89, 500, 234, 156]
    threshold = 400

    print(f"Looking for transaction over ${threshold}...")
    for i, transaction in enumerate(transactions, 1):
        if transaction > threshold:
            print(f"Found at position {i}: ${transaction}")
            break
        print(f"  Transaction {i}: ${transaction} (not high enough)")
    return


@app.cell
def _():
    # Continue: process only valid entries
    data_entries = [100, -50, 200, 0, 150, -20, 300]

    print("Processing valid (positive) entries only:")
    valid_sum = 0

    for entry in data_entries:
        if entry <= 0:
            print(f"  Skipping invalid entry: {entry}")
            continue

        valid_sum += entry
        print(f"  Added: {entry}")

    print(f"\nSum of valid entries: {valid_sum}")
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 4: Functions""")
    return


@app.cell
def _():
    # Simple function with no parameters
    def greet():
        return "Hello, Data Analyst!"

    message = greet()
    print(message)
    return


@app.cell
def _():
    # Function with parameters
    def calculate_discount(price, discount_rate):
        """Calculate the discounted price."""
        discount_amount = price * discount_rate
        final_price = price - discount_amount
        return final_price

    # Using the function
    original = 100
    result = calculate_discount(original, 0.20)
    print(f"Original: ${original}")
    print(f"After 20% discount: ${result}")

    # Call with different values
    result2 = calculate_discount(250, 0.15)
    print(f"\nOriginal: $250")
    print(f"After 15% discount: ${result2}")
    return


@app.cell
def _():
    # Function returning multiple values
    def calculate_metrics(sales_list):
        """Calculate total, average, and maximum from a list of sales."""
        total_sales = sum(sales_list)
        avg_sales = total_sales / len(sales_list)
        max_sales = max(sales_list)

        # Return multiple values as a tuple
        return total_sales, avg_sales, max_sales

    # Using the function
    weekly_sales = [1200, 1450, 1100, 1800, 2100, 950, 1350]
    total, average, maximum = calculate_metrics(weekly_sales)

    print(f"Total: ${total:,.2f}")
    print(f"Average: ${average:,.2f}")
    print(f"Maximum: ${maximum:,.2f}")
    return


@app.cell
def _():
    # Function with default parameters
    def apply_tax(amount, tax_rate=0.08):
        """Apply tax to an amount. Default tax rate is 8%."""
        return amount * (1 + tax_rate)

    # Use default tax rate
    price1 = apply_tax(100)
    print(f"With default tax (8%): ${price1:.2f}")

    # Override with custom tax rate
    price2 = apply_tax(100, 0.10)
    print(f"With custom tax (10%): ${price2:.2f}")
    return


@app.cell
def _():
    # Variable scope example
    # Global variable
    company_name = "DataCorp"

    def generate_report(revenue):
        # Local variable
        report_title = f"{company_name} Revenue Report"
        summary = f"{report_title}: ${revenue:,.2f}"
        return summary

    report = generate_report(50000)
    print(report)

    # This would cause an error (report_title is not accessible here):
    # print(report_title)
    return


@app.cell
def _():
    # Complete example: data validation function
    def validate_and_clean_sales(sales_data):
        """
        Validate and clean a list of sales values.

        - Remove negative values (data errors)
        - Remove zeros (cancelled transactions)
        - Return cleaned list and count of removed items
        """
        cleaned_data = []
        removed_count = 0

        for value in sales_data:
            if value > 0:
                cleaned_data.append(value)
            else:
                removed_count += 1

        return cleaned_data, removed_count

    # Test the function
    raw_data = [100, 250, -50, 0, 180, 320, 0, -10, 290]
    clean_data, errors = validate_and_clean_sales(raw_data)

    print(f"Original data: {raw_data}")
    print(f"Cleaned data: {clean_data}")
    print(f"Removed {errors} invalid entries")
    print(f"Clean total: ${sum(clean_data):,.2f}")
    return


if __name__ == "__main__":
    app.run()
