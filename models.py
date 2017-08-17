#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-02 18:10:22
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask.ext.sqlalchemy import SQLAlchemy             
from main import app


# INIT the sqlalchemy object                            
# Will be load the SQLALCHEMY_DATABASE_URL from config.py
# SQLAlchemy 会自动的从 app 对象中的 DevConfig 中加载连接数据库的配置项
db = SQLAlchemy(app)

class User(db.Model):
    """Represents Proected users."""

    # Set the name for table
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # Establish contact with Post's ForeignKey: user_id
    posts = db.relationship(
        'Post',
        backref='users',
        lazy='dynamic')
    def __init__(self, id, username, password):
        self.username = username
        self.id = id
        self.password = password

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.username)

#Many to many
posts_tags = db.Table('posts_tags',
    db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
    db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))

class Post(db.Model):
    """Represents Proected posts."""

    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # Set the foreign key for Post
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))
    # Establish contact with Comment's ForeignKey:post_id
    comments = db.relationship(
        'Comment',
        backref='posts',
        lazy='dynamic')
    #many = many:posts <==> tags
    tags = db.relationship(
        'Tag',
        secondary=posts_tags,
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, id, title):
        self.title = title
        self.id = id
    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)

class Tag(db.Model):
    """Represents Proected tags."""

    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name, id):
        self.name = name
        self.id = id
    def __repr__(self):
        return "<Model Tag `{}`>".format(self.name)

class Comment(db.Model):
    """Represents Proected comments."""

    __tablename__ = 'comments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, id, name):
        self.name = name
        self.id = id

    def __repr__(self):
        return '<Model Comment `{}`>'.format(self.name)