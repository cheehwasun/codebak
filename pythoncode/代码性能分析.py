#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-07 15:50:27
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

#性能分析
import cProfile  
import pstats


# 分析某条语句：
#c_Markov = c_MarkovCreater(savefilename)  
cProfile.run("<strong>c_Markov = c_MarkovCreater(savefilename)</strong>","result")  
p = pstats.Stats("result")  
p.strip_dirs().sort_stats(-1).print_stats() 

# 整段分析

if  __name__ == '__main__' :  
    import cProfile, pstats, StringIO  
    pr = cProfile.Profile()  
    pr.enable()  

    #代码

    pr.disable()  
    s = StringIO.StringIO()  
    sortby = 'cumulative'  
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)  
    ps.print_stats()  
    print s.getvalue()  