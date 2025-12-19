"""
Expense Summary Automator

A reliable Python script for processing expense data from CSV files.
Provides automated categorization, filtering, and financial insights.

Features:
- CSV data validation and processing
- Category-based expense summation
- Date range filtering
- Monthly trend analysis
- Error handling and data integrity checks

Author: Xeyronox
Version: 0.1
License: MIT
"""

import csv
from datetime import datetime
import os
from collections import defaultdict


def main():
    """
    Main application entry point.

    Orchestrates the entire expense analysis workflow:
    1. Get user preferences (files, filters)
    2. Process CSV data with validation
    3. Apply filters and calculations
    4. Generate comprehensive report
    """
    # Ensure we work from the script's directory for consistent file paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Get user preferences for input/output files
    input_file = input("Enter input CSV file name (default: purchases.csv): ").strip() or 'purchases.csv'
    output_file = input("Enter output file name (default: Monthly_Summary.txt): ").strip() or 'Monthly_Summary.txt'

    # Configure category filtering - allows users to focus on specific expense types
    filter_categories = None
    if input("Filter by categories? (y/n): ").strip().lower() == 'y':
        categories_str = input("Enter categories to include (comma-separated, e.g., Food,Rent): ").strip()
        # Clean and validate category inputs
        filter_categories = [cat.strip() for cat in categories_str.split(',') if cat.strip()]

    # Configure date range filtering - allows analysis of specific time periods
    start_date = None
    end_date = None
    if input("Filter by date range? (y/n): ").strip().lower() == 'y':
        try:
            start_str = input("Enter start date (YYYY-MM-DD): ").strip()
            start_date = datetime.strptime(start_str, '%Y-%m-%d').date()
            end_str = input("Enter end date (YYYY-MM-DD): ").strip()
            end_date = datetime.strptime(end_str, '%Y-%m-%d').date()
        except ValueError:
            # Handle invalid date formats gracefully
            print("Invalid date format. Proceeding without date filter.")

    # Process the CSV file with comprehensive error handling
    try:
        with open(input_file, 'r', newline='') as file:  # Specify newline='' for cross-platform compatibility
            reader = csv.DictReader(file)

            # Initialize data structures for analysis
            category_totals = defaultdict(float)  # Automatically handles new categories
            monthly_totals = defaultdict(float)   # Track spending by month
            total_entries = 0

            for row in reader:
                try:
                    # Extract and validate data from CSV row
                    category = row['Category'].strip()
                    amount = float(row['Amount'])

                    # Parse date for trend analysis (optional field)
                    row_date = None
                    try:
                        row_date = datetime.strptime(row['Date'].strip(), '%Y-%m-%d').date()
                        month_key = row_date.strftime('%Y-%m')
                        monthly_totals[month_key] += amount
                    except ValueError:
                        # Date parsing is optional - continue without monthly breakdown
                        pass

                    # Apply user-defined filters
                    if filter_categories and category not in filter_categories:
                        continue  # Skip categories not in the filter list

                    # Apply date range filters if specified
                    if start_date and row_date and row_date < start_date:
                        continue  # Skip entries before start date
                    if end_date and row_date and row_date > end_date:
                        continue  # Skip entries after end date

                    # Accumulate valid data
                    category_totals[category] += amount
                    total_entries += 1

                except (ValueError, KeyError) as e:
                    # Handle data validation errors gracefully
                    print(f"Warning: Skipping invalid row - {e}")
                    continue

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found. Please check the file path.")
        return
    except PermissionError:
        print(f"Error: No permission to read '{input_file}'. Check file permissions.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    total_spending = sum(category_totals.values())

    try:
        with open(output_file, 'w') as f:
            f.write("Monthly Expense Summary\n\n")
            if category_totals:
                for category, total in category_totals.items():
                    f.write(f"{category}: ${total:.2f}\n")
                f.write("\n\nAdvanced Analytics:\n")
                f.write(f"Total Spending: ${total_spending:.2f}\n")
                f.write(f"Number of Transactions: {total_entries}\n")
                if total_entries > 0:
                    f.write(f"Average Transaction: ${total_spending / total_entries:.2f}\n")
                f.write("Monthly Trends:\n")
                for month, total in sorted(monthly_totals.items()):
                    f.write(f"  {month}: ${total:.2f}\n")
                f.write(f"Predicted Next Month: ${total_spending * 1.05:.2f} (5% increase)\n")
            else:
                f.write("No matching expenses found.\n")
        print(f"Success: Summary generated in {output_file}.")
    except Exception as e:
        print(f"Error writing summary: {e}")

if __name__ == "__main__":
    main()