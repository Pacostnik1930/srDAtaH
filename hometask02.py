import requests
from bs4 import BeautifulSoup
import json

# Получение HTML-страницы
url = "http://books.toscrape.com/"
response = requests.get(url)
html_content = response.text

# Парсинг HTML
soup = BeautifulSoup(html_content, "html.parser")

# Извлечение информации о книгах
books = []
for article in soup.find_all("article", class_="Product Type"):
    # title = article.find("h3").find("a")["title"]
    price = article.find("p", class_="price_color").text
    availability = article.find("p", class_="instock availability").text.strip()
    # description = article.find("p", class_="product_description").text.strip()

    # Преобразование количества товара в наличии в число
    availability = int(availability.split()[2])

    book = {
        "price": price,
        "availability": availability,
    }
    books.append(book)

# Сохранение данных в JSON-файл
with open("books.json", "w") as f:
    json.dump(books, f, indent=4)

print("Данные сохранены в файл books.json")