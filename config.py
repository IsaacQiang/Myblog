#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-02 15:43:25
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

class Config(object):
    """Base config class."""
    pass
    SECRET_KEY = '0d16c0ab1c3193963b4223daa8702636'
class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/blog'