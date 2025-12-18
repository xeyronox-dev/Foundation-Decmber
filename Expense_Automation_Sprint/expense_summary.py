import csv
from datetime import datetime
import os
from collections import defaultdict

def main():
    # Auto-adjust to script's directory for relative paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # User inputs
    input_file = input("Enter input CSV file name (default: purchases.csv): ").strip() or 'purchases.csv'
    output_file = input("Enter output file name (default: Monthly_Summary.txt): ").strip() or 'Monthly_Summary.txt'

    # Category filtering
    filter_categories = None
    if input("Filter by categories? (y/n): ").strip().lower() == 'y':
        categories_str = input("Enter categories to include (comma-separated, e.g., Food,Rent): ").strip()
        filter_categories = [cat.strip() for cat in categories_str.split(',') if cat.strip()]

    # Date range filtering
    start_date = None
    end_date = None
    if input("Filter by date range? (y/n): ").strip().lower() == 'y':
        try:
            start_str = input("Enter start date (YYYY-MM-DD): ").strip()
            start_date = datetime.strptime(start_str, '%Y-%m-%d').date()
            end_str = input("Enter end date (YYYY-MM-DD): ").strip()
            end_date = datetime.strptime(end_str, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Proceeding without date filter.")

    try:
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)
            category_totals = defaultdict(float)
            monthly_totals = defaultdict(float)
            total_entries = 0
            for row in reader:
                try:
                    category = row['Category'].strip()
                    amount = float(row['Amount'])

                    # Parse date for trends and filters
                    row_date = None
                    try:
                        row_date = datetime.strptime(row['Date'].strip(), '%Y-%m-%d').date()
                        month = row_date.strftime('%Y-%m')
                        monthly_totals[month] += amount
                    except ValueError:
                        pass  # skip month if invalid date

                    # Apply filters
                    if filter_categories and category not in filter_categories:
                        continue
                    if row_date is None and (start_date or end_date):
                        continue
                    if row_date is not None and start_date and row_date < start_date:
                        continue
                    if row_date is not None and end_date and row_date > end_date:
                        continue

                    category_totals[category] += amount
                    total_entries += 1
                except ValueError:
                    print(f"Skipping invalid amount: {row['Amount']}")
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
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