"""
File Renamer - Automation Utility #2

A straightforward tool for renaming multiple files at once.
Built during December 2025 as part of foundational programming work.

Techniques applied from Finance_Utility_Build & Expense_Automation_Sprint:
- Robust input validation
- Configuration persistence
- Comprehensive error handling
- User-friendly output formatting
- Cross-platform path handling

Author: Xeyronox
"""

import os
import json
import platform
from pathlib import Path

def is_case_sensitive_filesystem():
    """Check if the filesystem is case-sensitive."""
    try:
        # More reliable method: try to create test files
        test_dir = Path.cwd() / '.file_renamer_test'
        test_dir.mkdir(exist_ok=True)

        test_file_lower = test_dir / 'testfile.txt'
        test_file_upper = test_dir / 'TESTFILE.txt'

        # Create lowercase file
        test_file_lower.write_text('test')
        case_sensitive = not test_file_upper.exists()

        # Clean up
        test_file_lower.unlink(missing_ok=True)
        test_file_upper.unlink(missing_ok=True)
        test_dir.rmdir()

        return case_sensitive

    except:
        # Fallback to OS detection
        system = platform.system().lower()
        if system == 'windows':
            return False
        elif system == 'darwin':  # macOS
            return False  # Most common configuration
        else:
            return True  # Linux, Unix, Termux

def load_config():
    """Load user preferences from config file."""
    try:
        # Try different possible config locations for cross-platform support
        config_paths = [
            Path.home() / '.file_renamer_config.json',
            Path.home() / 'file_renamer_config.json',
            Path.cwd() / 'file_renamer_config.json'
        ]

        for config_path in config_paths:
            if config_path.exists():
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    # Validate config structure
                    if isinstance(config, dict):
                        return config
    except (json.JSONDecodeError, IOError, KeyError):
        # If config is corrupted, continue to defaults
        pass

    return {'last_directory': '.', 'last_operation': 'add_prefix'}

def save_config(config):
    """Save user preferences to config file."""
    try:
        config_paths = [
            Path.home() / '.file_renamer_config.json',
            Path.home() / 'file_renamer_config.json',
            Path.cwd() / 'file_renamer_config.json'
        ]

        for config_path in config_paths:
            try:
                # Ensure directory exists
                config_path.parent.mkdir(parents=True, exist_ok=True)
                with open(config_path, 'w', encoding='utf-8') as f:
                    json.dump(config, f, indent=2, ensure_ascii=False)
                break  # Success, no need to try other locations
            except (IOError, OSError):
                continue  # Try next location
    except:
        # If all saving attempts fail, silently continue
        pass

def ask_yes_no(question, default='n'):
    """Ask a yes/no question with a default answer."""
    while True:
        answer = input(f"{question} (y/n, default {default}): ").strip().lower()
        if answer in ['y', 'yes', 'n', 'no', '']:
            return answer in ['y', 'yes'] or (answer == '' and default == 'y')
        print("Please enter 'y' for yes or 'n' for no.")

def get_input_with_default(prompt, default):
    """Get user input with a default value."""
    response = input(f"{prompt} (default: {default}): ").strip()
    return response if response else default

def validate_directory(directory_path):
    """Validate and normalize directory path."""
    if not directory_path or not isinstance(directory_path, str):
        print("Directory path cannot be empty.")
        return None

    try:
        # Convert to absolute path and resolve any relative components
        abs_path = os.path.abspath(directory_path.strip())

        if not abs_path:
            print("Invalid directory path.")
            return None

        if not os.path.exists(abs_path):
            print(f"Directory '{abs_path}' does not exist.")
            print("Please check the path and try again.")
            return None

        if not os.path.isdir(abs_path):
            print(f"'{abs_path}' is not a directory.")
            return None

        # Check if we can read the directory
        try:
            os.listdir(abs_path)
        except PermissionError:
            print(f"No permission to read directory '{abs_path}'.")
            print("Try running as administrator or choose a different directory.")
            return None
        except OSError as e:
            print(f"Cannot access directory: {e}")
            return None

        return abs_path

    except Exception as error:
        print(f"Error validating directory: {error}")
        return None

