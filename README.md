# All For My Puppy - Sales Management System

## 1. Description

This program is a command-line sales and inventory management system for a pet shop named "All For My Puppy". It allows sales assistants and managers to manage product inventory and process customer purchases. All data is stored in and retrieved from CSV files.

## 2. Features

### Question 1 Features:
*   **Role-Based User Authentication**: Differentiates between `manager` and `assistant` roles with different permissions.
*   **Sales Recording**: Allows users to record new sales, which automatically updates product stock levels.
*   **Product Management**: Allows managers to add new products to the inventory.
*   **Data Persistence**: Loads data from CSV files at the start and saves all changes back to the files upon logout.
*   **Secure Password Entry**: Hides password input for security.

### Question 2 Features:
*   **Modular Design**: Code is organized into separate modules (sales_operations.py, product_operations.py) for better maintainability.
*   **Search Sales by Date**: Search and display all sales made on a specific date.
*   **Search Sales by Product Name**: Case-insensitive partial match search for sales by product name (e.g., "dog" matches "Junior Dog Food" and "Dog Collar").
*   **Search Sales by Name and Date Range**: Combined search by product name and date range.
*   **Enhanced Modify Product**: Managers can search for products by ID or name (partial match) when modifying.

### Question 3 Features (New):
*   **Monthly Sales Visualization**: Display overall monthly sales values and counts using dual-axis line graphs.
*   **Product Monthly Sales**: Display monthly sales performance for a specific product with line graphs.
*   **Sales Comparison Bar Chart**: Display total sales by product sorted in descending order using bar charts.
*   **Uses numpy and matplotlib**: Professional data visualization with proper titles, labels, and legends.

## 3. Requirements

*   Python 3
*   numpy (for Question 3)
*   matplotlib (for Question 3)

### Installing Dependencies

For Question 3 graphical features, install the required packages:

```bash
# Using apt (Debian/Ubuntu)
sudo apt install python3-numpy python3-matplotlib

# Or using pip
pip3 install -r requirements.txt
```

## 4. How to Run the Program

To run the program, navigate to the project directory in your terminal and execute the following command, providing the paths to the sales and product CSV files:

```bash
python pet_shop_manager.py sales.csv puppy.csv
```

**Command Line Arguments:**
*   First argument: Path to the sales file (e.g., `sales.csv`)
*   Second argument: Path to the product file (e.g., `puppy.csv`)

The program will load these files along with `users.csv` for authentication. You will then be prompted to log in with a username and password from the `users.csv` file.

## 5. File Structure

*   `pet_shop_manager.py`: The main Python script with authentication and menu logic.
*   `sales_operations.py`: Module containing sales-related functions (enter, search).
*   `product_operations.py`: Module containing product-related functions (add, modify).
*   `analytics_operations.py`: Module containing data visualization functions (Question 3).
*   `puppy.csv`: Stores product information (id, name, price, stock).
*   `sales.csv`: Stores all sales transaction records.
*   `users.csv`: Stores user credentials and roles (username, password, type).
*   `requirements.txt`: Python package dependencies.
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

### 6.3. Sales Search Features

**Test Search by Date:**
1.  Log in with any credentials.
2.  Select option `2` to search sales by date.
3.  Enter a date (e.g., `11/09/2022`).
4.  The program should display all sales for that date with product names.

**Test Search by Product Name:**
1.  Log in with any credentials.
2.  Select option `3` to search sales by product name.
3.  Enter a partial product name (e.g., `dog`).
4.  The program should display all sales containing "dog" in the product name (case-insensitive).

**Test Search by Name and Date Range:**
1.  Log in with any credentials.
2.  Select option `4` to search by name and date range.
3.  Enter a product name and date range (e.g., `dog`, `11/09/2022`, `15/09/2022`).
4.  The program should display matching sales within the date range.

### 6.4. Product Management (Manager Only)

**Test Modify Product (Enhanced):**
1.  Log in as a manager (`user2` / `user2`).
2.  Select option `5` to modify a product.
3.  Enter either a product ID (e.g., `1`) or product name (e.g., `dog` for partial match).
4.  If multiple products match, select from the list.
5.  Modify the price or stock level (or both).
6.  The program should confirm that the product was updated successfully.
7.  Log out.
8.  Inspect `puppy.csv` to confirm the product details have been updated.

**Test Add Product:**
1.  Log in as a manager (`user2` / `user2`).
2.  Select option `6` to add a new product.
3.  Enter a name, price, and stock for the new item.
4.  The program should confirm that the product was added successfully.
5.  Log out.
6.  Inspect `puppy.csv` to confirm the new product has been added at the end of the file.

### 6.5. Analytics and Visualization (Question 3)

**Test Monthly Sales Display:**
1.  Log in with any credentials.
2.  Select option `7` to display monthly sales performance.
3.  Enter a start month (e.g., `09/2022`) and end month (e.g., `12/2022`).
4.  A dual-axis line graph should display showing sales values (blue) and number of sales (red).
5.  The graph should have proper title, axis labels, and legend.

**Test Product Monthly Sales:**
1.  Log in with any credentials.
2.  Select option `8` to display product monthly sales.
3.  View the product list and enter a product ID (e.g., `7`).
4.  Enter start and end months (e.g., `09/2022` to `12/2022`).
5.  A dual-axis line graph should display for the selected product.

**Test Sales Comparison Bar Chart:**
1.  Log in with any credentials.
2.  Select option `9` to display total sales by product.
3.  Enter a start date (e.g., `11/09/2022`) and end date (e.g., `30/09/2022`).
4.  A bar chart should display showing all products sorted by total sales (descending).
5.  Each bar should show the sales value on top.
6.  The graph should have proper title, axis labels, and be sorted correctly.