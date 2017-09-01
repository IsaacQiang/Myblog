#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-01 22:50:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask import Blueprint

admin = Blueprint(
    'admin',
    '__name__',
    template_folder='template/admin',
    static_folder='static/admin',
    url_prefix='/admin')


@admin.route('/')
def home():
    return render_template('home.html')
