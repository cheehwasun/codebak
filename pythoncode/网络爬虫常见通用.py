#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-12 20:52:57
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

import requests
import os
import re

# https加密网站
# import requests.packages.urllib3.util.ssl_
# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

# 常见user_agent
# USER_AGENTS = [
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#     "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#     "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#     "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#     "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#     "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
# ]


# headers = {'User-Agent': random.choice(USER_AGENTS)}#随机截取
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

# 获取页面信息，header 比如改变{userAgent：Mozilla/5.0}


def getHtml(url, params=None, headers=None, proxies=None, timeout=None):
    try:
        r = requests.get(url, params=params, headers=headers,
                         proxies=proxies, timeout=timeout)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # return r.text
        return BeautifulSoup(r.txt, 'lxml')
    except:
        return '网络异常'

# 获取网页元素并保存 比如图片p


def getElement(url, path):
    file = os.path.join(path, url.spilte('/')[-1])
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(file):
            r = requests.get(url)
            with open(file, 'wb') as f:
                f.write(r.content)
                f.close()
                print('保存成功')
        else:
            print('文件已经存在')

    except:
        print('爬取失败')


def regStr(regex):
    return re.compile(regex)


def parsePage(regex, html):
    try:
        return re.findall(regex, html)
    except Exception as e:
        raise e


# phantomjs 动态加载网页实例

from selenium import webdriver
# 请求头
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# phantomjs 添加请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4',
    'Connection': 'keep-alive'
}

cap = DesiredCapabilities.PhantomJS.copy()  # 使用copy()防止修改原代码定义dict
# 单一的更改useragent
# cap['phantomjs.page.settings.userAgent']=("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
for key, value in headers.items():
    cap['phantomjs.page.customHeaders.{}'.format(key)] = value


def getJs(url):
    driver = webdriver.PhantomJS(
        executable_path="phantomjs.exe", desired_capabilities=cap)
    driver.set_page_load_timeout(5)
    driver.set_window_size('30', '80')  # 设置浏览器宽30，高80
    driver.get(url)
    return driver.page_source


# BS4用法
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
# CSS 选择
    # 选择所有title标签
    soup.select("title")
    # 选择所有p标签中的第三个标签
    soup.select("p:nth-of-type(3)") 相当于soup.select(p)[2]
    # 选择body标签下的所有a标签
    soup.select("body a")
    # 选择body标签下的直接a子标签
    soup.select("body > a")
    # 选择id=link1后的所有兄弟节点标签
    soup.select("#link1 ~ .mysis")
    # 选择id=link1后的下一个兄弟节点标签
    soup.select("#link1 + .mysis")

    # 选择a标签，其id属性为link1的标签
    soup.select("a#link1")
    # 选择a标签，其类属性为mysis的标签
    soup.select("a.mysis")

    # 选择a标签，其属性中存在myname的所有标签
    soup.select("a[myname]")
    # 选择a标签，其属性href=http://example.com/lacie的所有标签
    soup.select("a[href='http://example.com/lacie']")
    # 选择a标签，其href属性以http开头
    soup.select('a[href^="http"]')
    # 选择a标签，其href属性以lacie结尾
    soup.select('a[href$="lacie"]')
    # 选择a标签，其href属性包含.com
    soup.select('a[href*=".com"]')
    # 从html中排除某标签，此时soup中不再有script标签
    [s.extract() for s in soup('script')]
    # 如果想排除多个呢
    [s.extract() for s in soup(['script', 'fram']

# tag用法

    article_user=tag.p.a.get_text()  # tag.p.a.string()
    article_user_url=tag.p.a['href']
    created=tag.p.span['data-shared-at']
    article_url=tag.h4.a['href']


# find——all
    soup.find_all('li', class_="have-img")
    # string 参数：通过 string 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, string 参数接受 字符串 , 正则表达式 , 列表, True 。 看例子:

     soup.find_all("a", string="Elsie")
