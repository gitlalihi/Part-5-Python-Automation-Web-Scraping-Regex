# extract and store the fetched data using regex built-in module
import requests
import re
import time

def fetch_and_save(url, file_path):
    try:
        start_time = time.time()
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx status codes)
        with open(file_path, "wb") as f:
            f.write(response.content)
            end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Content fetched from {url} and saved to {file_path} successfully.")  
        print(f"Time taken: {elapsed_time:.2f} seconds")
        # Introduce a time delay of 5 seconds (adjust as needed)
        time.sleep(5)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content: {e}")

def extract_details(html_content):
    name_match = re.search(r'<h2>Name: (.*?)<\/h2>', html_content, re.IGNORECASE | re.DOTALL)
    animal_match = re.search(r'Favorite animal: (.*?)<', html_content, re.IGNORECASE | re.DOTALL)
    color_match = re.search(r'Favorite Color: (.*?)<', html_content, re.IGNORECASE | re.DOTALL)
    hometown_match = re.search(r'Hometown: (.*?)<', html_content, re.IGNORECASE | re.DOTALL)

    if name_match:
        name = name_match.group(1).strip()
        print(f"Name: {name}")
    if animal_match:
        animal = animal_match.group(1).strip()
        print(f"Favorite Animal: {animal}")
    if color_match:
        color = color_match.group(1).strip()
        print(f"Favorite Color: {color}")
    if hometown_match:
        hometown = hometown_match.group(1).strip()
        print(f"Hometown: {hometown}")
    return name, animal, color, hometown

url = "http://olympus.realpython.org/profiles/poseidon"
file_path = "data/poseidon.html"

# Fetch and save the HTML content
fetch_and_save(url, file_path)

# Read the saved HTML file and extract details
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

name, favorite_animal, favorite_color, hometown = extract_details(html_content)

