import requests
from bs4 import BeautifulSoup
import json


url = "http://books.toscrape.com/"
response = requests.get(url)
html_content = response.text


soup = BeautifulSoup(html_content, "html.parser")


books = []
for article in soup.find_all("article", class_="Product Type"):
   
    price = article.find("p", class_="price_color").text
    availability = article.find("p", class_="instock availability").text.strip()


    
    availability = int(availability.split()[2])

    book = {
        "price": price,
        "availability": availability,
    }
    books.append(book)


with open("books.json", "w") as f:
    json.dump(books, f, indent=4)

print("Данные сохранены в файл books.json")