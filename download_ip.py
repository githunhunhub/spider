# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup


def download_ip(url):
    response = request.urlopen(url)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html)
    for ip in soup.find_all('title'):
        print(ip.string)


if __name__ == '__main__':
    url = 'http://www.bilibili.com/'
    download_ip(url)
