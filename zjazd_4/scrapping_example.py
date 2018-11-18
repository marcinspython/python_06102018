from requests import get
from bs4 import BeautifulSoup

url = "https://plot.ly/python/static-image-export/"

response = get(url)
# print(response.text)

html_soup = BeautifulSoup(response.text, 'html.parser')

books = html_soup.find_all('div', class_="book-info")
# print(books)
# print(books[0])

