# File Renamer - Comprehensive Test Suite

This directory contains a complete test suite for the File Renamer tool, covering all features and edge cases.

## Test Structure

### Test Data Directories
- `test_prefix/` - Files for testing prefix addition
- `test_suffix/` - Files for testing suffix addition
- `test_replace/` - Files for testing text replacement
- `test_numbers/` - Files for testing sequential numbering
- `test_case/` - Files with mixed case for case conversion testing
- `test_conflicts/` - Files that would conflict on case-insensitive systems
- `test_empty/` - Empty directory for testing no-files scenario

### Expected Outputs
- `expected_outputs/` - Contains sample output files for comparison
- Each test generates an output file showing the tool's behavior

## Running Tests

### On Windows
```cmd
# Run all tests
tests\run_tests.bat

# Or run individual test
echo test_prefix\n1\ntest_\ny | python file_renamer.py
```

### On Linux/macOS/Termux
```bash
# Run all tests
bash tests/run_tests.sh

# Or run individual test
echo -e "test_prefix\n1\ntest_\ny" | python file_renamer.py
```

## Test Cases Covered

### 1. Basic Operations
- ✅ Prefix addition
- ✅ Suffix addition
- ✅ Text replacement
- ✅ Sequential numbering
- ✅ Case conversion (upper/lower)

### 2. Edge Cases
- ✅ Empty directory handling
- ✅ Invalid directory paths
- ✅ Files with no extensions
- ✅ Files with special characters

### 3. Error Conditions
- ✅ Permission denied scenarios
- ✅ File already exists conflicts
- ✅ Case sensitivity issues (Windows/macOS)
- ✅ Protected file skipping

### 4. User Experience
- ✅ Input validation loops
- ✅ Clear error messages
- ✅ Preview functionality
- ✅ Confirmation prompts
- ✅ Progress feedback

### 5. Cross-Platform
- ✅ Windows case-insensitive handling
- ✅ Unix/Linux case-sensitive support
- ✅ Path normalization
- ✅ Unicode filename support

### 6. Configuration
- ✅ Settings persistence
- ✅ Config file recovery
- ✅ Default value handling

## Test Results Validation

After running tests, compare the output files in `expected_outputs/` with the actual tool behavior. All tests should:

1. **Execute without crashes** - No unhandled exceptions
2. **Provide clear feedback** - Users understand what happened
3. **Handle errors gracefully** - Meaningful error messages
4. **Preserve data integrity** - No unintended file modifications
5. **Work across platforms** - Consistent behavior everywhere

## Adding New Tests

To add a new test case:

1. Create a new subdirectory in `test_data/`
2. Add appropriate test files
3. Update the test runner scripts
4. Add expected output in `expected_outputs/`
5. Update this README

## Test Automation

The test suite can be run automatically using the provided scripts, making it easy to validate changes and ensure compatibility across different environments.

## Continuous Testing

Run these tests whenever making changes to the file renamer to ensure all functionality remains intact and cross-platform compatibility is maintained.