def get_rename_instructions():
    """Ask user what kind of renaming they want to do."""
    print("\nWhat kind of renaming would you like me to do?")
    print("1. Add a prefix (like 'old_' before each name)")
    print("2. Add a suffix (like '_backup' after each name)")
    print("3. Replace text (change 'old' to 'new' in names)")
    print("4. Add numbers (001, 002, 003, etc.)")
    print("5. Make all names lowercase")
    print("6. Make all names UPPERCASE")

    while True:
        choice = input("Enter your choice (1-6): ").strip()
        if choice in ['1', '2', '3', '4', '5', '6']:
            break
        print("Please enter a number between 1 and 6.")

    instructions = {}

    if choice == '1':
        prefix = input("What prefix should I add? ").strip()
        instructions = {'type': 'add_prefix', 'text': prefix}
    elif choice == '2':
        suffix = input("What suffix should I add? ").strip()
        instructions = {'type': 'add_suffix', 'text': suffix}
    elif choice == '3':
        old_text = input("What text should I replace? ").strip()
        new_text = input("What should I replace it with? ").strip()
        instructions = {'type': 'replace_text', 'old': old_text, 'new': new_text}
    elif choice == '4':
        start_num_input = input("Starting number (default: 1)? ").strip()
        start_num = int(start_num_input) if start_num_input.isdigit() else 1
        instructions = {'type': 'add_numbers', 'start': start_num}
    elif choice == '5':
        instructions = {'type': 'make_lowercase'}
    elif choice == '6':
        instructions = {'type': 'make_uppercase'}
    else:
        print("I didn't understand that choice. No changes will be made.")
        instructions = {'type': 'none'}

    return instructions

def find_files_in_directory(directory_path):
    """Find all files in a directory with validation."""
    validated_path = validate_directory(directory_path)
    if not validated_path:
        return []

    files_found = []
    try:
        for item in os.listdir(validated_path):
            full_path = os.path.join(validated_path, item)
            if os.path.isfile(full_path):
                files_found.append(item)
    except Exception as error:
        print(f"Problem reading directory: {error}")

    return sorted(files_found)

def show_rename_preview(file_list, rename_instructions):
    """Show what the renames will look like."""
    print("\n--- RENAME PREVIEW ---")
    for filename in file_list:
        new_name = generate_new_filename(filename, rename_instructions)
        if new_name != filename:
            print(f"  {filename} -> {new_name}")
        else:
            print(f"  {filename} -> (no change)")
    print("--- END PREVIEW ---\n")

def generate_new_filename(original_name, instructions):
    """Create the new filename based on instructions."""
    # Handle edge cases
    if not original_name or not isinstance(original_name, str):
        return original_name

    name_part, extension = os.path.splitext(original_name)

    # Ensure we have valid strings
    name_part = str(name_part) if name_part else ''
    extension = str(extension) if extension else ''

    operation = instructions.get('type', 'none')

    try:
        if operation == 'add_prefix':
            text = instructions.get('text', '')
            return f"{text}{name_part}{extension}"
        elif operation == 'add_suffix':
            text = instructions.get('text', '')
            return f"{name_part}{text}{extension}"
        elif operation == 'replace_text':
            old_text = instructions.get('old', '')
            new_text = instructions.get('new', '')
            new_name_part = name_part.replace(old_text, new_text)
            return f"{new_name_part}{extension}"
        elif operation == 'add_numbers':
            start = instructions.get('start', 1)
            return f"{name_part}_{start:03d}{extension}"
        elif operation == 'make_lowercase':
            return f"{name_part.lower()}{extension.lower()}"
        elif operation == 'make_uppercase':
            return f"{name_part.upper()}{extension.upper()}"
        else:
            return original_name
    except Exception:
        # If anything goes wrong, return original name
        return original_name

