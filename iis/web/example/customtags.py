#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-01 21:20:26
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

{% load test %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>自定义tags</title>
</head>
<body>
	<h1>首先在最头部 添加 {% load test %}</h1>
	<h2>我们将test中的func改成传递参数的，如下所示：<br>
	def func(a1,a2): <br>
  		  return a1+a2 <br>
	在tp3.html中传递参数 {% func 5 3 %} <br>
	</h2>

    {% func %}
</body>
</html>
