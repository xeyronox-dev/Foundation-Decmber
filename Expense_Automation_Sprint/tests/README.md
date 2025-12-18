# Test Cases

This folder contains sample outputs from running the expense_summary.py script with different configurations.

## Test Files

- **full_summary.txt**: Full dataset summary with all categories and dates.
- **food_only.txt**: Filtered to show only 'Food' category expenses.
- **december_only.txt**: Filtered to show only expenses from December 2023.
- **combined_food_dec.txt**: Combined filter for 'Food' category in December 2023.

## How to Run Tests

Use the script interactively or pipe inputs:

```bash
# Full summary
echo -e "\n\nn\nn\nn" | python ../expense_summary.py

# Food only
echo -e "\n\ny\nFood\nn\nn" | python ../expense_summary.py

# December only
echo -e "\n\ndec_test.txt\nn\ny\n2023-12-01\n2023-12-31\nn" | python ../expense_summary.py

# Combined Food + Dec
echo -e "\n\ncombined_test.txt\ny\nFood\ny\n2023-12-01\n2023-12-31\nn" | python ../expense_summary.py
```

Compare outputs with these reference files.