#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bottle import route, run
@route('/hello/')
def hello():
    return 'Hello World'
run(host='192.168.33.10', port=8080, debug=True, reloader=True)

