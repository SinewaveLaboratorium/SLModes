import requests
from bs4 import BeautifulSoup

import settings

def fetch_page_description(url):
    try:
        # Fetch the page content
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find the meta tag with the name 'description'
            meta_description = soup.find('meta', attrs={'name': 'description'})
            if meta_description and 'content' in meta_description.attrs:
                return meta_description['content']
            else:
                print("Description not found. Using default version.")
                return settings.slmodes_version
        else:
            print("Exception raised")
            raise Exception(f"Failed to retrieve page. Status code: {response.status_code}")

    except requests.ConnectionError:
        # Handle connection error (e.g., when offline)
        print("No internet connection. Using default version.")
        return settings.slmodes_version
