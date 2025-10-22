"""
Product Operations Module
Handles all product-related functionality including adding and modifying products.
"""


def add_new_product(products_data):
    """Handles adding a new product to the system."""
    print("\n--- Add a New Puppy Product ---")

    # Generate new product ID
    new_id = str(max([int(p[0]) for p in products_data]) + 1)

    name = input("Enter product name: ")
    if not name:
        print("Error: Product name cannot be empty.")
        return

    try:
        price = float(input("Enter product price: "))
        if price < 0:
            print("Error: Price cannot be negative.")
            return
    except ValueError:
        print("Error: Invalid price. Please enter a number.")
        return

    try:
        stock = int(input("Enter initial stock level: "))
        if stock < 0:
            print("Error: Stock cannot be negative.")
            return
    except ValueError:
        print("Error: Invalid stock. Please enter a number.")
        return

    new_product = [new_id, name, f"{price:.2f}", str(stock)]
    products_data.append(new_product)
    print(f"Product '{name}' added successfully with ID {new_id}.")


def modify_product(products_data):
    """Handles modifying an existing product's details.
    Supports search by product ID or product name.
    """
    print("\n--- Modify Puppy Product Details ---")
    
    # Display all products
    print("\n--- Available Products ---")
    for p in products_data:
        print(f"ID: {p[0]}, Name: {p[1]}, Price: {p[2]}, Stock: {p[3]}")
    print("-------------------------")
    
    search_term = input("Enter product ID or product name: ")
    product_to_modify = None
    
    # Try to find by ID first
    for p in products_data:
        if p[0] == search_term:
            product_to_modify = p
            break
    
    # If not found by ID, search by name (case-insensitive, partial match)
    if not product_to_modify:
        search_term_lower = search_term.lower()
        matches = []
        for p in products_data:
            if search_term_lower in p[1].lower():
                matches.append(p)
        
        if len(matches) == 0:
            print("Error: No product found matching your search.")
            return
        elif len(matches) == 1:
            product_to_modify = matches[0]
        else:
            # Multiple matches found
            print("\nMultiple products found:")
            for i, p in enumerate(matches, 1):
                print(f"{i}. ID: {p[0]}, Name: {p[1]}, Price: {p[2]}, Stock: {p[3]}")
            
            try:
                choice = int(input("Select product number: "))
                if 1 <= choice <= len(matches):
                    product_to_modify = matches[choice - 1]
                else:
                    print("Error: Invalid selection.")
                    return
            except ValueError:
                print("Error: Invalid input.")
                return
    
    print(f"\nModifying product: {product_to_modify[1]} (ID: {product_to_modify[0]})")
    print("Leave blank to keep current value")
    
    # Modify price
    new_price = input(f"Enter new price (current: {product_to_modify[2]}): ")
    if new_price:
        try:
            price = float(new_price)
            if price < 0:
                print("Error: Price cannot be negative.")
                return
            product_to_modify[2] = f"{price:.2f}"
        except ValueError:
            print("Error: Invalid price. Please enter a number.")
            return
    
    # Modify stock
    new_stock = input(f"Enter new stock level (current: {product_to_modify[3]}): ")
    if new_stock:
        try:
            stock = int(new_stock)
            if stock < 0:
                print("Error: Stock cannot be negative.")
                return
            product_to_modify[3] = str(stock)
        except ValueError:
            print("Error: Invalid stock. Please enter a number.")
            return
    
    print(f"Product '{product_to_modify[1]}' updated successfully.")
