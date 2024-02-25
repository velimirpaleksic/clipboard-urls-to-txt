# Clipboard URL Saver

## Overview

This Python program continuously monitors the clipboard for URLs and saves them to a text file. It checks if each URL is already present in the file to avoid duplicates.

## Requirements

- Python 3
- `pyperclip` library

Install the required library using:

```bash
pip install pyperclip
```

## Usage
1. Clone the repository or download the clipboard_url_saver.py file.
2. Run the program using:
```bash
python clipboard_url_saver.py
```
3. URLs copied to the clipboard will be checked and saved to the specified text file (saved_urls.txt by default).
4. The program runs in an infinite loop, continuously checking the clipboard every few seconds.

## Configuration
Specify the file path to save URLs by modifying the `file_path` variable in the script.
```bash
file_path = "saved_urls.txt"
```

Adjust the sleep duration in the loop to control how often the clipboard is checked.
```bash
# Sleep for a short duration before checking again
time.sleep(5)
```

## License
This project is licensed under the [MIT License](LICENSE).
