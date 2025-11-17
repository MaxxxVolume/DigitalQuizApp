# Imports and Setup
import requests
from bs4 import BeautifulSoup

# Webpage for scraping knowledge
url = "https://en.wikipedia.org/wiki/Polar_bear"

# setting up a User-Agent 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko), Chrome/58.0.3029.110 Safari/537.36'
}

print("Fetching Webpage...")
try: 
    page = requests.get(url, headers=headers)
    page.raise_for_status()  # raises error if page is not found

except requests.exceptions.RequestException as e:
    print(f"Error fetching page: {e}")
    exit()

# Creating a BeatifulSoup object to parse HTML
soup = BeautifulSoup(page.content, "html.parser")

# finding and extracting the text
print("Extracting content...")
try:
    # find all paragraph tags on the page
    paragraphs = soup.find_all('p')

    # open a new file to save content
    with open("scraped_content.txt", "w", encoding="utf-8") as f:
        for p in paragraphs:
            # write clean text from each paragraph into the file
            f.write(p.get_text() + "\n\n")

    print("Success! Content saved to scraped_content.txt")

except Exception as e:
    print(f"Error extracting or writing text: {e}")

