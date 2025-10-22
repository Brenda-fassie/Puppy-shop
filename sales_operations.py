"""
Sales Operations Module
Handles all sales-related functionality including recording and searching sales.
"""

import datetime


def enter_sales_record(sales_data, products_data):
    """Handles the process of entering a new sales record."""
    print("\n--- Available Products ---")
    for p in products_data:
        print(f"ID: {p[0]}, Name: {p[1]}, Price: {p[2]}, Stock: {p[3]}")
    print("-------------------------")

    product_id = input("Enter the product ID: ")
    product_to_sell = None
    for p in products_data:
        if p[0] == product_id:
            product_to_sell = p
            break

    if not product_to_sell:
        print("Error: Product ID not found.")
        return

    try:
        quantity = int(input(f"Enter quantity for {product_to_sell[1]}: "))
        if quantity <= 0:
            print("Error: Quantity must be a positive number.")
            return
        
        current_stock = int(product_to_sell[3])
        if quantity > current_stock:
            print(f"Error: Not enough stock. Only {current_stock} available.")
            return

    except ValueError:
        print("Error: Invalid quantity. Please enter a number.")
        return

    # Calculate total payment
    price = float(product_to_sell[2])
    total_payment = price * quantity
    print(f"Total price: {total_payment:.2f}")

    # Update stock
    product_to_sell[3] = str(current_stock - quantity)

    # Record the sale
    now = datetime.datetime.now()
    sale_record = [now.strftime("%d/%m/%Y"), now.strftime("%H:%M:%S"), product_id, str(quantity), f"{total_payment:.2f}"]
    sales_data.append(sale_record)

    print("Sale recorded successfully!")


def search_sales_by_date(sales_data, products_data):
    """Search and display sales records by date."""
    print("\n--- Search Sales by Date ---")
    date_str = input("Enter date (DD/MM/YYYY): ")
    
    print(f"\nSales records for {date_str}:")
    print("-" * 80)
    print(f"{'Date':<12} {'Time':<10} {'Product ID':<12} {'Product Name':<25} {'Quantity':<10} {'Payment':<10}")
    print("-" * 80)
    
    found = False
    for sale in sales_data:
        if sale[0] == date_str:
            # Find product name
            product_name = get_product_name(sale[2], products_data)
            print(f"{sale[0]:<12} {sale[1]:<10} {sale[2]:<12} {product_name:<25} {sale[3]:<10} {sale[4]:<10}")
            found = True
    
    if not found:
        print("No sales records found for this date.")
    print("-" * 80)


def search_sales_by_product_name(sales_data, products_data):
    """Search and display sales records by product name (case-insensitive, partial match)."""
    print("\n--- Search Sales by Product Name ---")
    search_term = input("Enter product name (or part of it): ").lower()
    
    print(f"\nSales records for products matching '{search_term}':")
    print("-" * 80)
    print(f"{'Date':<12} {'Time':<10} {'Product ID':<12} {'Product Name':<25} {'Quantity':<10} {'Payment':<10}")
    print("-" * 80)
    
    found = False
    for sale in sales_data:
        product_name = get_product_name(sale[2], products_data)
        if search_term in product_name.lower():
            print(f"{sale[0]:<12} {sale[1]:<10} {sale[2]:<12} {product_name:<25} {sale[3]:<10} {sale[4]:<10}")
            found = True
    
    if not found:
        print(f"No sales records found for products matching '{search_term}'.")
    print("-" * 80)


def search_sales_by_name_and_date(sales_data, products_data):
    """Search and display sales records by product name and date range."""
    print("\n--- Search Sales by Product Name and Date Range ---")
    search_term = input("Enter product name (or part of it): ").lower()
    start_date_str = input("Enter start date (DD/MM/YYYY): ")
    end_date_str = input("Enter end date (DD/MM/YYYY): ")
    
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y")
        end_date = datetime.datetime.strptime(end_date_str, "%d/%m/%Y")
    except ValueError:
        print("Error: Invalid date format. Please use DD/MM/YYYY.")
        return
    
    print(f"\nSales records for products matching '{search_term}' between {start_date_str} and {end_date_str}:")
    print("-" * 80)
    print(f"{'Date':<12} {'Time':<10} {'Product ID':<12} {'Product Name':<25} {'Quantity':<10} {'Payment':<10}")
    print("-" * 80)
    
    found = False
    for sale in sales_data:
        product_name = get_product_name(sale[2], products_data)
        
        # Check if product name matches
        if search_term in product_name.lower():
            try:
                sale_date = datetime.datetime.strptime(sale[0], "%d/%m/%Y")
                # Check if date is within range
                if start_date <= sale_date <= end_date:
                    print(f"{sale[0]:<12} {sale[1]:<10} {sale[2]:<12} {product_name:<25} {sale[3]:<10} {sale[4]:<10}")
                    found = True
            except ValueError:
                continue
    
    if not found:
        print(f"No sales records found matching the criteria.")
    print("-" * 80)


def get_product_name(product_id, products_data):
    """Helper function to get product name by ID."""
    for p in products_data:
        if p[0] == product_id:
            return p[1]
    return "Unknown"
