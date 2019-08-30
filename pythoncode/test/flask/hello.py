#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-25 18:35:10
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('1.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'asd' and password == '123':
        return render_template('signin-ok.html')
    return render_template('form.html', messages='Bad uuuu')


@app.route('/user/<username>')
def profile(username):
    return 'Username %s' % username


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
        # do_the_login()
    else:
        pass
        # show_login_form()



# url_for生成url
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     #不带参数的构成/login?name=asd
#     print(url_for('login', name='asd'))
#     #带参数的按照参数来/user/john Doe
#     print(url_for('profile', username='John Doe'))
if __name__ == '__main__':
    app.debug = True
    app.run()
