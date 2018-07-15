#coding:utf-8
from flask import current_app, jsonify
from flask import make_response

from ihone import redis_store, constaints
from ihone.utils.captcha.captcha import captcha
from ihone.utils.response_code import RET
from . import api


# 图片验证码模块

@api.route("/image_codes/<image_code_id>")
def get_image_code(image_code_id):
    # 获取参数
    # 校验参数
    # 业务处理
    # 生成验证码图片
    # 名字,验证码真实值,图片的二进制内容
    name,text,image_data=captcha.generate_captcha()
    try:
        # 保存验证码真实值和编号
        # redis_store.set("image_code_%s" % image_code_id,text)
        # redis_store.expires("image_code_%s" % image_code_id, constaints.IMAGE_CODE_EXPIRES)

        redis_store.setex("image_code_%s" % image_code_id,constaints.IMAGE_CODE_EXPIRES,text)

    except Exception as e:
        current_app.logger.error(e)
        resp={
            "errno":RET.DBERR,
            "errmsg":"false"
        }
        return jsonify(resp)

    resp=make_response(image_data)
    resp.headers["Content-Type"] = "image/jpg"
    # 返回值
    return resp

