#!/usr/bin/python3
import requests
import csv

src = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts(link=src):
    response = requests.get(link)
    if response:
        print('Status Code: {}'.format(response.status_code))
        json_version = response.json()
        for i in range(0, len(json_version)):
            print(json_version[i]['title'])

def fetch_and_save_posts(link=src):
    list_of_dictionary_to_csv = []
    response = requests.get(link)
    if response:
        json_version = response.json()
        for i in range(0, len(json_version)):
            dict_for_while = {}
            dict_for_while['id'] = json_version[i]['id']
            dict_for_while['title'] = json_version[i]['title']
            dict_for_while['body'] = json_version[i]['body']
            list_of_dictionary_to_csv.append(dict_for_while)

    with open('posts.csv', 'w', newline='') as file:
        fieldnames = ['id', 'title',  'body']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in list_of_dictionary_to_csv:
            writer.writerow(i)
