# Automation Utility #2 - File Renamer

A simple, powerful bulk file renaming tool built during December 2025.

## Overview

This utility helps you quickly rename multiple files with various patterns, saving hours of manual renaming work. Perfect for organizing downloads, photos, documents, or any bulk file management task.

## Who is This For?

**Perfect for:**
- **Content Creators**: Rename batches of photos, videos, or audio files
- **Digital Organizers**: Clean up messy download folders or file collections
- **System Administrators**: Bulk rename files on servers or user directories
- **Developers**: Organize project files with consistent naming
- **Anyone with Files**: If you need to rename many files with patterns

**Not suitable for:**
- Files that are currently open in other applications
- System-critical files (renaming may cause issues)
- Files with complex naming requirements beyond patterns
- Large-scale enterprise file management systems

## Features

- 🔄 **Multiple Rename Patterns**:
  - Add prefixes or suffixes
  - Replace text within filenames
  - Add sequential numbering
  - Convert case (upper/lower)
- 👀 **Preview Mode**: See changes before applying
- ✅ **Safe Operations**: Confirm before making changes
- 📁 **Directory Support**: Works with any folder
- 🚫 **Error Handling**: Skips problematic files gracefully

## Usage

### Quick Start
```bash
python file_renamer.py
```

### Interactive Prompts:
1. **Directory**: Enter path to scan (default: current directory)
2. **Operation**: Choose rename type (prefix, suffix, replace, numbering, case)
3. **Parameters**: Provide operation-specific details
4. **Preview**: Review changes before applying
5. **Confirm**: Apply or cancel the operation

### Step-by-Step Example
```bash
$ python file_renamer.py

File Renamer Tool
Let's rename some files together!

Which directory should I check (default: .): my_photos

I found 5 files:
  1. IMG_001.jpg
  2. IMG_002.jpg
  3. IMG_003.jpg
  4. DSC_001.jpg
  5. photo.jpg

Let's decide how to rename them!

What kind of renaming would you like me to do?
1. Add a prefix (like 'old_' before each name)
2. Add a suffix (like '_backup' after each name)
3. Replace text (change 'old' to 'new' in names)
4. Add numbers (001, 002, 003, etc.)
5. Make all names lowercase
6. Make all names UPPERCASE
Enter your choice (1-6): 1
What prefix should I add? vacation_2023_

--- RENAME PREVIEW ---
  IMG_001.jpg -> vacation_2023_IMG_001.jpg
  IMG_002.jpg -> vacation_2023_IMG_002.jpg
  IMG_003.jpg -> vacation_2023_IMG_003.jpg
  DSC_001.jpg -> vacation_2023_DSC_001.jpg
  photo.jpg -> vacation_2023_photo.jpg
--- END PREVIEW ---

Should I go ahead and rename these files (y/n, default n): y
[OK] Renamed: IMG_001.jpg -> vacation_2023_IMG_001.jpg
[OK] Renamed: IMG_002.jpg -> vacation_2023_IMG_002.jpg
[OK] Renamed: IMG_003.jpg -> vacation_2023_IMG_003.jpg
[OK] Renamed: DSC_001.jpg -> vacation_2023_DSC_001.jpg
[OK] Renamed: photo.jpg -> vacation_2023_photo.jpg

--- SUMMARY ---
Files I looked at: 5
Files I renamed: 5
Perfect! All files renamed without any issues.

Thanks for using the File Renamer! Happy organizing!
```

### Common Use Cases

#### Organize Photos by Event
```
Pattern: Add prefix "summer_vacation_"
Result: summer_vacation_IMG_001.jpg, summer_vacation_IMG_002.jpg, etc.
```

#### Add Sequential Numbers
```
Pattern: Add numbers starting at 001
Result: file_001.txt, file_002.txt, file_003.txt
```

#### Standardize File Extensions
```
Pattern: Make all lowercase
Result: DOCUMENT.PDF → document.pdf
```

#### Clean Up Downloads
```
Pattern: Replace " " with "_"
Result: my file.txt → my_file.txt
```

## Examples

### Add Prefix
```
Files: document1.txt, document2.txt
Pattern: Add prefix "report_"
Result: report_document1.txt, report_document2.txt
```

### Sequential Numbering
```
Files: photo.jpg, image.jpg, pic.jpg
Pattern: Add numbering starting at 001
Result: photo_001.jpg, image_002.jpg, pic_003.jpg
```

### Replace Text
```
Files: report_old.txt, data_old.csv
Pattern: Replace "old" with "new"
Result: report_new.txt, data_new.csv
```

## Getting Started

Create some test files in a directory and run the tool:

```bash
# Create test files
echo "test" > file1.txt
echo "test" > file2.txt
echo "test" > old_report.txt

# Run the renamer
python file_renamer.py
```

## Requirements

- Python 3.x
- No external dependencies

## Safety Features

- **Preview before apply**: Always see what will change
- **Confirmation required**: No accidental renames
- **Error recovery**: Continues with other files if one fails
- **No overwrites**: Won't overwrite existing files

## Cross-Platform

Works on:
- ✅ Windows
- ✅ Linux
- ✅ macOS
- ✅ Termux (Android)

## Author

**Xeyronox** - Built as part of Foundation December 2025

Focus: Time-saving automation without complexity.

## License

MIT License