#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:15:04
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# timedemo.py 时间相关的模块演示
# 演示的模块:time(时间) / datatime(处理 日期&时间) / calendar(日历)

import time


def time_demo():
    curtime = time.time()  # 获取当前时间戳
    time_str = time.ctime(curtime)  # 转为string格式
    print(time_str)  # => Fri May  5 18:28:08 2017

    time_tup = time.localtime(curtime)  # 转为struct_time(tuple)格式
    print(time_tup.tm_year)  # => 2017


def time_func():
    '''
    time模块处理时间的相关说明:
        1. 部分系统无法处理很久之前或之后的日期和时间 (如:32系统通常时间到2038年为止)
        2. UTC (/GMT) 为格林威治标准时间 (简称:世界时间);
        3. DST 为夏令时
        4. 格式化指示符: %Y(世纪年) / %m(月[01, 12]) / %d(日[01, 31]) / %H(时[00, 23]) / %M(分[00, 59]) / %S(秒[00, 61]) / %w(星期[0, 6])
                       %b(月E缩写) %B(月E) / %a(星期E缩写) / %A(星期E) / %I(12时[01, 12]) / %c(日期+时间) / %x(日期) / %X(时间) / %p(AM/PM) / %z(时区[-23：59，+23：59]) / %%('%')
                       %j(年<-日[001, 366]) / %U(年<-星期[00, 53]) / %W(年<-周[00, 53])
        5. 星期日为一个星期周期的第一天

    '''

    # 时间戳
    time_s = time.altzone  # 夏令时与UTC的差值
    time_s = time.timezone  # (时区) 本地时间与UTC的差值
    time_s = time.time()  # 当前时间戳 (受系统时间影响) 单位:秒 ( => 1493986228.8606732 >> 1493986228s)
    time_s = time.mktime(time_tup)  # 元组转成时间
    time_s = time.monotonic()  # 单调始终的值 (不受系统时钟更新的影响) 单位:秒 ( => 250075.796 >> 250075s)
    time_s = time.perf_counter()  # (高分辨率)性能计数器 (包括睡眠时间) 单位:秒 ( => 552.1569544781966 >> 552s)



    # 元组(struct_time) [格式:(2008, 1, 1, 0, 0, 0, -1, -1, -1) >> (年, 月, 日, 时, 分, 秒, 星期, 年<-日, DST)]
    # gmtime([secs]) // 时间戳转为UTC; 0: 开始0年的时间(1970年) / 无参:UTC / time_s:转为世界时间
    time_tup = time.gmtime(time_s)
    # localtime([secs]) // 时间戳转为本地时间
    time_tup = time.localtime(time_s)
    # strptime(string[, format]) 解析时间
    time_tup = time.strptime('Tue Jan 01 00:00:00 2008', '%a %b %d %H:%M:%S %Y')  # 字符串解析成时间

    # struct_time
    time_year = time_tup.tm_year  # 从struct_time中获取数据, 其他省略



    # 字符串
    # asctime([t]) // 时间格式化 (系统样式); 不传参为当前时间
    time_str = time.asctime(time_tup)
    # ctime([secs]) // 同asctime()
    time_str = time.ctime(time_s)
    # strftime(format[, t])
    time_str = time.strftime("%Y-%m-%d-%H-%M-%S", time_tup)


    # 其他
    time.sleep(1.1)  # 线程睡眠 单位:s
    time_dst = time.daylight  # 夏令时时区(0未定义)



# ===========================================


import datetime

def datetime_demo():

    datetime_dt = datetime.datetime.today()  # 获取当前日期和时间
    datetime_str = datetime_dt.strftime("%Y/%m/%d %H:%M:%S")  # 格式化日期时间
    print(datetime_str)

    time_delta = datetime.timedelta(hours=-3)  # 时间间隔

    datetime_pre = datetime_dt + time_delta  # 将时间提前12小时
    print(datetime_pre.ctime())

    # 将日期时间转为日期
    date = datetime_dt.date()
    print("现在是 {}年 {}月 {}日".format(date.year, date.month, date.day))

    # 将日期时间转为时间
    time = datetime_dt.time()
    print("现在是 {}".format(time.isoformat()))

    # 将日期时间转为时间戳
    time_s = datetime_dt.timestamp()
    print("现在的时间戳: {}".format(time_s))



