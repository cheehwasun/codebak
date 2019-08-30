#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21 13:41:25
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$
##########
from pymongo import MongoClient
import datetime


def get_db(host='192.168.2.106', port=27017, database='test'):
    try:
        client = MongoClient(host, port)
        db = client[database]
    except Exception as e:
        print(e)
        print('连接db出错')
    return db


def get_collection(db):
    print(db.collection_names())


def add_odds(db):
    col = db.odds
    info = {'index': '1111', 'teama': '主队', 'teamb': '客队', 'changetime': datetime.datetime.today(
    ), 'handicap': '平手', 'upodds': '1.00', 'downodds': '1.00', 'score': '-', 'livetime': '0'}
    info_id = col.insert(info)
