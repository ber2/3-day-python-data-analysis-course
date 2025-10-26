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
    # Session 2 Reference: Data Structures and Numerical Computing

    This notebook contains all the code examples from Session 2.
    Use it as a reference if you fall behind during live coding.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 1: Core Data Structures""")
    return


@app.cell
def _():
    # Creating lists
    sales = [1200, 1450, 1100, 1800, 2100]
    products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
    mixed = [100, "Product", True, 3.14]

    print(f"Sales: {sales}")
    print(f"Products: {products}")
    print(f"Mixed types: {mixed}")

    # Accessing elements
    print(f"\nFirst sale: ${sales[0]}")
    print(f"Last product: {products[-1]}")  # Negative indexing
    print(f"First three sales: {sales[0:3]}")  # Slicing
    return


@app.cell
def _():
    # List methods
    daily_sales = [1200, 1450, 1100]

    # Add new sales
    daily_sales.append(1800)
    print(f"After append: {daily_sales}")

    # Insert at specific position
    daily_sales.insert(0, 1000)
    print(f"After insert: {daily_sales}")

    # Remove a value
    daily_sales.remove(1100)
    print(f"After remove: {daily_sales}")

    # Sort the list
    daily_sales.sort()
    print(f"After sort: {daily_sales}")

    # Get list statistics
    print(f"\nTotal sales: ${sum(daily_sales):,}")
    print(f"Number of days: {len(daily_sales)}")
    print(f"Average: ${sum(daily_sales) / len(daily_sales):.2f}")
    return


@app.cell
def _():
    # Creating tuples
    coordinates = (40.7128, -74.0060)  # NYC coordinates
    rgb_color = (255, 128, 0)
    single_item = (42,)  # Note the comma!

    print(f"Coordinates: {coordinates}")
    print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")

    # Unpacking tuples
    lat, lon = coordinates
    print(f"\nUnpacked - Lat: {lat}, Lon: {lon}")

    # Tuples are immutable - this would raise an error:
    # coordinates[0] = 50  # TypeError!

    # But you can create a new tuple
    new_coordinates = (50.0, coordinates[1])
    print(f"New coordinates: {new_coordinates}")

    # Common use: multiple return values
    def get_stats(numbers):
        return min(numbers), max(numbers), sum(numbers) / len(numbers)

    minimum, maximum, average = get_stats([1, 2, 3, 4, 5])
    print(f"\nStats - Min: {minimum}, Max: {maximum}, Avg: {average}")
    return


@app.cell
def _():
    # Creating dictionaries - representing a customer
    customer_dict = {
        "id": 12345,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "purchases": 15,
        "total_spent": 2450.00
    }

    print("Customer information:")
    print(f"Name: {customer_dict['name']}")
    print(f"Email: {customer_dict['email']}")
    print(f"Total spent: ${customer_dict['total_spent']:.2f}")

    # Adding new key-value pairs
    customer_dict["vip_status"] = True
    print(f"\nVIP Status: {customer_dict['vip_status']}")

    # Updating values
    customer_dict["purchases"] += 1
    customer_dict["total_spent"] += 150.00
    print(f"Updated purchases: {customer_dict['purchases']}")
    print(f"Updated total: ${customer_dict['total_spent']:.2f}")
    return


@app.cell
def _():
    # Dictionary methods and iteration
    inventory_dict = {
        "laptop": 45,
        "mouse": 120,
        "keyboard": 78,
        "monitor": 32
    }

    # Iterating over keys
    print("Products in stock:")
    for product in inventory_dict.keys():
        print(f"  - {product}")

    # Iterating over values
    print(f"\nTotal items: {sum(inventory_dict.values())}")

    # Iterating over key-value pairs
    print("\nFull inventory:")
    for product, quantity in inventory_dict.items():
        print(f"  {product.capitalize()}: {quantity} units")

    # Safe access with .get()
    tablets = inventory_dict.get("tablet", 0)
    print(f"\nTablets in stock: {tablets}")

    # Practical: find low stock items
    print("\nLow stock alerts (< 50 units):")
    for product, quantity in inventory_dict.items():
        if quantity < 50:
            print(f"  ⚠️  {product}: only {quantity} left!")
    return


@app.cell
def _():
    # Creating sets - automatically removes duplicates
    customer_ids_set = {101, 102, 103, 102, 101, 104}
    print(f"Unique customers: {customer_ids_set}")
    print(f"Count: {len(customer_ids_set)}")

    # Fast membership testing
    print(f"\nIs customer 102 active? {102 in customer_ids_set}")
    print(f"Is customer 999 active? {999 in customer_ids_set}")

    # Set operations
    weekday_customers = {101, 102, 103, 105}
    weekend_customers = {103, 104, 106, 107}

    # Union - all customers
    all_customers = weekday_customers | weekend_customers
    print(f"\nAll customers: {all_customers}")

    # Intersection - customers who shop both weekday and weekend
    frequent = weekday_customers & weekend_customers
    print(f"Frequent shoppers (both): {frequent}")

    # Difference - only weekday shoppers
    weekday_only = weekday_customers - weekend_customers
    print(f"Weekday only: {weekday_only}")

    # Practical: remove duplicates from a list
    transaction_list = [101, 102, 101, 103, 102, 101, 104]
    unique_customers_from_transactions = set(transaction_list)
    print(f"\nTransactions: {transaction_list}")
    print(f"Unique customers: {len(unique_customers_from_transactions)}")
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 2: NumPy Arrays""")
    return


