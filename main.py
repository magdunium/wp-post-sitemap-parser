#coding: utf-8

from bs4 import BeautifulSoup
import requests

urls = ['http://yourdomain1.pl/post-sitemap.xml','http://yourdomain2.pl/post-sitemap.xml']

for url in urls:
    html = requests.get(url).text
    bs = BeautifulSoup(html, 'html.parser')
    possible_links = bs.find_all('loc')
    for link in possible_links:
        print link.text