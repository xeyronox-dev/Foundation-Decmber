"""
Advanced Profit/Loss Calculator

A comprehensive financial analysis tool for CSV data.
Supports filtering, analytics, export, and cross-platform use.

Version: 1.0
Author: Xeyronox
"""

import csv
import os
from collections import defaultdict

def validate_row(row):
    """Validate a CSV row for required fields and data types."""
    try:
        date = row.get('Date', '').strip()
        trans_type = row.get('Type', '').strip().lower()
        amount = float(row.get('Amount', '0').strip())
        description = row.get('Description', '').strip()

        if not date:
            return False, "Missing date"
        if trans_type not in ['revenue', 'expense']:
            return False, f"Invalid type: {trans_type}"
        if amount <= 0:
            return False, f"Invalid amount: {amount}"
        if not description:
            return False, "Missing description"

        return True, {'date': date, 'type': trans_type, 'amount': amount, 'description': description}
    except ValueError:
        return False, "Invalid amount format"

def load_financial_data(csv_file):
    """Load and validate financial data from CSV."""
    revenues = []
    expenses = []
    total_revenue = 0.0
    total_expenses = 0.0

    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row_num, row in enumerate(reader, start=2):
                valid, result = validate_row(row)
                if not valid:
                    print(f"Warning: Row {row_num} invalid - {result}. Skipping.")
                    continue

                data = result
                if data['type'] == 'revenue':
                    revenues.append(data)
                    total_revenue += data['amount']
                else:
                    expenses.append(data)
                    total_expenses += data['amount']

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return None

    return {
        'revenues': revenues,
        'expenses': expenses,
        'total_revenue': total_revenue,
        'total_expenses': total_expenses,
        'net_profit': total_revenue - total_expenses
    }

def display_results(data):
    """Display the profit/loss results clearly."""
    if data is None:
        return

    print("\n" + "="*50)
    print("          PROFIT/LOSS CALCULATOR RESULTS")
    print("="*50)

    print("\nREVENUE SUMMARY:")
    print(f"Total Revenue: ${data['total_revenue']:.2f}")
    print(f"Number of Revenue Transactions: {len(data['revenues'])}")
    if data['revenues']:
        print("Top Revenue Sources:")
        sorted_rev = sorted(data['revenues'], key=lambda x: x['amount'], reverse=True)[:3]
        for rev in sorted_rev:
            print(f"  ${rev['amount']:.2f} - {rev['description']} ({rev['date']})")

    print("\nEXPENSE SUMMARY:")
    print(f"Total Expenses: ${data['total_expenses']:.2f}")
    print(f"Number of Expense Transactions: {len(data['expenses'])}")
    if data['expenses']:
        print("Top Expense Categories:")
        expense_by_desc = defaultdict(float)
        for exp in data['expenses']:
            expense_by_desc[exp['description']] += exp['amount']
        sorted_exp = sorted(expense_by_desc.items(), key=lambda x: x[1], reverse=True)[:3]
        for desc, amt in sorted_exp:
            print(f"  ${amt:.2f} - {desc}")

    print("\nNET RESULT:")
    net = data['net_profit']
    if net > 0:
        print(f"[PROFIT] ${net:.2f}")
        print("Great job! You're in the green.")
    elif net < 0:
        print(f"[LOSS] ${abs(net):.2f}")
        print("Consider reviewing expenses or increasing revenue.")
    else:
        print("[BREAK-EVEN] $0.00")
        print("Balanced budget achieved.")

    print("\n" + "="*50)

def main():
    """Main function."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print("Profit/Loss Calculator")
    print("Analyzes revenue and expenses to calculate net profit or loss.\n")

    csv_file = input("Enter CSV file name (default: financial_data.csv): ").strip() or 'financial_data.csv'

    data = load_financial_data(csv_file)
    if data:
        display_results(data)

        # Option to save processed data
        if input("Save processed data to file? (y/n): ").strip().lower() == 'y':
            save_filename = input("Save filename (default: processed_data.json): ").strip() or 'processed_data.json'
            try:
                import json
                with open(save_filename, 'w') as f:
                    # Convert defaultdict to dict for JSON
                    json_data = {
                        'revenues': data['revenues'],
                        'expenses': data['expenses'],
                        'total_revenue': data['total_revenue'],
                        'total_expenses': data['total_expenses'],
                        'net_profit': data['net_profit']
                    }
                    json.dump(json_data, f, indent=2)
                print(f"Data saved to {save_filename}")
            except Exception as e:
                print(f"Error saving data: {e}")
    else:
        print("Could not load data. Please check your file.")

if __name__ == "__main__":
    main()