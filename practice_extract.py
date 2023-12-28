# Using regex built-in module to undersstand structure of html at the basic level
import re
import requests
import time  

url = "http://olympus.realpython.org/profiles/dionysus"
for i in range(1):
    response = requests.get(url)
    if response.status_code == 200:
        print("Request successful!")
        html_content = response.text
        print("HTML CONTENT")
        print(html_content)
    else:
        print(f"Response error occurred: {response.status_code}")
    # Use regular expressions to extract information
    title_match = re.search(r'<title[^>]*>(.*?)<\/title>', html_content, re.IGNORECASE | re.DOTALL)
    name_match = re.search(r'<h2>Name: (.*?)<\/h2>', html_content, re.IGNORECASE | re.DOTALL)
    hometown_match = re.search(r'Hometown: (.*?)<', html_content, re.IGNORECASE | re.DOTALL)
    animal_match = re.search(r'Favorite animal: (.*?)<', html_content, re.IGNORECASE | re.DOTALL)
    color_match = re.search(r'Favorite Color: (.*?)<', html_content, re.IGNORECASE | re.DOTALL)

    # Extract information from matches
    title = title_match.group(1).strip() if title_match else ''
    name = name_match.group(1).strip() if name_match else ''
    hometown = hometown_match.group(1).strip() if hometown_match else ''
    animal = animal_match.group(1).strip() if animal_match else ''
    color = color_match.group(1).strip() if color_match else ''

    # Print extracted information
    print(f"Title: {title}")
    print(f"Name: {name}")
    print(f"Hometown: {hometown}")
    print(f"Favorite Animal: {animal}")
    print(f"Favorite Color: {color}")
time.sleep(1)  
