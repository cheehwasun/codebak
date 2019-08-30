#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:08:04
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# coding=utf-8
# urllibdemo.py urllib演示

# urllib 用于处理Url相关的工具,用于从网络获取数据(网页源码/下载资源)
from urllib import request  # 请求url, 支持 HTTP(0.9/1.0) / FTP / 本地文件 / URL
from urllib import parse  # 解析url, 支持 file / ftp / gopher / hdl / http / https / imap / mailto / mms / news / nntp / prospero / rsync / rtsp / rtspu / sftp / shttp / sip / sips / snews / svn / svn+ssh / telnet / wais
from urllib import robotparser  # 分析 robots.txt 文件
from urllib import error  # 异常
import re  # 正则模块
from bs4 import BeautifulSoup
import os

# 演示(下载斗鱼首页的图片)


def demo():
    os.mkdir("images")

    # -- 获取网页源代码 --
    f = request.urlopen("https://www.douyu.com")
    data = f.read().decode("utf-8")

    # -- 获取网页源码中的图片地址 --
    # 方式一: 正则的方式
    images = re.findall(r'src="(.*?\.(jpg|png))"', data)
    tnum = 0
    for i in images:
        # 下载资源
        request.urlretrieve(i[0], "./images/%d.%s" % (tnum, i[1]))
        tnum += 1

    # 方式二: Beautiful Soup (安装: pip install beautifulsoup4) 提取html/xml标签中的内容
    soup = BeautifulSoup(data, "html.parser")
    images = soup.find_all("img")  # 取标签

    tnum = 0
    for i in images:
        # 下载资源
        imgurl = i.get("src")
        if len(imgurl) > 3:
            request.urlretrieve(imgurl, "./images/%d.jpg" % tnum)
        tnum += 1

    # -- 关闭 --
    f.close


# 参数详解
def fun():
    neturl = "http://luzhuo.me/blog/Base1.html"
    imgurl = "http://luzhuo.me/image/performers/%E5%85%B3%E6%99%93%E5%BD%A4.jpg"

    # --- urllib.parse --- 解析Url
    # - 编码 -
    neturl = "%s?%s" % (neturl, parse.urlencode(
        {"name": "luzhuo", "age": 21}))  # Get传参url构建
    data = parse.urlencode({"name": "luzhuo", "啊age": 21}
                           ).encode('ascii')  # POST参参data构建

    # - 解码 -
    # => ParseResult(scheme='http', netloc='luzhuo.me', path='/image/performers/%E5%85%B3%E6%99%93%E5%BD%A4.jpg', params='', query='', fragment=''
    urls = parse.urlparse(imgurl)
    urls = parse.urlparse(
        "//luzhuo.me/image/performers/%E5%85%B3%E6%99%93%E5%BD%A4.jpg?a=1")
    scheme = urls.scheme  # 获取相应数据

    # - 替换 -
    # 替换后部分 => http://luzhuo.me/blog/Fame.html
    url = parse.urljoin('http://luzhuo.me/blog/Base1.html', 'Fame.html')
    url = parse.urljoin('http://luzhuo.me/blog/Base1.htm',
                        '//xxx/blog')  # => http://xxx/blog

    # --- urllib.reques --- 请求数据
    try:
        # - Request - 构建
        req = request.Request(neturl)  # GET
        req = request.Request(neturl, headers={"1": "2"})  # 添加请求头
        req = request.Request(
            neturl, data=b'This is some datas.')  # POST 添加POST请求数据
        req = request.Request(neturl, data)  # POST 添加POST请求数据
        req = request.Request(
            neturl, data=b"This is some datas.", method="PUT")  # PUT 其他类型的请求

        # 获取
        url = req.full_url  # 获取Url
        reqtype = req.type  # 请求类型(如http)
        host = req.host  # 主机名(如:luzhuo.me / luzhuo.me:8080)
        host = req.origin_req_host  # 主机名(如:luzhuo.me)
        url = req.selector  # url路径(如:/blog/Base1.html)
        data = req.data  # 请求的实体,没有为Noce
        boolean = req.unverifiable  # 是否是RFC 2965定义的不可验证的
        method = req.get_method()  # 请求方式(如:GET / POST)
        # 修改
        # 添加请求头,键冲突将覆盖
        req.add_header(
            "User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
        req.add_unredirected_header("Key", "value")  # 添加不会重定向的请求头
        req.remove_header("Key")  # 删除请求头
        req.get_header("Key")  # 获取请求头, 无返回None
        req.get_header("Key", "None.")  # 获取请求头
        boolean = req.has_header("Key")  # 是否有该请求头
        headers = req.header_items()  # (所有)请求头列表
        req.set_proxy("220.194.55.160:3128", "http")  # 设置代理(主机,类型)
        # 下载
        filename, headers = request.urlretrieve(
            imgurl)  # 下载资源(不提供文件名不复制), 返回(文件名,头信息)元组
        filename, headers = request.urlretrieve(
            imgurl, filename="./xxx.jpg", reporthook=callback, data=None)  # reporthook下载进度回调
        request.urlcleanup()  # 清除下载的临时文件

        # - response - 请求结果
        res = request.urlopen(neturl)  # GET 打开Url,返回response
        res = request.urlopen(
            neturl, data=b'This is some datas.')  # POST 添加POST请求数据
        res = request.urlopen(req)  # 支持 Request 参数
        # 获取信息
        data = res.read().decode("utf-8")  # 读取全部数据
        data = res.readline().decode("utf-8")  # 读取行数据
        url = res.geturl()  # 获取Url
        info = res.info()  # 元信息,如头信息
        code = res.getcode()  # 状态码

        # 释放资源
        res.close

    # --- urllib.error ---
    except error.URLError as e:
        print(e)
    except error.HTTPError as e:
        # code / reason / headers 异常
        print(e)
    except error.ContentTooShortError as e:
        # 数据下载异常
        print(e)


def robot():
    # --- urllib.robotparser --- robots.txt
    rp = robotparser.RobotFileParser()
    rp.set_url("https://www.zhihu.com/robots.txt")  # 设置指向 robots.txt 文件的网址
    rp.read()  # 获取数据给解析器
    boolean = rp.can_fetch("*", "http://www.musi-cal.com/")  # 是否允许提取该url
    time = rp.mtime()  # 获取 robots.txt 的时间
    rp.modified()  # 将 robots.txt 时间设为当前时间


# 下载进度回调
def callback(datanum, datasize, filesize):  # (数据块数量 数据块大小 文件大小)
    down = 100 * datanum * datasize / filesize

    if down > 100:
        down = 100

    print("%.2f%%" % down)


if __name__ == "__main__":
    demo()
    fun()
    robot()
