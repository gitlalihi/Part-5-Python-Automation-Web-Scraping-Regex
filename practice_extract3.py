import re
import requests
import time  

url = "http://olympus.realpython.org/profiles/poseidon"
for i in range(1):
    response = requests.get(url)
    if response.status_code == 200:
        print("Request successful!")
        html_content = response.text
        print("HTML CONTENT")
        print(html_content)
    else:
        print(f"Response error occurred: {response.status_code}")
    
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

time.sleep(1)
    