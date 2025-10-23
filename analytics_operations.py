"""
Analytics Operations Module
Handles data analysis and visualization for sales performance.
Uses matplotlib and numpy for graphical displays.
"""

import datetime
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict


def display_monthly_sales(sales_data, products_data):
    """Display monthly sales values and number of sales using two line graphs."""
    print("\n--- Display Monthly Sales Performance ---")
    
    start_month = input("Enter start month (MM/YYYY): ")
    end_month = input("Enter end month (MM/YYYY): ")
    
    try:
        start_date = datetime.datetime.strptime(f"01/{start_month}", "%d/%m/%Y")
        end_date = datetime.datetime.strptime(f"01/{end_month}", "%d/%m/%Y")
        # Set end date to last day of the month
        if end_date.month == 12:
            end_date = end_date.replace(day=31)
        else:
            next_month = end_date.replace(month=end_date.month + 1, day=1)
            end_date = next_month - datetime.timedelta(days=1)
    except ValueError:
        print("Error: Invalid date format. Please use MM/YYYY.")
        return
    
    # Collect monthly data
    monthly_sales = defaultdict(lambda: {'value': 0.0, 'count': 0})
    
    for sale in sales_data:
        try:
            sale_date = datetime.datetime.strptime(sale[0], "%d/%m/%Y")
            if start_date <= sale_date <= end_date:
                month_key = sale_date.strftime("%m/%Y")
                monthly_sales[month_key]['value'] += float(sale[4])
                monthly_sales[month_key]['count'] += 1
        except (ValueError, IndexError):
            continue
    
    if not monthly_sales:
        print("No sales data found for the specified period.")
        return
    
    # Sort by date
    sorted_months = sorted(monthly_sales.keys(), key=lambda x: datetime.datetime.strptime(f"01/{x}", "%d/%m/%Y"))
    sales_values = [monthly_sales[m]['value'] for m in sorted_months]
    sales_counts = [monthly_sales[m]['count'] for m in sorted_months]
    
    # Create the plot with two y-axes
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    ax1.set_xlabel('Month', fontsize=12)
    ax1.set_ylabel('Sales Value ($)', color='blue', fontsize=12)
    line1 = ax1.plot(sorted_months, sales_values, color='blue', marker='o', label='Sales Value')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True, alpha=0.3)
    
    # Create second y-axis
    ax2 = ax1.twinx()
    ax2.set_ylabel('Number of Sales', color='red', fontsize=12)
    line2 = ax2.plot(sorted_months, sales_counts, color='red', marker='s', label='Number of Sales')
    ax2.tick_params(axis='y', labelcolor='red')
    
    # Title and legend
    plt.title(f'Monthly Sales Performance ({start_month} to {end_month})', fontsize=14, fontweight='bold')
    
    # Combine legends
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left')
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("graphs/monthly_sales.png")
    
    print(f"\nSaved to graphs/monthly_sales.png for the period from {start_month} to {end_month}.")


