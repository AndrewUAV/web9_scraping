import requests

from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


def find_authors():
    authors_list = list()
    authors = soup.find_all('small', class_='author')
    for author in authors:
        authors_list.append(author.get_text(strip=True))
    return authors_list


def find_all_authors_links():

    links = list()
    authors = soup.find_all('small', class_='author')
    for author in authors:
        link = url + author.find_next_sibling('a')['href']
        links.append(link)
    return links


def find_born_date(links: list):
    dates = list()

    for link in links:
        date_response = requests.get(link)
        date_soup = BeautifulSoup(date_response.text,'lxml')
        date = date_soup.find_all('span', class_='author-born-date')
        dates.append(date[0].get_text(strip=True))
    return dates


def find_born_location(links):
    locations = list()

    for link in links:
        location_response = requests.get(link)
        location_soup = BeautifulSoup(location_response.text, 'lxml')
        location = location_soup.find_all('span', class_='author-born-location')
        locations.append(location[0].get_text(strip=True))
    return locations


def find_description(links):
    descriptions = list()

    for link in links:
        description_response = requests.get(link)
        description_soup = BeautifulSoup(description_response.text, 'lxml')
        description = description_soup.find_all('div',class_='author-description')
        descriptions.append(description[0].get_text(strip=True))
    return descriptions


def find_tags():
    tags_list = list()
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        tags_div = quote.find('div', class_='tags')
        tags = tags_div.find_all('a', class_='tag')
        tags_author = [tag.get_text(strip=True) for tag in tags]
        tags_list.append(tags_author)
    return tags_list


def find_quote():
    quotes_list = list()

    quotes = soup.find_all('span', class_='text')
    for quote in quotes:
        quotes_list.append(quote.text.strip('\u201c\u201d'))
    return quotes_list
