#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-08 16:29:52
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

import sys
import time
j = '#'
space = ' ' * 50
if __name__ == '__main__':
    for i in range(100):
        p = int((i / 100) * 100)
        j = '#' * int(p / 2)
        space = ' ' * int(50 - (p / 2))
        sys.stdout.write(str(p) + '%  ||' + j + space + '||' + "\r")
        sys.stdout.flush()
        time.sleep(0.01)
