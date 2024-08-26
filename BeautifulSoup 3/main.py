import requests
from bs4 import BeautifulSoup

# Function to fetch and parse the HTML content
def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the HTML content. Status code: {response.status_code}")
        return None

# Function to extract Urdu text from HTML using BeautifulSoup
def extract_urdu_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Adjust the CSS selector according to the structure of the webpage you are scraping
    urdu_elements = soup.select('div.bbc-1cvxiy9')  # Replace with the actual CSS selector
    urdu_text = [element.get_text() for element in urdu_elements]
    return urdu_text

# Function to save Urdu text to a text file
def save_to_text_file(urdu_text, file_name='output.txt'):
    with open(file_name, 'w', encoding='utf-8') as file:
        for text in urdu_text:
            file.write(text + '\n')

# URL of the Urdu webpage you want to scrap
url = 'https://www.bbc.com/urdu/articles/c4n0nzln42ro'

# Get HTML content
html_content = get_html_content(url)

if html_content:
    # Extract Urdu text
    urdu_text = extract_urdu_text(html_content)
    
    # Save to a text file
    save_to_text_file(urdu_text)
    print("Data saved to output.txt successfully.")
else:
    print("Web scraping failed.")