#coding:utf-8

from flask import session, jsonify,g
from werkzeug.routing import BaseConverter
from functools import wraps

# 自定义路由器
from ihone.utils.response_code import RET


class RegexConverter(BaseConverter):
    def __init__(self,url_map,regex):
        super(RegexConverter,self).__init__(url_map)
        self.regex=regex



def login_required(view_func):
    """检验用户的登陆状态"""
    # 让装饰器的名字和注释文档不改变，装饰圈都需要加上@wraps
    @wraps(view_func)
    def wrapper(*args,**kwargs):
        user_id=session.get("user_id")
        if user_id is not None:
            g.user_id=user_id
            return view_func(*args,**kwargs)
        else:
            resp={
                "errno":RET.SESSIONERR,
                "errmsg":"用户未登录"
            }
            return jsonify(resp)
    return wrapper