@app.cell
def _():
    # Import NumPy (standard alias is 'np')
    import numpy as np

    print(f"NumPy version: {np.__version__}")
    return (np,)


@app.cell
def _(np):
    # Create array from a list
    sales_list = [1200, 1450, 1100, 1800, 2100, 950, 1350]
    sales_array = np.array(sales_list)
    print(f"Sales array: {sales_array}")
    print(f"Type: {type(sales_array)}")
    print(f"Data type: {sales_array.dtype}")

    # Create arrays with NumPy functions
    zeros = np.zeros(5)
    ones = np.ones(5)
    sequence = np.arange(1, 8)  # Like range(), but returns array

    print(f"\nZeros: {zeros}")
    print(f"Ones: {ones}")
    print(f"Sequence: {sequence}")

    # 2D array (matrix)
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\nMatrix:\n{matrix}")
    print(f"Shape: {matrix.shape}")
    return


@app.cell
def _(np):
    # Arithmetic operations - vectorized!
    daily_sales = np.array([1200, 1450, 1100, 1800, 2100])

    # Apply 10% discount to all sales (vectorized!)
    discounted_sales = daily_sales * 0.9
    print(f"Original: {daily_sales}")
    print(f"After 10% discount: {discounted_sales}")

    # Add a bonus to all sales
    with_bonus = daily_sales + 100
    print(f"With $100 bonus: {with_bonus}")

    # Element-wise operations
    prices = np.array([10, 20, 30, 40, 50])
    quantities = np.array([5, 3, 8, 2, 6])
    revenues = prices * quantities
    print(f"\nPrices: {prices}")
    print(f"Quantities: {quantities}")
    print(f"Revenues: {revenues}")

    # Compare with Python lists (would need a loop!)
    # for i in range(len(prices)):
    #     revenues[i] = prices[i] * quantities[i]
    return


@app.cell
def _(np):
    # Statistical analysis with NumPy
    weekly_sales = np.array([1200, 1450, 1100, 1800, 2100, 950, 1350])

    print("Weekly Sales Analysis")
    print("=" * 40)
    print(f"Total revenue: ${np.sum(weekly_sales):,.2f}")
    print(f"Average daily sales: ${np.mean(weekly_sales):,.2f}")
    print(f"Median: ${np.median(weekly_sales):,.2f}")
    print(f"Std deviation: ${np.std(weekly_sales):,.2f}")
    print(f"Minimum: ${np.min(weekly_sales):,.2f}")
    print(f"Maximum: ${np.max(weekly_sales):,.2f}")
    print(f"Range: ${np.max(weekly_sales) - np.min(weekly_sales):,.2f}")

    # Find indices
    best_day = np.argmax(weekly_sales)
    worst_day = np.argmin(weekly_sales)
    print(f"\nBest day: Day {best_day + 1} (${weekly_sales[best_day]})")
    print(f"Worst day: Day {worst_day + 1} (${weekly_sales[worst_day]})")
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 3: Working with Files""")
    return


@app.cell
def _():
    # Writing to a text file
    sales_report = """Daily Sales Report
    ==================
    Day 1: $1,200
    Day 2: $1,450
    Day 3: $1,100
    Day 4: $1,800
    Day 5: $2,100
    """

    with open("sales_report.txt", "w") as file:
        file.write(sales_report)

    print("✓ File written: sales_report.txt")

    # Reading from a file
    with open("sales_report.txt", "r") as file:
        content = file.read()

    print("\nFile contents:")
    print(content)

    # Reading line by line
    print("Reading line by line:")
    with open("sales_report.txt", "r") as file:
        for line_num, line in enumerate(file, 1):
            print(f"  Line {line_num}: {line.strip()}")
    return


@app.cell
def _():
    # Working with CSV files
    import csv

    # Writing CSV
    customers_csv = [
        ["id", "name", "purchases", "total"],
        [101, "Alice Johnson", 15, 2450.00],
        [102, "Bob Smith", 8, 1320.50],
        [103, "Carol White", 22, 3890.00],
        [104, "David Brown", 5, 780.00]
    ]

    with open("customers.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(customers_csv)

    print("✓ CSV file written: customers.csv")

    # Reading CSV
    print("\nReading CSV file:")
    with open("customers.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"  {row}")

    # Reading CSV as dictionaries (more convenient!)
    print("\nReading CSV as dictionaries:")
    with open("customers.csv", "r") as file:
        dict_reader = csv.DictReader(file)
        for row in dict_reader:
            print(f"  Customer {row['id']}: {row['name']} - ${row['total']}")
    return (csv,)


@app.cell
def _():
    # Working with JSON files
    import json

    # Python dictionary
    customer_json_data = {
        "id": 12345,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "purchases": [
            {"date": "2024-01-15", "amount": 150.00, "product": "Laptop"},
            {"date": "2024-02-20", "amount": 50.00, "product": "Mouse"},
            {"date": "2024-03-10", "amount": 85.00, "product": "Keyboard"}
        ],
        "vip": True
    }

    # Writing JSON
    with open("customer.json", "w") as file:
        json.dump(customer_json_data, file, indent=2)

    print("✓ JSON file written: customer.json")

    # Reading JSON
    with open("customer.json", "r") as file:
        loaded_json_data = json.load(file)

    print("\nLoaded customer data:")
    print(f"Name: {loaded_json_data['name']}")
    print(f"Email: {loaded_json_data['email']}")
    print(f"VIP Status: {loaded_json_data['vip']}")
    print(f"\nPurchases:")
    for purchase in loaded_json_data['purchases']:
        print(f"  {purchase['date']}: {purchase['product']} - ${purchase['amount']:.2f}")
    return (json,)


@app.cell
def _(mo):
    mo.md(r"""## Part 4: Introduction to Classes""")
    return


