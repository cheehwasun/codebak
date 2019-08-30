#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-19 02:32:27
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$
import tkinter

from tkinter import Tk, Scrollbar, Frame

from tkinter.ttk import Treeview


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
            self.dic1 = dict(self._filter(bs))
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
                    yield (index, [t1, t2, handicap, left, right, score, time1])
            except Exception as e:
                print(e)
                print("过滤错误")


# def saveDic(dic):
#     try:
#         with open('win007.pk', 'wb') as f:
#             pickle.dump(dic, f)

#     except Exception as e:
#         print(e)


def mkDic():
    url = 'http://live.titan007.com/'
    cap = DesiredCapabilities.PHANTOMJS.copy()
    l = random.choice(USER_AGENTS)
    cap['phantomjs.page.settings.userAgent'] = (l)
    a = scanJs(url, cap)
    a.parse()
    return a.dic1


if __name__ == '__main__':

        # 创建tkinter应用程序窗口
    root = Tk()
    # 设置窗口大小和位置
    root.geometry('1200x750+200+50')
    # 不允许改变窗口大小
    root.resizable(False, False)

    # 设置窗口标题

    root.title('盘口变化')

    # 使用Treeview组件实现表格功能

    frame = Frame(root)
    frame.place(x=0, y=10, width=1200, height=750)

    # 滚动条

    scrollBar = Scrollbar(frame)
    scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    # Treeview组件，9列，显示表头，带垂直滚动条

    tree = Treeview(frame, columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6',
                                    'c7', 'c8', 'c9'), show="headings", yscrollcommand=scrollBar.set, height=50)

    # 设置每列宽度和对齐方式
    tree.column('c1', width=100, anchor='center')
    tree.column('c2', width=100, anchor='center')
    tree.column('c3', width=200, anchor='center')
    tree.column('c4', width=200, anchor='center')
    tree.column('c5', width=100, anchor='center')
    tree.column('c6', width=100, anchor='center')
    tree.column('c7', width=100, anchor='center')
    tree.column('c8', width=100, anchor='center')
    tree.column('c9', width=100, anchor='center')

    # 设置每列表头标题文本
    tree.heading('c1', text='时间')
    tree.heading('c2', text='编号')
    tree.heading('c3', text='主队')
    tree.heading('c4', text='客队')
    tree.heading('c5', text='旧盘口')
    tree.heading('c6', text='新盘口')
    tree.heading('c7', text='水位')
    tree.heading('c8', text='比分')
    tree.heading('c9', text='比赛时间')

    tree.pack(fill=tkinter.BOTH, expand=1, pady=2)

    # Treeview组件与垂直滚动条结合

    scrollBar.config(command=tree.yview)

    # 建立爬虫字典和全局变量保存数据
    dic1 = mkDic()
    # 扫描盘口变化返回字典

    def scan():
        dic2 = mkDic()
        t1 = time.ctime().split(' ')[-2]
        l = []
        for x in dic1:
            if (dic1[x][2] != dic2[x][2]) and (dic2[x][2] != '封'):
                dic1[x][2] = dic2[x][2]
                l1 = dic2[x]
                l2 = [l1[3] + '----' + l1[4]]
                l3 = l1[:3] + l2 + l1[-2:]
                l3.insert(2, dic1[x][2])
                l3.insert(0, t1)
                l3.insert(1, x)
                l.append(l3)
        return l

    # 插入数据
    def insert_odd(l):
        if not len(l):
            return
        else:
            for x in range(len(l)):
                tree.insert('', 0, values=l[x])

            # 设置样式
            # items = tree.get_children()
            # for each in range(len(items)):
            #     print(items[each])
            #     if each % 2 == 1:
            #         tree.item(items[each], tags=('oddrow2'))
            #     else:
            #         tree.item(items[each], tags=('oddrow1'))
            # # 对标签进行设置 foreground, background, image ,font=("微软雅黑", 12, "bold")
            # tree.tag_configure('oddrow1', background='#eeeeff',
            #                    font=("微软雅黑", 10, "bold"))
            # tree.tag_configure('oddrow2', font=("微软雅黑", 10, "bold"))

    def setRow():
        try:
            odd_dic = scan()
        except Exception as e:
            print('扫描出错')
            print(e)
        try:
            insert_odd(odd_dic)
        except Exception as e:
            print('插入出错')
            print(e)
        root.after(30000, setRow)

    root.after(30000, setRow)
    # 运行程序，启动事件循环
    root.mainloop()
