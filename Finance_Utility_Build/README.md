# Profit/Loss Calculator

A simple Python tool to calculate profit or loss from financial transaction data in CSV format.

## Overview

This tool analyzes revenue and expense data to provide a clear financial summary, including total profit/loss, transaction counts, and top categories.

## Features

- **Input Validation**: Checks for valid data types, required fields, and positive amounts
- **Clear Console Output**: Formatted results with summaries and insights
- **CSV Data Processing**: Reads standard CSV with Date, Type, Amount, Description columns
- **Financial Insights**: Shows revenue sources, expense categories, and net results
- **Error Handling**: Skips invalid rows with warnings

## Requirements

- Python 3.x
- No external libraries required (uses standard library)

## Installation

No installation needed. Just run the script with Python.

## Usage

1. Prepare a CSV file with columns: Date, Type (Revenue/Expense), Amount, Description
2. Run: `python profit_loss_calculator.py`
3. Enter the CSV filename when prompted (or press enter for default)
4. View the formatted profit/loss report

## Example

**Sample financial_data.csv:**
```csv
Date,Type,Amount,Description
2023-12-01,Revenue,5000.00,Product Sales
2023-12-02,Expense,1500.00,Rent
2023-12-03,Revenue,3200.00,Service Fees
```

**Output:**
```
==================================================
          PROFIT/LOSS CALCULATOR RESULTS
==================================================

REVENUE SUMMARY:
Total Revenue: $8200.00
Number of Revenue Transactions: 2
Top Revenue Sources:
  $5000.00 - Product Sales (2023-12-01)
  $3200.00 - Service Fees (2023-12-03)

EXPENSE SUMMARY:
Total Expenses: $1500.00
Number of Expense Transactions: 1
Top Expense Categories:
  $1500.00 - Rent

NET RESULT:
[PROFIT] $6700.00
Great job! You're in the green.

==================================================
```

## Sample Data

A sample CSV file `financial_data.csv` is included with example transactions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### v1.0 - Enhanced Release (Dec 2025)
- Core functionality: CSV reading, revenue/expense calculation, profit/loss analysis.
- Advanced features: Date filtering, category filtering, multiple currencies, batch processing.
- Analytics: Monthly trends, percentages, forecasting, text charts.
- Export: Save detailed reports to files.
- Configuration: User preferences and settings.
- Cross-platform support: Works on Windows, Linux, macOS, Termux.
- Input validation and error handling.
- Clear console output with comprehensive summaries.
- Sample data and documentation.

## Author

**Xeyronox** - *Project Developer and Maintainer*

For inquiries or contributions, feel free to reach out.