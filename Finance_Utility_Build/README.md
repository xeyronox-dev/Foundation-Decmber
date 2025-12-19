# Profit/Loss Calculator

A simple Python tool to calculate profit or loss from financial transaction data in CSV format.

## Overview

This tool analyzes revenue and expense data to provide a clear financial summary, including total profit/loss, transaction counts, and top categories.

## Who is This For?

**Perfect for:**
- **Small Business Owners**: Track profitability and identify top revenue sources
- **Freelancers & Entrepreneurs**: Monitor business financial health with simple metrics
- **Financial Analysts**: Quick analysis of transaction data without complex software
- **Accountants**: Validate financial data and generate basic profit/loss reports
- **Students & Educators**: Learn financial analysis concepts with real data

**Not suitable for:**
- Complex financial modeling or forecasting
- Multi-currency transactions (single currency only)
- Advanced accounting features (taxes, depreciation, etc.)
- Integration with existing accounting systems

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

### Quick Start
1. Prepare a CSV file with columns: Date, Type (Revenue/Expense), Amount, Description
2. Run: `python profit_loss_calculator.py`
3. Enter the CSV filename when prompted (or press enter for default)
4. View the formatted profit/loss report

### Step-by-Step Example
```bash
$ python profit_loss_calculator.py

Profit/Loss Calculator
Analyzes revenue and expenses to calculate net profit or loss.

Enter CSV file name (default: financial_data.csv): financial_data.csv
```

The tool will then process your data and display a comprehensive report.

### CSV File Format
Your CSV must have these exact column headers:
- **Date**: Transaction date (YYYY-MM-DD format)
- **Type**: Either "Revenue" or "Expense" (case-insensitive)
- **Amount**: Numeric value (positive for both revenue and expenses)
- **Description**: Brief description of the transaction

### Usage Examples

#### Basic Profit Analysis
```
Input: Mixed revenue and expense transactions
Output: Total revenue, total expenses, net profit/loss
```

#### Revenue-Only Analysis
```
Input: Only revenue transactions
Output: Revenue breakdown and sources
```

#### Expense Tracking
```
Input: Only expense transactions
Output: Expense categories and spending analysis
```

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