def datetime_func():
    '''
    用于处理日期和时间 
    '''

    timedelta_temp = datetime.timedelta(seconds=60, minutes=59, hours=23)
    date_temp = datetime.date.today() - datetime.timedelta(1)


    # === timedelta ===
    # 内部只存储: days日[-999999999, 999999999) / seconds秒 [0, 86399) / microseconds微秒(1E-6秒)[0, 999999)
    # milliseconds毫秒(1‰秒)[ == 1000 * microseconds ] / minutes分[ == 60 * seconds] / hours时[ == 3600 * seconds] / weeks周期[ == 7 * days]
    # timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) // 表示时间的间隔
    timedelta = datetime.timedelta(1)
    time_total = timedelta.total_seconds()  # 计算时间差的总秒数 ( => 86400.0 )

    # 计算
    boolean = timedelta == timedelta_temp  # 时间是否相等 => True
    timedelta = timedelta + timedelta_temp  # 加上 => timedelta(2)
    timedelta = timedelta - timedelta_temp  # 减去 => timedelta(0)
    timedelta = timedelta * 10  # 乘以 => timedelta(10)
    timedelta = timedelta * 0.01  # 乘以浮点数 => timedelta(0, 864)
    fnum = timedelta / timedelta_temp  # 除以 => 1.0
    timedelta = timedelta / 10  # 除以整数 或 浮点数 (不能除以0) => timedelta(0, 8640)
    num = timedelta // timedelta_temp  # 商(delta / 整数)(不能除以0) => 1
    timedelta = timedelta % timedelta_temp  # 余数 => timedelta(0)
    num, time_delta = divmod(timedelta, timedelta_temp)  # (商, 余数) => (1, datetime.timedelta(0))
    timedelta = +timedelta  # 内存地址引用(没用)
    timedelta = -timedelta  # 取反 => timedelta(-1)
    timedelta = abs(time_delta)  # 绝对值
    strs = str(time_delta)  # 格式化为[D day[s], ][H]H:MM:SS[.UUUUUU]字符串 => '1 day, 0:00:00'
    strs = repr(time_delta)  # 格式化为datetime.timedelta(D[, S[, U]])字符串 => 'datetime.timedelta(1)'



    # === date ===
    # date 可做字典的键, 所有date对象被为True
    # year年[MINYEAR, MAXYEAR] / month月[1, 12] / day日[1, 给定年月的最大天数]
    # date(year, month, day) # 公历日历中的日期, 两个方向上无限延伸
    date = datetime.date(2017, 5, 6)

    date = date.min  # 最早日期 => date(1, 1, 1)
    date = date.max  # 最晚日期 => date(9999, 12, 31)
    timedelta = date.resolution  # 不相等日期之间最小差异 (1天) => timedelta(1)

    date_year = date.year  # year年 [MINYEAR, MAXYEAR]
    date_month = date.month  # month月 [1, 12]
    date_day = date.day  # day日 [1, 给定年月的最大天数]

    date = datetime.date.today()  # 当前本地日期 (类方法) => date(2017, 5, 6)
    date = datetime.date.fromtimestamp(time.time())  # 将时间戳转为日历 (类方法) => date(2017, 5, 6)
    date = datetime.date.fromordinal(12)  # 返回公历序数日期 (类方法) => date(1, 1, 12)

    # 计算
    date = date + timedelta  # 加 => date(2017, 5, 7)
    date = date - timedelta
    timedelta = date - timedelta  # 日历相减 => timedelta(1)
    # replace(year=None, month=None, day=None)
    date = date.replace(day=12)  # 替换 => date(2017, 5, 12)

    num = date.toordinal()  # date在公历日历中的序数 (从date.min开始数)
    num = date.weekday()  # 周几 (0:周日)
    num = date.isoweekday()  # 周几 (1:周一)
    year, week, weekday = date.isocalendar()  # 返回年, 周数, 周几 (year, week, weekday) (注:weekday == isoweekday)
    date_str = date.isoformat()  # 格式化为‘YYYY-MM-DD’格式 => '2017-05-06'
    date_str = date.ctime()  # 格式化为日期格式  => 'Sat May  6 00:00:00 2017' (注:时分秒均为0, 下同)
    date_str = date.strftime("%Y-%m-%d-%H-%M-%S")  # 格式化为指定格式



    # === datetime ===
    # datetime 可做字典的键。所有datetime都为True
    # year年[MINYEAR, MAXYEAR] / month月[1, 12] / day日[1, 给定年月的最大天数] / hour时[0, 24) / minute[0. 60) / second秒[0, 60) / microsecond微秒[0, 1000000)
    # datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

    # 类方法
    date_time = datetime.datetime.today()  # 当前本地日期时间 => datetime(2017, 5, 6, 17, 51, 59, 124232)
    date_time = datetime.datetime.now()  # 同today
    date_time = datetime.datetime.utcnow()  # UTC日期和时间
    date_time = datetime.datetime.fromtimestamp(time.time())  # 时间戳转为datetime
    date_time = datetime.datetime.utcfromtimestamp(time.time())  # 时间戳转为UTCdatetime
    date_time = datetime.datetime.fromordinal(12)  # 公历序数日期
    date_time = datetime.datetime.strptime('Tue Jan 01 00:00:00 2008', '%a %b %d %H:%M:%S %Y')  # 解析

    # 实例方法
    date = date_time.date()  # 转为date => date(2017, 5, 6)
    time = date_time.time()  # 转为time => time(19, 10, 46, 149016)
    time_s = date_time.timestamp()  # 转为时间戳
    struct_time = date_time.timetuple()  # 转为 struct_time
    struct_time = date_time.utctimetuple()
    # replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]]) // 替换
    date_time = date_time.replace(year=2017)  # => datetime(2018, 5, 6, 19, 10, 46, 149016)
    num = date_time.toordinal()  # 公历序数
    num = date_time.weekday()  # 周几 (0:周日)
    num = date_time.isoweekday()  # 周几 (1:周一)
    year, week, weekday = date_time.isocalendar()  # (year, week, weekday(1:星期一))
    datetime_str = date_time.isoformat(sep='T')  # 格式化, sep时间和日期分隔符 => '2017-05-06T19:10:46.149016'
    datetime_str = date_time.ctime()  # 格式化
    datetime_str = date_time.strftime("%Y-%m-%d-%H-%M-%S")  # 格式化



    # === time ===
    # time可做字典的键, time视为True
    # Time表示一天中的本地时间,独立于任何特定的日子
    # hour时[0, 24) minute分[0, 60) second秒[0, 60) microsecond微秒[0, 1000000)
    # datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
    time = datetime.time(18, 30, 59)

    time_t = time.min  # 最早 => time(0, 0)
    time_t = time.max  # 最晚 => time(23, 59, 59, 999999)
    time_t = time.resolution  # 最小差值 => timedelta(0, 0, 1)
    num = time.hour
    num = time.minute
    mum = time.second
    mum = time.microsecond

    # replace([hour[, minute[, second[, microsecond[, tzinfo]]]]])
    time_t = time.replace(hour=17)  # 替换
    time_s = time.isoformat()  # 格式化 => '18:30:59'
    time_s = time.strftime("%H-%M-%S")  # 格式化



