from __future__ import print_function
import torch
x = torch.rand(5, 5)# 行 列
print(x)


import urllib.request
import requests
import os
import time
import shutil
from lxml import html


def get_page():
    '''
    获取页面
    :return:
    '''
    url = "http://699pic.com/"
    i_headers = {
        "User-Agent": "",'Connection': 'close'
    }
    req = urllib.request.Request(url, headers=i_headers)
    page = urllib.request.urlopen(req).read()
    return page


def get_image(page):
    htm = html.fromstring(page)
    urls = []  # img路径
    for img_page in htm.xpath('//div[@class="label-list clearfix"]/a/@href'):
        if img_page[:4] == "http":
            urls.append(img_page)

    k = 1
    for url in urls:
        dirname = os.path.abspath(".") + "/" + str(k)  # 文件下载在项目路径下
        if os.path.exists(dirname):
            shutil.rmtree(dirname)
        os.mkdir(dirname)
        i_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400",
            "Referer": "http://699pic.com/?sem=1&sem_kid=33723&sem_type=1"
        }
        req = urllib.request.Request(url, headers=i_headers)
        i_page = urllib.request.urlopen(req).read()
        htm = html.fromstring(i_page)
        # img_title = htm.xpath('//div[@class="list"]/a/img/@alt')
        img_src = htm.xpath('//div[@class="list"]/a/img/@data-original')  # 图片的src获取不到
        num = 0

        for src in img_src:
            filename = dirname + "/" + str(num) + ".jpg"  # 这里名字先随便起了
            with open(filename, "wb") as img:  # 二进制写文件
                img.write(requests.get(src, headers=i_headers).content)
                time.sleep(0.5)
            num += 1
            if num > 5:  # 每个分类下载5张图片就结束
                break
        k += 1
        if k == 3:  # 这样做下载两个分类就结束
            break


if __name__ == '__main__':
    page = get_page()
    get_image(page)