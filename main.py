# Importing Requests
import requests
import time

url="http://olympus.realpython.org/profiles/aphrodite" # the website we want to get a
for i in range(1):
    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful!")
        html_content = response.text
        print("HTML Content:")
        print(html_content)
    else:
        print(f"Error: {response.status_code}")
    #Introducing a delay of 5 seconds
    time.sleep(5)