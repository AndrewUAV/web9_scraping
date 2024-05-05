import json
import threading as th
from connect_db import session
from models import Quotes, Authors
from create_quoter_file import create_quoter_file
from create_authors_file import create_authors_file


def create_all_data_files():
    th1 = th.Thread(create_quoter_file())
    th2 = th.Thread(create_authors_file())

    th1.start()
    th2.start()

    th1.join()
    th2.join()


def main():
    with open('authors.json', 'r') as file:
        authors_data = json.load(file)

    with open('quotes.json', 'r') as file:
        quotes_data = json.load(file)

    for author_data in authors_data:
        author = Authors(**author_data)
        session.add(author)

    for quote_data in quotes_data:
        tags = ', '.join(quote_data['tags'])
        quote_data['tags'] = tags
        quote = Quotes(**quote_data)
        session.add(quote)

    session.commit()


if __name__ == '__main__':
    create_all_data_files()
    main()