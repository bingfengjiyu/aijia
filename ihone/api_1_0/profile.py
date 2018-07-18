# coding:utf-8
from flask import current_app

from ihone.models import User
from ihone.utils.image_storage import storage
from ihone.utils.response_code import RET
from . import api
from ihone.utils.commons import login_required
from flask import g,request, jsonify
from ihone.constaints import QINIU_URL_DOMAIN


@api.route("/users/avatar",methods=["POST"])
@login_required
def set_user_avatar():
    # 获取参数，头像图片，用户
    user_id=g.user_id
    image_file=request.files.get("avatar")
    # 校验参数
    if image_file is None:
        return jsonify(errno=RET.PARAMERR,errmsg="未上传图像")

    # 保存用户头像
    # 读取文件内容
    image_data=image_file.read()
    try:
        # 上传到七牛服务器
        file_name=storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR,errmsg="上传头像异常")
    # 将文件名信息保存到数据库中
    try:
        User.query.filter_by(id=user_id).update({"avatar_url": image_file})
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存头像信息失败")
    # 返回值
    avatar_url=QINIU_URL_DOMAIN+file_name
    return jsonify(errno=RET.OK,errmsg="保存头像成功",data={"avatar_url":avatar_url})


