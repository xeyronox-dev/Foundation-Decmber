#!/bin/bash
# Comprehensive Test Runner for File Renamer

echo "========================================"
echo "File Renamer - Comprehensive Test Suite"
echo "========================================"

cd "$(dirname "$0")/.."

# Function to run a test
run_test() {
    local test_name="$1"
    local test_dir="$2"
    local inputs="$3"
    local expected_files="$4"

    echo ""
    echo "Running test: $test_name"
    echo "Directory: $test_dir"
    echo "Inputs: $inputs"

    # Reset test directory
    if [ -d "tests/$test_dir" ]; then
        rm -rf "tests/${test_dir}_backup"
        cp -r "tests/$test_dir" "tests/${test_dir}_backup"
    fi

    # Run the test
    echo "$inputs" | python file_renamer.py > "tests/expected_outputs/${test_name}_output.txt" 2>&1

    # Check results
    echo "Test completed. Check tests/expected_outputs/${test_name}_output.txt"
    echo "Expected files after rename: $expected_files"
    ls -la "tests/$test_dir/"
}

# Test 1: Prefix Addition
run_test "prefix_test" "test_prefix" $'test_prefix\n1\ntest_\ny' "test_file1.txt test_file2.txt test_document.pdf"

# Test 2: Suffix Addition
run_test "suffix_test" "test_suffix" $'test_suffix\n2\n_backup\ny' "report_backup.txt data_backup.csv image_backup.jpg"

# Test 3: Text Replacement
run_test "replace_test" "test_replace" $'test_replace\n3\nold\nnew\ny' "new_file.txt new_data.txt new_file.txt"

# Test 4: Numbering
run_test "numbering_test" "test_numbers" $'test_numbers\n4\n10\ny' "photo_010.jpg image_011.png picture_012.gif"

# Test 5: Case Conversion
run_test "case_test" "test_case" $'test_case\n5\ny' "mixed_case.txt another.file simple.txt"

# Test 6: Conflict Detection
run_test "conflict_test" "test_conflicts" $'test_conflicts\n5\ny' "test.txt TEST.TXT"

# Test 7: Empty Directory
run_test "empty_test" "test_empty" $'test_empty\nn' "No files found"

# Test 8: Invalid Directory
run_test "invalid_dir_test" "." $'nonexistent_dir\n' "does not exist"

echo ""
echo "========================================"
echo "Test Suite Complete!"
echo "Check tests/expected_outputs/ for results"
echo "========================================"