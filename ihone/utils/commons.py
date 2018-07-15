#coding:utf-8


from werkzeug.routing import BaseConverter

# 自定义路由器
class RegexConverter(BaseConverter):
    def __init__(self,url_map,regex):
        super(RegexConverter,self).__init__(url_map)
        self.regex=regex


