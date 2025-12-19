# Automation Utility #2 - File Renamer

A simple, powerful bulk file renaming tool built during December 2025.

## Overview

This utility helps you quickly rename multiple files with various patterns, saving hours of manual renaming work. Perfect for organizing downloads, photos, documents, or any bulk file management task.

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

```bash
python file_renamer.py
```

### Interactive Prompts:
1. **Directory**: Enter path to scan (default: current directory)
2. **Operation**: Choose rename type (prefix, suffix, replace, numbering, case)
3. **Parameters**: Provide operation-specific details
4. **Preview**: Review changes before applying
5. **Confirm**: Apply or cancel the operation

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