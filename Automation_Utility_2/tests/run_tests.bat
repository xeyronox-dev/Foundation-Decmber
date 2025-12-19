@echo off
REM Comprehensive Test Runner for File Renamer (Windows)

echo ========================================
echo File Renamer - Comprehensive Test Suite
echo ========================================

cd /d "%~dp0.."

REM Function to run a test
:run_test
set test_name=%~1
set test_dir=%~2
set inputs=%~3
set expected_files=%~4

echo.
echo Running test: %test_name%
echo Directory: %test_dir%
echo Inputs: %inputs%

REM Reset test directory
if exist "tests\%test_dir%" (
    rmdir /s /q "tests\%test_dir%_backup" 2>nul
    xcopy "tests\%test_dir%" "tests\%test_dir%_backup\" /e /i /h /y >nul
)

REM Run the test
echo %inputs% | python file_renamer.py > "tests\expected_outputs\%test_name%_output.txt" 2>&1

REM Check results
echo Test completed. Check tests\expected_outputs\%test_name%_output.txt
echo Expected files after rename: %expected_files%
dir "tests\%test_dir%\"
goto :eof

REM Run all tests
call :run_test "prefix_test" "test_prefix" "test_prefix\n1\ntest_\ny" "test_file1.txt test_file2.txt test_document.pdf"
call :run_test "suffix_test" "test_suffix" "test_suffix\n2\n_backup\ny" "report_backup.txt data_backup.csv image_backup.jpg"
call :run_test "replace_test" "test_replace" "test_replace\n3\nold\nnew\ny" "new_file.txt new_data.txt new_file.txt"
call :run_test "numbering_test" "test_numbers" "test_numbers\n4\n10\ny" "photo_010.jpg image_011.png picture_012.gif"
call :run_test "case_test" "test_case" "test_case\n5\ny" "mixed_case.txt another.file simple.txt"
call :run_test "conflict_test" "test_conflicts" "test_conflicts\n5\ny" "test.txt TEST.TXT"
call :run_test "empty_test" "test_empty" "test_empty\nn" "No files found"
call :run_test "invalid_dir_test" "." "nonexistent_dir\n" "does not exist"

echo.
echo ========================================
echo Test Suite Complete!
echo Check tests\expected_outputs\ for results
echo ========================================