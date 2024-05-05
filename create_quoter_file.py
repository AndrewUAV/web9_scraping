import json
from find_info import find_tags, find_authors, find_quote


def create_file(quotes_list):
    file_name = 'quotes.json'
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(quotes_list, json_file, indent=2)


def create_quoter_file():
    tags = find_tags()
    author = find_authors()
    quote = find_quote()
    quotes_list = list()
    for i in range(len(author)):
        quotes = {
            'tags': tags[i],
            'author': author[i],
            'quote': quote[i]
        }
        quotes_list.append(quotes)

    create_file(quotes_list)


if __name__ == "__main__":
    create_quoter_file()