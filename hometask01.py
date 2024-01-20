import requests

def search_venues(category):
    client_id = 'CEZEH0N4PF5PKUHGTOA4ZUIDJBF5FSY11H2JNCQ2O5OFGLCF'  # Замените на ваш реальный client ID Foursquare
    client_secret = 'ITUIJPQ3HCVHHMRJVAGMPCJTWCZCRKBO1ZS1DZEYS0OUXGNN'  # Замените на ваш реальный client secret Foursquare
    version = '20220101'  # Версия API

    # Запрос к API Foursquare для поиска заведений в указанной категории
    url = f'https://api.foursquare.com/v2/venues/search?client_id={client_id}&client_secret={client_secret}&v={version}&near=New+York&query={category}'
    response = requests.get(url)
    data = response.json()

    # Обработка полученных данных
    for venue in data['response']['venues']:
        name = venue['name']
        address = venue['location']['address'] if 'address' in venue['location'] else 'Адрес не указан'
        rating = venue['rating'] if 'rating' in venue else 'Рейтинг не указан'
        print(f'Название: {name}, Адрес: {address}, Рейтинг: {rating}')

if __name__ == '__main__':
    category = input('Введите категорию заведений (например, кофейни, музеи, парки и т.д.): ')
    search_venues(category)