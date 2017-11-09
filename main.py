#coding: utf-8

from bs4 import BeautifulSoup
import requests
import os

urls = []
headers = {"User-Agent":"Mozilla/5.0"}

if os.path.isfile('url-list.txt'):
    with open('url-list.txt') as f:
        for line in f:
            urls.append(line)
else:
    print 'No "url-list.txt" file found. Create file "url-list.txt" to run the program'

for url in urls:
    html = requests.get(url, timeout = 5, headers=headers)

    if html.status_code != 200:
        print url, html.status_code
    else:
        bs = BeautifulSoup(html.text, 'html.parser')
        possible_links = bs.find_all('loc')
        for link in possible_links:
            print link.text
