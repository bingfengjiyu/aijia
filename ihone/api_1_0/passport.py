# coding:utf-8
import re

from flask import current_app
from flask import request, jsonify,session

from ihone.utils.response_code import RET
from . import api
from ihone import redis_store, db
from ihone.models import User





@api.route("/users",methods=["POST"])
def register():
    # 以json数据发过来
    # request.get_json()方法能够将请求体的json数据转换为字典
    req_dict=request.get_json()
    mobile=req_dict.get("mobile")
    sms_code=req_dict.get("sms_code")
    password=req_dict.get("password")

    if not all([mobile,sms_code,password]):
        resp={
            "errno":RET.PARAMERR,
            "errmsg":"参数不完整"
        }

        return jsonify(resp)


    if not re.match(r'1[34578]\d{9}',mobile):
        resp={
            "errno": RET.DATAERR,
            "errmsg": "手机格式错误"
        }

        return jsonify(resp)

    try:
        real_sms_code=redis_store.get("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)
        resp={
            "errno": RET.DBERR,
            "errmsg": "查询短信验证码错误"
        }
        return jsonify(resp)

    if real_sms_code is None:
        resp = {
            "errno": RET.NODATA,
            "errmsg": "短信验证码过期"
        }
        return jsonify(resp)

    if real_sms_code!=sms_code:
        resp = {
            "errno": RET.DATAERR,
            "errmsg": "短信验证码错误"
        }
        return jsonify(resp)

    try:
        redis_store.delete("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)


    # try:
    #     user=User.query.filter_by(mobile=mobile).first()
    # except Exception as e:
    #     current_app.logger.error(e)
    #     resp = {
    #         "errno": RET.DBERR,
    #         "errmsg": "数据库异常"
    #     }
    #     return jsonify(resp)
    # if user is not None:
    #     resp = {
    #         "errno": RET.DATAEXIST,
    #         "errmsg": "手机号已经注册"
    #     }
    #     return jsonify(resp)

    user=User(name=mobile,mobile=mobile)
    # 对于password属性的设置，会调用属性方法，进行加密
    user.password=password
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        resp = {
            "errno": RET.DATAEXIST,
            "errmsg": "手机号已经注册"
        }
        return jsonify(resp)

    session["user_id"]=user.id
    session["user_name"]=mobile
    session["mobile"]=mobile

    resp = {
        "errno": RET.OK,
        "errmsg": "注册成功"
    }
    return jsonify(resp)