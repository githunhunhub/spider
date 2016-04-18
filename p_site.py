# -*- coding: utf-8 -*-

from urllib import request
import os

def url_open(page_url):
    req = request.Request(page_url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
    })

    resp = request.urlopen(page_url)
    html = resp.read()
    return html

def find_img_url(page_url):
    html = url_open(page_url).decode('utf-8')
    img_addrs = []
    # 查找关键词“img src”，并从后边提取图片网址
    a = html.find('img src')
    while a != -1:
        #print('a')
        b = html.find('.jpg', a, a+100)
        if b != -1:
            #print('b')
            img_addrs.append(html[a+9:b+4])
        else:
            b = a+9
        a = html.find('img src', b)
    for i in img_addrs:
        print(i)

    return img_addrs

def save_img(img_url):
    os.mkdir('acfun')
    os.chdir('acfun')

    for i in img_url:
        filename = i.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(i)
            f.write(img)

# 修改此处网址
page_url = 'http://www.acfun.tv/v/list59/index.htm'
img_url = find_img_url(page_url)
save_img(img_url)
