#coding: utf-8

from bs4 import BeautifulSoup
import requests

urls = ['http://yourdomain.pl/post-sitemap.xml','http://yourdomain.pl/post-sitemap.xml']


for url in urls:
    html = requests.get(url)

    if html.status_code != 200:
        print url, html.status_code
    else:
        bs = BeautifulSoup(html.text, 'html.parser')
        possible_links = bs.find_all('loc')
        for link in possible_links:
            print link.text