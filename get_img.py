# -*- coding: utf-8 -*-
import re
import os
import shutil
from urllib import request

def url_open(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
    }
    req = request.Request(url, headers=headers)
    page = request.urlopen(req)
    html = page.read().decode('gb2312', 'ignore')
    return html


def get_img(html):
    # ?: 在正则表达式中表示不要把此括号内的当成一个group
    p = r'<img src="([^"]+\.(?:jpg|png))"'
    img_list = re.findall(p, html)

    for l in img_list:
        print(l)

    if os.path.exists('get_img'):
        print("Exist")
        shutil.rmtree('get_img')
        os.mkdir('get_img')
        os.chdir('get_img')
    else:
        os.mkdir('get_img')
        os.chdir('get_img')
        print("Create")
    for each in img_list:
        filename = each.split('/')[-1]
        # 此处的urlretrieve与urlopen类似
        request.urlretrieve(each, filename, None)


if __name__ == '__main__':
    url = 'http://www.51tietu.net/tp'
    html = url_open(url)
    get_img(url_open(url))
