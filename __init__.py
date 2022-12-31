#! /usr/bin/python
# coding:UTF-8

import requests

from bs4 import BeautifulSoup

link = "http://www.santostang.com/"  # 提供网址

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT6.1;en-US; rv:1. 9.1.6) Gecko/20091201 Firefox/3.5.6'}  # 编写遵从协议

r = requests.get(link, headers=headers)  # 向网址发送请求
print(r)
soup = BeautifulSoup(r.text,
                     "lxml")  # 运用BeautifulSoup 进行解析。
title = soup.find("h1", class_="post-title").a.text.strip()  # 对解析的数据进行筛选，选择 h1 的数据
print("soup=", soup)
with open("_init_.txt", "a+", encoding="utf-8") as f:  # a+代表可读写
    f.write("\n" + title + "\n")
    f.close()
