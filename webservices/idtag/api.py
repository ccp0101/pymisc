import tornado.gen
import tornado.httpclient
import urllib

"""
http://zhaoren.idtag.cn/zhaoren_app/searchName!statisticsList.htm?name=
http://zhaoren.idtag.cn/samename/searchName!statisticsReport2.htm?name=NAME
Provinces http://zhaoren.idtag.cn/samename/searchName!getProvinces.htm?name=NAME
Sex http://zhaoren.idtag.cn/samename/searchName!statisticsReport1.htm?selectType=2&name=NAME&total=3466&birthday=
Ages http://zhaoren.idtag.cn/samename/searchName!statisticsReport1.htm?selectType=1&name=NAME&total=3466&birthday=
星座 http://zhaoren.idtag.cn/samename/searchName!statisticsReport1.htm?selectType=3&name=NAME&total=3466&birthday=
生肖 http://zhaoren.idtag.cn/samename/searchName!statisticsReport1.htm?selectType=4&name=NAME&total=3466&birthday=
Birthday http://zhaoren.idtag.cn/samename/searchName!sameBirth.htm?birth=0000-01-01&name=NAME
http://zhaoren.idtag.cn/samename/searchName!sameBirth.htm?birth=1995-01-01&name=NAME&sameYear=true
"""

class IDTagWebService(object):
    def __init__(self, *args, **kwargs):
        self.options = kwargs

    @tornado.gen.engine
    def getNumberOfIdenticalNames(self, name, callback):
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch,
            "http://zhaoren.idtag.cn/zhaoren_app/searchName!statisticsList.htm?name=" +
            urllib.quote(name))

        # if response.error
