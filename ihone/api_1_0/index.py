# coding:utf-8
from . import api
from ihone import db,models
from flask import current_app


# index模板

@api.route('/index')
def hello_world():
    # logging.error()
    # logging.warn()
    # logging.info()
    # logging.debug()

    # current_app.logger.error("error msg")
    # current_app.logger.warn("warn msg")
    # current_app.logger.info("info msg")
    # current_app.logger.debug("debug msg")
    return 'Hello World!'