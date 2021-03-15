import requests
from bs4 import BeautifulSoup


URL = 'https://www.mineplex.com/home/'

headers = {"User agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

count = soup.find(id = 'wwwMpPlayerCount').get_text()

print('Mineplex player count: ' + count)
