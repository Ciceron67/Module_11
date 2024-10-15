import requests
from bs4 import BeautifulSoup

url = ('https://trudvsem.ru/vacancy/search?_regionIds='
       '7700000000000&page=0&salary=0&salary=999999&scheduleType=FULL&busyType=FULL&education='
       'HIGH&professionalSphere=InformationTechnology&vacancyType=LONG')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
divs = soup.find_all('div')
for i, div in enumerate(divs):
    print(f"{div.text.strip()}")
else:
    print(f'Ошибка: {response.status_code}')
