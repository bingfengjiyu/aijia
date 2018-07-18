# coding:utf-8
from flask import current_app, jsonify
from flask import json
from flask import request
from datetime import datetime

from ihone.utils.response_code import RET
from . import api
from ihone.models import Area, House
from ihone import redis_store


# @api.route("/areas")
# def get_area_info():
#     # 查询数据库，获取城区信息
#     try:
#         areas_llist=Area.query.all()
#
#     except Exception as e:
#         current_app.logger.error(e)
#         areas_json=None
#     if areas_json in None:
#         try:
#            areas_llist
#         except
#         return jsonify(error=RET.DBERR,errmsg="查询城区信息异常")
#     # 遍历列表，处理每个对象，转换一下对象的属性名
#     areas=[]
#     for area in areas_llist:
#         areas.append(area.to_dict())
#
#     # 将数据转换成json
#
#     areas_json=json.dumps(areas)
#     # 将数据在redis当中保存一份缓存
#     try:
#         redis_store.set("area_info",areas_json)
#     except Exception as e:
#         current_app.logger.error(e)
#
#     return jsonify(errno=RET.OK,errmsg="查询城区信息成功",data={"areas":areas})




@api.route("/houses",methods=["GET"])
def get_house_list():
    start_date_str=request.args.get("sd","")
    end_date_str=request.args.get("ed","")
    area_id=request.args.get("aid","")
    sort_key=request.args.get("sk","new")
    page=request.args.get("p",1)

    try:
        start_date=None
        if start_date_str:
            start_date=datetime.strptime(start_date_str,"%Y-%m-%d")
        end_date=None
        if end_date_str:
            end_date=datetime.strptime(end_date_str,"%Y-%m-%d")
        if start_date and end_date:
            assert start_date<=end_date
    except Exception as e:
        return jsonify(errno=RET.PARAMERR,errmsg="日期参数有误")

    # 判断页数
    try:
        page=int(page)
    except Exception:
        page=1

    # 查询数据
    House.query.filter().order_by()





