# -*- coding: utf-8 -*-

import re
from urllib import request

    
def url_open(url):
    headers = {
        'Connection': 'Keep-Alive',
        'Cache-Control' : 'max-age=0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
    }

    req = request.Request(url, headers=headers)
    resp = request.urlopen(req)
    html = resp.read().decode('utf-8')
    #print(html)
    return html


def get_ip(html):
    p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25\[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25\[0-5])'
    ip_list = re.findall(p, html)

    num = 0
    for each in ip_list:
        num += 1
        print(num, ':', each)

if __name__ == '__main__':
    url = 'http://www.xicidaili.com'
    html = url_open(url)
    get_ip(html)