@app.cell
def _():
    # Creating a Product class
    class Product:
        """Represents a product in our inventory."""

        def __init__(self, name, price, quantity):
            """Initialize a new product."""
            self.name = name
            self.price = price
            self.quantity = quantity

        def get_total_value(self):
            """Calculate total inventory value for this product."""
            return self.price * self.quantity

        def sell(self, amount):
            """Sell some quantity of the product."""
            if amount > self.quantity:
                print(f"Error: Only {self.quantity} available!")
                return False
            self.quantity -= amount
            print(f"Sold {amount} {self.name}(s). {self.quantity} remaining.")
            return True

        def restock(self, amount):
            """Add more inventory."""
            self.quantity += amount
            print(f"Restocked {amount} {self.name}(s). Total: {self.quantity}")


    # Creating objects (instances)
    laptop_product = Product("Laptop", 999.99, 50)
    mouse_product = Product("Mouse", 25.99, 200)

    print(f"Product: {laptop_product.name}")
    print(f"Price: ${laptop_product.price}")
    print(f"Quantity: {laptop_product.quantity}")
    print(f"Total value: ${laptop_product.get_total_value():,.2f}")
    return (Product,)


@app.cell
def _(Product):
    # Using class methods
    keyboard_product = Product("Mechanical Keyboard", 89.99, 30)

    # Use methods
    print(f"Initial inventory: {keyboard_product.quantity}")
    print(f"Total value: ${keyboard_product.get_total_value():,.2f}")

    print("\n--- Selling ---")
    keyboard_product.sell(5)

    print("\n--- Restocking ---")
    keyboard_product.restock(10)

    print("\n--- Trying to oversell ---")
    keyboard_product.sell(100)

    print(f"\nFinal inventory: {keyboard_product.quantity}")
    return


@app.cell
def _():
    # Customer class with purchase history
    class Customer:
        """Represents a customer with purchase history."""

        def __init__(self, customer_id, name, email):
            """Initialize a new customer."""
            self.customer_id = customer_id
            self.name = name
            self.email = email
            self.purchases = []
            self.total_spent = 0.0

        def make_purchase(self, amount, product):
            """Record a purchase."""
            self.purchases.append({"product": product, "amount": amount})
            self.total_spent += amount
            print(f"{self.name} purchased {product} for ${amount:.2f}")

        def get_summary(self):
            """Get customer summary."""
            return {
                "id": self.customer_id,
                "name": self.name,
                "email": self.email,
                "num_purchases": len(self.purchases),
                "total_spent": self.total_spent,
                "average_purchase": self.total_spent / len(self.purchases) if self.purchases else 0
            }

        def is_vip(self):
            """Check if customer qualifies as VIP (spent > $1000)."""
            return self.total_spent > 1000


    # Using the Customer class
    alice_customer = Customer(101, "Alice Johnson", "alice@example.com")

    print(f"Customer created: {alice_customer.name}")
    print()

    # Make some purchases
    alice_customer.make_purchase(150.00, "Laptop Case")
    alice_customer.make_purchase(899.99, "Monitor")
    alice_customer.make_purchase(45.50, "USB Cable")

    # Get summary
    print("\n--- Customer Summary ---")
    customer_summary = alice_customer.get_summary()
    for key, value in customer_summary.items():
        print(f"{key}: {value}")

    print(f"\nVIP Status: {alice_customer.is_vip()}")
    return (Customer,)


if __name__ == "__main__":
    app.run()
