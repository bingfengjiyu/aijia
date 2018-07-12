#coding:utf-8
from logging.handlers import RotatingFileHandler

import redis
import logging
from flask import Flask
from config import config_dict
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session


from utils.commons import RegexConverter

# 构建数据库对象
db=SQLAlchemy()


redis_store=None

csrf=CSRFProtect()


# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=40, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)

# 工厂模式
def create_app(config_name):
    app = Flask(__name__)
    conf=config_dict[config_name]
    app.config.from_object(conf)

    # 初始化数据库db
    db.init_app(app)

    global redis_store
    redis_store = redis.StrictRedis(host=conf.REDIS_HOST, port=conf.REDIS_PORT)
    # 初始化
    csrf.init_app(app)

    Session(app)
    app.url_map.converters['re']=RegexConverter

    import api_1_0

    app.register_blueprint(api_1_0.api,url_prefix="/api/v1_0")

    from ihone.web_html import html

    app.register_blueprint(html)


    return app