def execute_renames(directory_path, file_list, instructions):
    """Actually rename the files with comprehensive error handling."""
    successful_renames = 0
    problems_encountered = []

    # Safety check: don't rename this script or critical files
    script_name = os.path.basename(__file__)
    protected_files = {script_name, 'file_renamer.py', 'README.md', 'LICENSE'}

    for index, old_filename in enumerate(file_list):
        # Skip protected files
        if old_filename.lower() in protected_files:
            print(f"- Skipped: {old_filename} (protected file)")
            continue

        try:
            old_path = os.path.join(directory_path, old_filename)

            # Check if source file still exists
            if not os.path.exists(old_path):
                problems_encountered.append(f"Source file {old_filename} no longer exists")
                print(f"[SKIPPED] {old_filename}: File no longer exists")
                continue

            if instructions['type'] == 'add_numbers':
                # Apply actual sequential numbering
                name_part, ext = os.path.splitext(old_filename)
                start_number = instructions['start']
                new_filename = f"{name_part}_{start_number + index:03d}{ext}"
            else:
                new_filename = generate_new_filename(old_filename, instructions)

            if new_filename != old_filename:
                new_path = os.path.join(directory_path, new_filename)

                # Check if target file already exists
                if os.path.exists(new_path):
                    problems_encountered.append(f"Target file {new_filename} already exists")
                    print(f"[SKIPPED] {old_filename}: Target filename already exists")
                    continue

                # On case-insensitive filesystems, check for case conflicts
                if not is_case_sensitive_filesystem():
                    # Check if any existing file has the same name ignoring case
                    existing_files = [f.lower() for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
                    if new_filename.lower() in existing_files:
                        problems_encountered.append(f"Case conflict: {new_filename} would conflict with existing file on case-insensitive filesystem")
                        print(f"[SKIPPED] {old_filename}: Case conflict with existing file")
                        continue

                # Attempt the rename
                os.rename(old_path, new_path)
                print(f"[OK] Renamed: {old_filename} -> {new_filename}")
                successful_renames += 1
            else:
                print(f"- Skipped: {old_filename} (no change needed)")

        except PermissionError:
            error_message = f"No permission to rename {old_filename}"
            print(f"[ERROR] {error_message}")
            problems_encountered.append(error_message)
        except OSError as error:
            error_message = f"OS error renaming {old_filename}: {error}"
            print(f"[ERROR] {error_message}")
            problems_encountered.append(error_message)
        except Exception as error:
            # Catch any other unexpected errors
            error_message = f"Unexpected error renaming {old_filename}: {error}"
            print(f"[ERROR] {error_message}")
            problems_encountered.append(error_message)

    return successful_renames, problems_encountered

def main():
    """
    Main application entry point.

    Workflow:
    1. Load user preferences from config file
    2. Get target directory from user (with smart defaults)
    3. Validate directory access and permissions
    4. Scan for files and display count
    5. Present renaming options and get user choice
    6. Show preview of changes
    7. Apply renames with confirmation
    8. Save preferences for next use
    """
    # Load user preferences from previous sessions
    config = load_config()

    print("File Renamer Tool")
    print("Let's rename some files together!")
    print("I work on Windows, macOS, Linux, and even Termux on Android.\n")

    # Get target directory (default to current directory)
    default_dir = config.get('last_directory', '.')
    target_directory = get_input_with_default("Which directory should I check", default_dir)

    # Validate directory exists and is accessible
    validated_directory = validate_directory(target_directory)
    if not validated_directory:
        print("Please try again with a valid directory path.")
        return

    # Find files
    found_files = find_files_in_directory(validated_directory)
    if not found_files:
        print("I didn't find any files in that directory.")
        print("Make sure there are files in the folder you specified.")
        return

    print(f"\nGreat! I found {len(found_files)} file{'s' if len(found_files) != 1 else ''} in that directory:")
    for i, filename in enumerate(found_files[:10], 1):
        print(f"  {i}. {filename}")
    if len(found_files) > 10:
        print(f"  ... and {len(found_files) - 10} more files")

    print("\nLet's decide how to rename them!")

    # Get renaming instructions
    rename_instructions = get_rename_instructions()

    if not rename_instructions or rename_instructions.get('type') == 'none':
        print("No valid operation selected. Exiting.")
        return

    # Update config with last operation
    config['last_directory'] = validated_directory
    config['last_operation'] = rename_instructions['type']
    save_config(config)

    # Show preview
    show_rename_preview(found_files, rename_instructions)

    # Confirm with clear explanation
    print("\nThis is just a preview. I can show you exactly what will happen before I make any changes.")
    print("Important: I will skip protected files like this script itself.")

    # Safety check: ensure at least one file will be renamed
    will_rename = any(generate_new_filename(f, rename_instructions) != f for f in found_files)
    if not will_rename:
        print("No files would be changed with the current settings.")
        print("Try different rename options.")
        return

    if not ask_yes_no("Should I go ahead and rename these files"):
        print("No problem! I won't change anything. You can run me again anytime.")
        return

    # Do the renaming
    renamed_count, errors = execute_renames(validated_directory, found_files, rename_instructions)

    # Summary
    print("\n--- SUMMARY ---")
    print(f"Total files checked: {len(found_files)}")
    print(f"Files successfully renamed: {renamed_count}")
    if errors:
        print(f"Files I couldn't rename: {len(errors)}")
        print("Check the error messages above for details.")
    else:
        print("Perfect! All files renamed without any issues.")

    print("\nThanks for using the File Renamer! Happy organizing!")

if __name__ == "__main__":
    main()