import pyperclip
import re
import time

def get_clipboard_url():
    # Get the clipboard content
    clipboard_content = pyperclip.paste()

    # Use regular expression to find URLs in the clipboard content
    url_pattern = re.compile(r'https?://\S+')
    urls = url_pattern.findall(clipboard_content)

    return urls

def save_url_to_file(url, file_path):
    # Read existing URLs from the file
    existing_urls = set()
    try:
        with open(file_path, 'r') as file:
            existing_urls = set(file.read().splitlines())
    except FileNotFoundError:
        pass

    # Check if the URL is not already in the file before saving
    if url not in existing_urls:
        with open(file_path, 'a') as file:
            file.write(url + '\n')
        print(f"Saved: {url}")

if __name__ == "__main__":
    # Specify the file path to save URLs
    file_path = "saved_urls.txt"

    # Infinite loop to continuously check clipboard and save URLs
    while True:
        # Get URLs from the clipboard
        urls = get_clipboard_url()

        # Save each URL to the file
        for url in urls:
            save_url_to_file(url, file_path)

        # Sleep for a short duration before checking again
        time.sleep(5)
