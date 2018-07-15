# coding:utf-8
import redis


class Config():
    SECRET_KEY = "klhdfh31yklsafhhf"
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python02"
    # 追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask_session用到的配置信息
    SESSION_TYPE = "redis"
    # 让cookie中的session_id增加签名加密处理
    SESSION_USE_SIGNER = True
    # 创建StrictRedis对象，与redis服务器建⽴连接
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # session的有效期,单位是秒
    PERMANENT_SESSION_LIFETIME = 86400


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


config_dict={
    "develop":DevelopmentConfig,
    "product":ProductionConfig
}
