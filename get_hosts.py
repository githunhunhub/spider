# -*- coding: utf-8 -*-
from urllib import request
import os


def url_open(url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    req = request.Request(url=url, headers=headers)
    page = request.urlopen(req)
    html = page.read().decode('utf-8')
    # print(html)
    return html


def get_hosts(html):
    with open('C:\Windows\System32\drivers\etc\HOSTS', 'wt') as f:
        f.write(html)
    print('write finish')


if __name__ == "__main__":
    url = 'https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts'
    html = url_open(url)
    get_hosts(html)

