import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all("h3")

    for i, title in enumerate(titles, start=1):
        print(f"{i}. {title.a.text.strip()}")
else:
    print("Failed to retrieve the webpage")
