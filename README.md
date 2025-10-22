# All For My Puppy - Sales Management System

## 1. Description

This program is a command-line sales and inventory management system for a pet shop named "All For My Puppy". It allows sales assistants and managers to manage product inventory and process customer purchases. All data is stored in and retrieved from CSV files.

## 2. Features

*   **Role-Based User Authentication**: Differentiates between `manager` and `assistant` roles with different permissions.
*   **Sales Recording**: Allows users to record new sales, which automatically updates product stock levels.
*   **Product Management**: Allows managers to add new products to the inventory.
*   **Data Persistence**: Loads data from CSV files at the start and saves all changes back to the files upon logout.
*   **Secure Password Entry**: Hides password input for security.

## 3. Requirements

*   Python 3

## 4. How to Run the Program

To run the program, navigate to the project directory in your terminal and execute the following command:

```bash
python pet_shop_manager.py
```

The program will automatically load data from the CSV files (`sales.csv`, `puppy.csv`, and `users.csv`) located in the same directory. You will then be prompted to log in with a username and password from the `users.csv` file.

## 5. File Structure

*   `pet_shop_manager.py`: The main Python script containing all the program logic.
*   `puppy.csv`: Stores product information (id, name, price, stock).
*   `sales.csv`: Stores all sales transaction records.
*   `users.csv`: Stores user credentials and roles (username, password, type).
*   `README.md`: This documentation file.

## 6. Test Evidence Guide

This section provides a guide on how to test the program's functionality to ensure it meets all requirements.

### 6.1. Authentication

1.  **Test Manager Login**: Run the program and log in with manager credentials (e.g., `user2` / `user2`). The welcome message should greet you as a `manager`, and the menu should show the "Add a new puppy product" option.
2.  **Test Assistant Login**: Log in with assistant credentials (e.g., `user1` / `user1`). The welcome message should greet you as an `assistant`, and the menu should **not** show the "Add a new puppy product" option.
3.  **Test Invalid Login**: Attempt to log in with an incorrect username or password. The program should display an error and prompt you to log in again.

### 6.2. Sales and Inventory

1.  **Test Successful Sale**: Log in and select option `1`. Note the stock of a product (e.g., ID `1`, stock `50`).
2.  Enter the product ID (`1`) and a valid quantity (e.g., `5`).
3.  The program should confirm the sale.
4.  Log out to save the data.
5.  Inspect `puppy.csv` to confirm the stock for ID `1` has been reduced. Inspect `sales.csv` to confirm the new sale has been recorded at the end of the file.
6.  **Test Insufficient Stock**: Log in again and attempt to purchase the same product, but with a quantity greater than the remaining stock. The program should display an "Not enough stock" error and cancel the transaction.

### 6.3. Product Management (Manager Only)

1.  **Test Add Product**: Log in as a manager (`user2` / `user2`).
2.  Select option `2` to add a new product.
3.  Enter a name, price, and stock for the new item.
4.  The program should confirm that the product was added successfully.
5.  Log out.
6.  Inspect `puppy.csv` to confirm the new product has been added at the end of the file.