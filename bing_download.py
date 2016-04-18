# -*- coding: utf-8 -*-


import urllib.request

response = urllib.request.urlopen('http://s2.cn.bing.net/th?id=OJ.ZuiLxxWGLpZqTA&pid=MSNJVFeeds')
bing_img = response.read()

with open('th.jpg', 'wb') as f:
    f.write(bing_img)
