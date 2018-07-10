# coding:utf-8
from . import api
from ihone import db


@api.route('/index')
def hello_world():
    return 'Hello World!'