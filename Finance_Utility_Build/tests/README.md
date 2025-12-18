# Comprehensive Test Suite for Profit/Loss Calculator

This directory contains test cases for validating all features of the Profit/Loss Calculator.

## Test Files

### Data Files
- `november_data.csv`: Sample data for November 2023 (5 transactions, mixed revenue/expense)

### Test Scenarios

#### 1. Basic Profit Calculation
**Input:** Default settings with financial_data.csv
**Expected:** Profit of $16,600 with detailed breakdowns
**Command:** `echo -e "\n\n\nn\nn\nn" | python ../profit_loss_calculator.py`

#### 2. Date Range Filtering
**Input:** financial_data.csv, date range 2023-12-01 to 2023-12-15
**Expected:** Only December transactions within range
**Command:** `echo -e "\n\n\nn\ny\n2023-12-01\n2023-12-15\nn" | python ../profit_loss_calculator.py`

#### 3. Category Filtering - Revenue Only
**Input:** financial_data.csv, filter to revenue only
**Expected:** Only revenue transactions, no expenses
**Command:** `echo -e "\n\n\ny\nrevenue\nn\nn" | python ../profit_loss_calculator.py`

#### 4. Multi-File Processing
**Input:** financial_data.csv,november_data.csv
**Expected:** Combined analysis from both files
**Command:** `echo -e "\nfinancial_data.csv,november_data.csv\n\nn\nn\nn" | python ../profit_loss_calculator.py`

#### 5. Export to File
**Input:** Default with export enabled
**Expected:** Text file created with detailed report
**Command:** `echo -e "\n\n\nn\nn\ny\ntest_export.txt" | python ../profit_loss_calculator.py`

#### 6. Custom Currency
**Input:** Euro symbol (€), default data
**Expected:** All amounts shown in euros
**Command:** `echo -e "€\n\n\nn\nn\nn" | python ../profit_loss_calculator.py`

#### 7. Edge Case - No Data
**Input:** Empty or non-existent file
**Expected:** Graceful error message
**Command:** `echo -e "\nnonexistent.csv\nn\nn\nn" | python ../profit_loss_calculator.py`

#### 8. Invalid Data Handling
**Input:** CSV with invalid amounts/types
**Expected:** Warnings for invalid rows, processing of valid data
**Command:** Create test file with invalid data and run

## Running Tests

1. Navigate to the tests directory
2. Run the commands above to test each scenario
3. Compare outputs with expected results
4. Check that exports are created correctly
5. Verify error handling for edge cases

## Test Results

All tests should pass with appropriate outputs. The tool handles invalid inputs gracefully and provides clear feedback.