#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-19 14:57:09
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-16 23:13:59
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pickle
import time
import random
import os
import datetime
import pymongo

# cap=DesiredCapabilities.PHANTOMJS.copy()
# cap['phantomjs.page.settings.userAgent']=("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
]


class scanJs(object):
    def __init__(self, url, cap=DesiredCapabilities.PHANTOMJS):

        self.url = url
        self.cap = cap

    def _getJs(self):
        driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
        driver.set_window_size('30', '30')
        driver.set_page_load_timeout(10)
        try:
            driver.get(self.url)
            self.html = driver.page_source
            driver.quit()
            return True
        except Exception as e:
            print(e)
            return False

    def parse(self):
        if self._getJs():
            bs = BeautifulSoup(self.html, 'lxml')
            self.ldic = self._filter(bs)
        else:
            print('网络异常')

    def _filter(self, bs):
        self.l1 = bs.select('tr[odds]')
        for each in bs.select('tr[odds]'):
            try:
                odd = each.attrs['odds'].split(',')
                if odd[0]:
                    t1 = each.select('a[id^=team1]')[0].string
                    t2 = each.select('a[id^="team2"]')[0].string
                    time1 = each.select('td.td_status')[0].get_text()
                    score = each.select('td[class^=td_score]')[0].string
                    handicap = each.select('td[id^=pk_] div')[
                        0].get_text().split('*')[-1]
                    index = odd[0]
                    left = odd[3]
                    right = odd[4]
                    changetime = datetime.datetime.today()
                    z1 = ['index', '变化时间', '主队', '客队',
                          '盘口', '水位', '比分', '比赛时间']
                    z2 = [index, changetime, t1, t2, handicap,
                          left + '---' + right, score, time1]
                    yield dict(zip(z1, z2))
            except Exception as e:
                print(e)
                print("过滤错误")


def mk_ldic():
    url = 'http://live.titan007.com/'
    cap = DesiredCapabilities.PHANTOMJS.copy()
    l = random.choice(USER_AGENTS)
    cap['phantomjs.page.settings.userAgent'] = (l)
    a = scanJs(url, cap)
    a.parse()
    return a.ldic


def get_db(host='192.168.2.106', port=27017, database='test'):
    try:
        client = pymongo.MongoClient(host, port)
        db = client[database]
    except Exception as e:
        print(e)
        print('连接db出错')
    return db


def init_db():
    try:
        db = get_db()
        db.t1.remove()
        db.t2.remove()
        ldic = mk_ldic()
        for each in ldic:
            db.t1.insert(each)

    except Exception as e:
        print(e)
        print('数据初始错误')


def cmp():
    try:
        db = get_db()
    except:
        print('获取数据库链接失败')
    ldic = mk_ldic()
    for each in ldic:
        f1 = db.t1.find({'index': dic['index']})
        if not f1.count():
            db.t1.insert(dic)
        else:
            f = db.t1.find(
                {'$and': [{'index': each['index']}, {'盘口': {'$eq': each['盘口']}}]})
            if not f.count():
                db.t2.update({'index': each['index']}, {'$set': each}, True)
                each.pop('_id', -1)
                db.t1.update({'index': each['index']}, {'$set': each}, True)


if __name__ == '__main__':
    time1 = time.time()

    init_db()
    time.sleep(60)
    cmp()

    time2 = time.time()
    print('扫描用时：%f\t秒' % (time2 - time1))
