#coding:utf-8
import redis
from flask import Flask
from config import config_dict
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session


# 构建数据库对象
db=SQLAlchemy()


redis_store=None

csrf=CSRFProtect()


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
    import api_1_0

    app.register_blueprint(api_1_0.api,url_prefix="/api/v1_0")


    return app

