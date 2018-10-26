from bs4 import BeautifulSoup
import requests

sources = []
source = requests.get('https://jakoszczedzacpieniadze.pl/ranking-lokat-czyli-najlepsze-lokaty-bankowe').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())
print(soup.find_all('div', class_='container'))
