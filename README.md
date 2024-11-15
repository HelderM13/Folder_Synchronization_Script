
# Folder Synchronization Script

This Python script synchronizes two folders: `source` and `replica`. The `replica` folder is updated to become an identical copy of the `source` folder, ensuring one-way synchronization. The script runs periodically, copying, updating, or removing files in the `replica` folder to match the `source` folder. All file operations are logged to both the console and a log file.

## Features

- **One-way Synchronization**: The content of the `replica` folder is updated to match the `source` folder.
- **Periodic Execution**: The synchronization is performed at regular intervals (default: every 10 seconds).
- **File Operations Logging**: All file creation, copying, updating, and removal actions are logged in `log.txt` and displayed in the console.

## Requirements

- **Python 3.10.11**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org).

## Usage

### 1. Setup
1. Clone this repository or copy the script to your local machine.
2. Create a directory named `source` in the same folder as the script. The script will also create a `replica` directory automatically if it doesn't exist.
3. Ensure the `source` folder has files to be synchronized with the `replica` folder.

### 2. Run the Script
Run the script using the following command in your terminal or command prompt:
```bash
python Folder_Synchronization_Script.py
```

> Replace `Folder_Synchronization_Script.py` with the actual name of your script file.

### 3. Stopping the Script
The script runs continuously. To stop it, use `Ctrl + C` in the terminal or close the command prompt.

## File Structure

- **source/**: The folder where the original files are located. This folder must contain files to be synchronized with the `replica`.
- **replica/**: The folder that will be synchronized to match the `source` folder.
- **log.txt**: A file where all synchronization operations are logged.

## Logging

All file operations are logged in `log.txt`. Each entry includes a description of the action performed, such as:
- File creation
- File copying or updating
- File or directory removal

### Example Log Entry
```
Created file: C:\path	o\source\dummy1.txt
Copied/Updated file: C:\path	o\source\dummy1.txt to C:\path	o
eplica\dummy1_replica.txt
Removed file: C:\path	o
eplica\old_file_replica.txt
```

## Configuration

### Synchronization Interval
The synchronization interval is set to 10 seconds by default. You can change this value by modifying the `interval` variable in the script.

## Limitations

- The script does not support two-way synchronization. Changes made in the `replica` folder are not propagated back to the `source`.
- The program does not handle large folders with complex directory structures efficiently. Consider optimizations for such use cases.

## Future Improvements

- Add command-line arguments for better customization (e.g., paths, interval).
- Implement better handling for large file operations.
- Add support for logging timestamps for each operation.
