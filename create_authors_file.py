import json
from find_info import (find_authors,
                       find_born_date,
                       find_born_location,
                       find_all_authors_links,
                       find_description)


def create_file(authors_list):
    file_name = 'authors.json'
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(authors_list, json_file, indent=2)


def create_authors_file():
    links = find_all_authors_links()
    fullname = find_authors()
    born_date = find_born_date(links)
    born_location = find_born_location(links)
    description = find_description(links)

    authors_list = list()

    for i in range(len(links)):
        authors = {
            'fullname': fullname[i],
            'born_date': born_date[i],
            'born_location': born_location[i],
            'description': description[i]
        }
        authors_list.append(authors)

    create_file(authors_list)

if __name__ == '__main__':
    create_authors_file()