# ===========================================


import calendar

def calendar_demo():
    calen_text = calendar.TextCalendar()

    # 打印月历
    calen_text.prmonth(2017, 5, w=0, l=0)

    # 打印年历
    calen_text.pryear(2017, w=2, l=1, c=6, m=3)



def calendar_func():
    '''
    日历相关的操作
    默认星期一作为一周的第一天, 可设置
    '''

    # === Calendar ===
    # Calendar(firstweekday=0) // Calendar对象 firstweekday:一周的第一天,0周一(默认),6周日
    calen = calendar.Calendar()

    calen_iter = calen.iterweekdays()  # 迭代器,一周的星期数字 => 0 1 2 3 4 5 6
    calen_iter = calen.itermonthdates(2017, 5)  # 迭代器, x年x月中所有天 => 2017-05-01 2017-05-02 017-05-03 ...
    calen_iter = calen.itermonthdays2(2017, 5)  # 迭代器, x年x月中所有(日,星期) => (1, 0) (2, 1) (3, 2) ...
    calen_iter = calen.itermonthdays(2017, 5)  # 迭代器, x年x月中的所有天 => 1 2 3 ...
    calen_iter = calen.monthdatescalendar(2017, 5)  # 迭代器, x年x月中data(年,月,日)对象 => date(2017, 5, 1) date(2017, 5, 2) ...
    calen_iter = calen.monthdays2calendar(2017, 5)  # 迭代器, x年x月中(日,星期)的周列表 => [(1, 0), (2, 1) ...] [ ... ] ...
    calen_iter = calen.monthdayscalendar(2017, 5)  # 迭代器, x年x月中日的周列表 => [1,2,3 ...] [...] ...
    calen_lists = calen.yeardatescalendar(2017, width=3)  # x年所有data(年,月,日)对象的月列表
    calen_lists = calen.yeardays2calendar(2017, width=3)  # x年所有(日,星期)的月列表
    calen_lists = calen.yeardayscalendar(2017, width=3)  # x年所有日的月列表


    # === TextCalendar ===
    # TextCalendar(firstweekday=0) // 纯文本的日历
    calen_text = calendar.TextCalendar()

    calen_str = calen_text.formatmonth(2017, 5, w=0, l=0)  # x年x月所有日
    calen_text.prmonth(2017, 5, w=0, l=0)  # (打印) x年x月所有日
    calen_str = calen_text.formatyear(2017, w=2, l=1, c=6, m=3)  # x年所有日
    calen_text.pryear(2017, w=2, l=1, c=6, m=3)  # (打印) x年所有日


    # === HTMLCalendar ===
    # HTMLCalendar(firstweekday=0) // HTML的日历
    calen_html = calendar.HTMLCalendar()

    calen_str = calen_html.formatmonth(2017, 5, withyear=True)  # x年x月的所有日
    calen_str = calen_html.formatyear(2017, width=3)  # x年所有日
    calen_str = calen_html.formatyearpage(2017, width=3, css='calendar.css', encoding=None)  # (完整编码) x年所有日


    # === calendar 模块的函数 ===
    calendar.setfirstweekday(calendar.SUNDAY)  # 设置每周开始的工作日(默认:0周一,6周日),如设置星期天为第一个工作日(calendar.SUNDAY) 参数:MONDAY / TUESDAY / WEDNESDAY / THURSDAY / FRIDAY / SATURDAY / SUNDAY
    num = calendar.firstweekday()  # 返回每周的第一天的星期
    boolean = calendar.isleap(2017)  # x年是否为闰年
    num = calendar.leapdays(2010, 2020)  # x年到y年的闰年数
    num = calendar.weekday(2017, 5, 6)  # x年x月x日的星期几
    strs = calendar.weekheader(1)  # 星期E名, 1为名字长度
    weekday, days = calendar.monthrange(2017, 5)  # x年x月 (星期, 月天数)
    calen_lists = calendar.monthcalendar(2017, 5)  # x年x月的月历
    calen_lists = calendar.prmonth(2017, 5, w=0, l=0)  # x年x月的日历
    calen_strs = calendar.month(2017, 5, w=0, l=0)  # 月历
    calendar.prcal(2017, w=0, l=0, c=6, m=3)  # (打印) 整年日历
    calen_strs = calendar.calendar(2017, w=2, l=1, c=6, m=3)  # 整年日历
    time_s = calendar.timegm(time.gmtime(time.time()))  # 时间元组 转为 时间戳

    calen_iter = calendar.day_name  # 迭代器, 星期E名称
    calen_iter = calendar.day_abbr  # 迭代器, 星期E缩写名称
    calen_iter = calendar.month_name  # 迭代器, 月E名称
    calen_iter = calendar.month_abbr  # 迭代器, 月E缩写名称



if __name__ == "__main__":
    time_demo()
    datetime_demo()
    calendar_demo()

    # time_func()
    # datetime_func()
    # calendar_func()
