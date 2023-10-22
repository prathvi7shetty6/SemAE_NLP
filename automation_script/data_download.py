import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse

# URL of the directory containing the files
base_url = "https://www.cs.unc.edu/~somnath/SemAE/data/amazon/json/"

# Send an HTTP GET request to the directory URL
response = requests.get(base_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all anchor tags (links) on the page
    links = soup.find_all("a")
    
    # Iterate through the links and download files
    for link in links:
        # Get the href attribute (link) from the anchor tag
        href = link.get("href")
        print(href)
        # Ignore parent directory link (../)
        if not href.startswith("../"):
            # Build the full URL for the file
            file_url = base_url + href
            
            # Extract the file name from the URL
            file_name = os.path.basename(urlparse(href).path)
            
            # Check if it's a file (not a directory or parent link)
            print(file_name)

            if "." in file_name:
                # Download the file
                try:
                    response = requests.get(file_url)
                    response.raise_for_status()
                    
                    with open(file_name, "wb") as file:
                        file.write(response.content)
                    
                    print(f"Downloaded: {file_name}")
                except requests.exceptions.RequestException as e:
                    print(f"Error downloading {file_name}: {str(e)}")
else:
    print("Error: Unable to retrieve the directory listing.")