def display_product_monthly_sales(sales_data, products_data):
    """Display monthly sales for a specific product using two line graphs."""
    print("\n--- Display Product Monthly Sales ---")
    
    # Display product list
    print("\n--- Available Products ---")
    for p in products_data:
        print(f"ID: {p[0]}, Name: {p[1]}")
    print("-------------------------")
    
    product_id = input("Enter product ID: ")
    
    # Verify product exists
    product_name = None
    for p in products_data:
        if p[0] == product_id:
            product_name = p[1]
            break
    
    if not product_name:
        print("Error: Product ID not found.")
        return
    
    start_month = input("Enter start month (MM/YYYY): ")
    end_month = input("Enter end month (MM/YYYY): ")
    
    try:
        start_date = datetime.datetime.strptime(f"01/{start_month}", "%d/%m/%Y")
        end_date = datetime.datetime.strptime(f"01/{end_month}", "%d/%m/%Y")
        # Set end date to last day of the month
        if end_date.month == 12:
            end_date = end_date.replace(day=31)
        else:
            next_month = end_date.replace(month=end_date.month + 1, day=1)
            end_date = next_month - datetime.timedelta(days=1)
    except ValueError:
        print("Error: Invalid date format. Please use MM/YYYY.")
        return
    
    # Collect monthly data for the product
    monthly_sales = defaultdict(lambda: {'value': 0.0, 'count': 0})
    
    for sale in sales_data:
        try:
            if sale[2] == product_id:  # Check product ID
                sale_date = datetime.datetime.strptime(sale[0], "%d/%m/%Y")
                if start_date <= sale_date <= end_date:
                    month_key = sale_date.strftime("%m/%Y")
                    monthly_sales[month_key]['value'] += float(sale[4])
                    monthly_sales[month_key]['count'] += 1
        except (ValueError, IndexError):
            continue
    
    if not monthly_sales:
        print(f"No sales data found for product '{product_name}' in the specified period.")
        return
    
    # Sort by date
    sorted_months = sorted(monthly_sales.keys(), key=lambda x: datetime.datetime.strptime(f"01/{x}", "%d/%m/%Y"))
    sales_values = [monthly_sales[m]['value'] for m in sorted_months]
    sales_counts = [monthly_sales[m]['count'] for m in sorted_months]
    
    # Create the plot with two y-axes
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    ax1.set_xlabel('Month', fontsize=12)
    ax1.set_ylabel('Sales Value ($)', color='blue', fontsize=12)
    line1 = ax1.plot(sorted_months, sales_values, color='blue', marker='o', label='Sales Value')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True, alpha=0.3)
    
    # Create second y-axis
    ax2 = ax1.twinx()
    ax2.set_ylabel('Number of Sales', color='red', fontsize=12)
    line2 = ax2.plot(sorted_months, sales_counts, color='red', marker='s', label='Number of Sales')
    ax2.tick_params(axis='y', labelcolor='red')
    
    # Title and legend
    plt.title(f'Monthly Sales for {product_name} ({start_month} to {end_month})', 
              fontsize=14, fontweight='bold')
    
    # Combine legends
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left')
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("graphs/product_monthly_sales.png")
    
    print(f"\nSaved to graphs/product_monthly_sales.png for the period from {start_month} to {end_month}.")


def display_product_sales_comparison(sales_data, products_data):
    """Display total sales values by product using a bar chart, sorted in descending order."""
    print("\n--- Display Total Sales by Product ---")
    
    start_date_str = input("Enter start date (DD/MM/YYYY): ")
    end_date_str = input("Enter end date (DD/MM/YYYY): ")
    
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y")
        end_date = datetime.datetime.strptime(end_date_str, "%d/%m/%Y")
    except ValueError:
        print("Error: Invalid date format. Please use DD/MM/YYYY.")
        return
    
    # Collect sales by product
    product_sales = defaultdict(float)
    
    for sale in sales_data:
        try:
            sale_date = datetime.datetime.strptime(sale[0], "%d/%m/%Y")
            if start_date <= sale_date <= end_date:
                product_id = sale[2]
                product_sales[product_id] += float(sale[4])
        except (ValueError, IndexError):
            continue
    
    if not product_sales:
        print("No sales data found for the specified period.")
        return
    
    # Get product names and sort by sales value (descending)
    product_info = []
    for product_id, total_sales in product_sales.items():
        product_name = None
        for p in products_data:
            if p[0] == product_id:
                product_name = p[1]
                break
        if product_name:
            product_info.append((product_name, total_sales))
    
    # Sort by sales value in descending order
    product_info.sort(key=lambda x: x[1], reverse=True)
    
    product_names = [p[0] for p in product_info]
    sales_values = [p[1] for p in product_info]
    
    # Create bar chart
    fig, ax = plt.subplots(figsize=(14, 8))
    
    bars = ax.bar(range(len(product_names)), sales_values, color='steelblue', edgecolor='black')
    
    # Add value labels on top of bars
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:.2f}',
                ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Product Name', fontsize=12, fontweight='bold')
    ax.set_ylabel('Total Sales Value ($)', fontsize=12, fontweight='bold')
    ax.set_title(f'Total Sales by Product ({start_date_str} to {end_date_str})',
                 fontsize=14, fontweight='bold')
    
    ax.set_xticks(range(len(product_names)))
    ax.set_xticklabels(product_names, rotation=45, ha='right')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("graphs/product_sales_comparison.png")
    
    print(f"\nSaved to graphs/product_sales_comparison.png for the period from {start_date_str} to {end_date_str}.")
