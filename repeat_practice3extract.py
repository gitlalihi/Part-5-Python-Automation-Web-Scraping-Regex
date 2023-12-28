#Using user-defined functions and much better handling of code using time delay for repeated requests
import requests
import time

def fetch_and_save(url, path):
    try:
        start_time = time.time()
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx status codes)
        with open(path, "wb") as f:
            f.write(response.content)
            end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Content fetched from {url} and saved to {path} successfully.")
        print(f"Time taken: {elapsed_time:.2f} seconds")
        # Introduce a time delay of 2 seconds (adjust as needed)
        time.sleep(2)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content: {e}")

url = "http://olympus.realpython.org/profiles/poseidon"
file_path = "data/poseidon.html"

fetch_and_save(url, file_path)