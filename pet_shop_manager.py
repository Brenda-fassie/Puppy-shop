
import csv
import datetime
from getpass import getpass

def load_csv_data(file_path, delimiter=','):
    """Loads data from a CSV file."""
    data = []
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            header = next(reader)  # Skip header
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return [], []
    return data, header

def main():
    """Main function to run the pet shop management system."""
    # 1. Set file paths
    sales_file_path = "sales.csv"
    products_file_path = "puppy.csv"
    users_file_path = "users.csv"

    # 2. Load data from CSV files
    sales_data, sales_header = load_csv_data(sales_file_path, delimiter='\t')
    products_data, products_header = load_csv_data(products_file_path)
    users_data, users_header = load_csv_data(users_file_path)

    print("Data loaded successfully.")
    print(f"Loaded {len(sales_data)} sales records.")
    print(f"Loaded {len(products_data)} product records.")
    print(f"Loaded {len(users_data)} user records.")

    # 3. User Authentication
    print("\n--- Login ---")
    logged_in_user_role = None
    while logged_in_user_role is None:
        logged_in_user_role = login(users_data)
        if logged_in_user_role is None:
            print("Invalid username or password. Please try again.")

    print(f"\nLogin successful! Welcome, {logged_in_user_role}.")

    # 4. Main Application Loop
    while True:
        display_menu(logged_in_user_role)
        choice = input("Enter your choice: ")

        if choice == '1':
            enter_sales_record(sales_data, products_data)
        elif choice == '2' and logged_in_user_role == 'manager':
            add_new_product(products_data)
        elif choice == '3':
            # 5. Logout
            save_csv_data(sales_file_path, sales_data, sales_header, delimiter='\t')
            save_csv_data(products_file_path, products_data, products_header)
            print("Data saved. Logging out. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def add_new_product(products_data):
    """Handles adding a new product to the system."""
    print("\n--- Add a New Puppy Product ---")

    # Generate new product ID
    # This is a simple way to generate a new ID. A more robust system might handle deleted IDs.
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

    # Assuming payment is handled externally for now, we calculate the total price.
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


def save_csv_data(file_path, data, header, delimiter=','):
    """Saves data to a CSV file."""
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        writer.writerow(header)
        writer.writerows(data)


def display_menu(role):
    """Displays the menu based on the user's role."""
    print("\n--- Menu ---")
    print("1. Enter a sales record")
    if role == 'manager':
        print("2. Add a new puppy product")
    print("3. Logout")


def login(users_data):
    """Authenticates a user and returns their role."""
    username = input("Username: ")
    password = getpass("Password: ")

    for user_record in users_data:
        # Assuming user_record is [username, password, type]
        if user_record[0] == username and user_record[1] == password:
            return user_record[2]  # Return the user's type/role
    return None


if __name__ == "__main__":
    main()
