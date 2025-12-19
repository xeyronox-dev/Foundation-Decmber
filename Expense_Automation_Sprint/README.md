# Expense Summary Automator

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust, interactive Python script designed to automate the generation of monthly expense summaries from CSV data. It efficiently sums purchases by category, supports advanced filtering options, and provides quick financial insights while handling errors gracefully.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Testing](#testing)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [FAQ](#faq)
- [Support](#support)
- [Credits](#credits)
- [Changelog](#changelog)
- [License](#license)
- [Developer](#developer)

## Overview

### Problem
Manual expense totaling requires 20 minutes weekly, involving tedious calculations susceptible to human error.

### Solution
This automation script processes CSV purchase data, validates entries, sums amounts by category, and outputs a formatted summary instantly. It includes interactive options for custom file paths, category filtering, and date range selection.

## Who is This For?

**Perfect for:**
- **Small Business Owners**: Quickly analyze monthly expenses without manual calculations
- **Freelancers & Consultants**: Track project-related spending across categories
- **Students & Budget-Conscious Individuals**: Monitor personal expenses and spending patterns
- **Finance Teams**: Automate basic expense reporting and categorization
- **Anyone with CSV Expense Data**: If you export expenses from apps, banks, or accounting software

**Not suitable for:**
- Complex multi-company accounting systems
- Advanced financial analysis requiring charts/graphs
- Integration with existing accounting software

## Prerequisites

- **Python Version**: 3.x or higher
- **Input File**: `purchases.csv` with required columns:
  - `Date` (YYYY-MM-DD format)
  - `Category` (e.g., Food, Rent, Tech)
  - `Amount` (numeric values)

## Installation

Clone or download the repository and ensure Python is installed.

```bash
# No installation required - uses only Python standard library
```

## Usage

### Quick Start
1. Place your `purchases.csv` file in the project directory (or specify a custom path when prompted).
2. Run: `python expense_summary.py`
3. Follow the interactive prompts to configure options (file names, filters).
4. Review the generated summary file.

### Interactive Options
- **Input/Output Files**: Specify custom CSV input and text output file names.
- **Category Filtering**: Include only specific categories (comma-separated).
- **Date Range Filtering**: Limit to expenses within a date range (YYYY-MM-DD).

### Step-by-Step Example
```bash
$ python expense_summary.py

Enter input CSV file name (default: purchases.csv): purchases.csv
Enter output file name (default: Monthly_Summary.txt): expense_report.txt
Filter by categories? (y/n): y
Enter categories to include (comma-separated, e.g., Food,Rent): Food,Rent
Filter by date range? (y/n): y
Enter start date (YYYY-MM-DD): 2023-12-01
Enter end date (YYYY-MM-DD): 2023-12-31

Success: Summary generated in expense_report.txt
```

### Advanced Usage Examples

#### Filter by Specific Categories
```
Filter by categories? (y/n): y
Enter categories to include: Food,Transportation
```
Result: Only shows expenses in Food and Transportation categories.

#### Analyze Specific Time Period
```
Filter by date range? (y/n): y
Enter start date: 2023-11-01
Enter end date: 2023-11-30
```
Result: Only November 2023 expenses included.

#### Custom File Names
```
Enter input CSV file name: my_expenses.csv
Enter output file name: november_summary.txt
```
Result: Reads from `my_expenses.csv`, writes to `november_summary.txt`.

## Example

**Sample `purchases.csv`:**
```csv
Date,Category,Amount
2023-12-01,Food,50.00
2023-12-02,Rent,1000.00
2023-12-03,Tech,200.00
2023-12-04,Food,30.00
```

**Generated `Monthly_Summary.txt` (with defaults):**
```
Monthly Expense Summary

Food: $80.00
Rent: $1000.00
Tech: $200.00

Advanced Analytics:
Total Spending: $1280.00
Number of Transactions: 4
Average Transaction: $320.00
Monthly Trends:
  2023-12: $1280.00
Predicted Next Month: $1344.00 (5% increase)
```

## Features

| Feature              | Description                                      |
|----------------------|--------------------------------------------------|
| Error Handling      | Manages missing files and invalid data entries   |
| Category Summation  | Automatically groups and totals by category     |
| Data Validation     | Skips non-numeric amounts with warnings         |
| Formatted Output    | Produces clean, readable summary reports        |
| Cross-Platform      | Compatible with Windows, Linux, macOS, and Termux|
| Interactive Input   | Custom file paths and filtering options         |
| Date Range Filtering| Filter expenses by start and end dates          |
| Auto-Path Adjustment| Runs relative to script directory for portability|
| Advanced Analytics  | Trends, predictions, and spending insights      |

## Testing

Sample test outputs are available in the `test/` folder, demonstrating various filtering scenarios. Run the script with different inputs to verify functionality.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Roadmap

Future enhancements planned for this project:

- **Export to PDF**: Generate PDF reports with charts and summaries.
- **Advanced Analytics**: Add features like spending trends, budget comparisons, and predictive insights.
- **No GUI Planned**: The project will remain CLI-based for simplicity and cross-platform compatibility.

## FAQ

### How to handle large CSV files?
The script processes files line-by-line, so it can handle large files efficiently without loading everything into memory. For very large files, ensure sufficient RAM and consider splitting the CSV if needed.

### Can I use custom date formats?
Currently, dates must be in YYYY-MM-DD format. Future versions may support more formats.

### What if my CSV has extra columns?
The script only uses Date, Category, and Amount columns. Extra columns are ignored.

## Support

If you encounter issues or have questions:

- Check the FAQ above.
- Report bugs or request features via GitHub Issues (once the repository is uploaded).
- For direct support, contact the author.

## Credits

- **Developer**: Xeyronox
- **Libraries**: Built with Python's standard library (csv, datetime, os).
- Special thanks to the open-source community for inspiration.

## Changelog

### v0.1 - Initial Release (Dec 2025)
- Core functionality: CSV reading, category summation, error handling.
- Interactive features: Dynamic file paths, category and date filtering.
- Advanced analytics: Spending trends, predictions, and monthly breakdowns.
- Documentation: Complete README, license, tests, and requirements.
- Cross-platform support: Works on Windows, Linux, macOS, and Termux.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Xeyronox** - *Project Developer and Maintainer*

For inquiries or contributions, feel free to reach out.