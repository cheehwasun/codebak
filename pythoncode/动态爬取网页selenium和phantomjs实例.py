#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-16 19:11:52
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

#phantomjs 动态加载网页实例

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path="D:\Python27\Scripts\phantomjs.exe")
driver.set_page_load_timeout(5)
driver.set_window_size('30','80') #设置浏览器宽30，高80

try:
    driver.get('http://www.baidu.com')

    html=driver.page_source #网页源码
    driver.page_source.encode()#编码

    driver.find_element_by_id('kw')                    #通过ID定位
    driver.find_element_by_class_name('s_ipt')         #通过class属性定位
    driver.find_element_by_name('wd')                  #通过标签name属性定位
    driver.find_element_by_tag_name('input')           #通过标签属性定位
    driver.find_element_by_css_selector('#kw')         #通过css方式定位
    driver.find_element_by_xpath("//input[@id='kw']")  #通过xpath方式定位
    driver.find_element_by_link_text("贴吧")           #通过xpath方式定位
 
    driver.find_element_by_id('kw').tag_name   #获取标签的类型

    driver.save_screenshot('11.png')  # 截取全屏，并保存

except Exception as e:
    print e　　


try:
    driver.get('http://www.baidu.com')
    print driver.find_element_by_id("cp").text  # 获取元素的文本信息
    driver.find_element_by_id('kw').clear()              #用于清除输入框的内容
    driver.find_element_by_id('kw').send_keys('Hello')  #在输入框内输入Hello
    driver.find_element_by_id('su').click()              #用于点击按钮
    driver.find_element_by_id('su').submit()             #用于提交表单内容
 
except Exception as e:
    print e
