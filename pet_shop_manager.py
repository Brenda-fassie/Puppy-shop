import sys
import csv
from getpass import getpass

# Import custom modules
from sales_operations import (enter_sales_record, search_sales_by_date, 
                              search_sales_by_product_name, search_sales_by_name_and_date)
from product_operations import add_new_product, modify_product

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
        sys.exit(1)
    return data, header

def main():
    """Main function to run the pet shop management system."""
    # 1. Get file paths from command line arguments
    if len(sys.argv) != 3:
        print("Usage: python pet_shop_manager.py <sales_file.csv> <products_file.csv>")
        sys.exit(1)

    sales_file_path = sys.argv[1]
    products_file_path = sys.argv[2]
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
        elif choice == '2':
            search_sales_by_date(sales_data, products_data)
        elif choice == '3':
            search_sales_by_product_name(sales_data, products_data)
        elif choice == '4':
            search_sales_by_name_and_date(sales_data, products_data)
        elif choice == '5' and logged_in_user_role == 'manager':
            modify_product(products_data)
        elif choice == '6' and logged_in_user_role == 'manager':
            add_new_product(products_data)
        elif choice == '7':
            # Logout
            save_csv_data(sales_file_path, sales_data, sales_header, delimiter='\t')
            save_csv_data(products_file_path, products_data, products_header)
            print("Data saved. Logging out. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")




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
    print("2. Search sales by date")
    print("3. Search sales by product name")
    print("4. Search sales by product name and date range")
    if role == 'manager':
        print("5. Modify puppy product details")
        print("6. Add a new puppy product")
    print("7. Logout")


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
