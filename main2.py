import requests
import time

url="http://olympus.realpython.org/profiles/dionysus"

for i in range(2):
    response=requests.get(url)
    if response.status_code==200:
        print("Request successful !")
        html_content=response.text
        print("HTML CONTENT")
        print(html_content)
    else:
        print(f"Response error occured:{response.status_code}")
    time.sleep(5)
