# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
import json

import os

#setting port number
define("port", default=10000, help="run on the given port", type=int)

# 結果格納用の配列
vrList = []
acList = []
zatsuList = []

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("welcome to tornado")
        self.finish()
    def post(self):
        # print(self.request)
        data = json.loads(self.request.body)
        print(data)
        res = {
            'statusCode' : "200"
        }
        self.set_header("Content-Type","application/json")
        self.write(json.dumps(res))
        self.finish()

# 音声認識
class VrResultHandler(tornado.web.RequestHandler):
    def post(self):
        # print(self.request)
        data = json.loads(self.request.body)
        vrList.append(data["VRResult"])
        print(vrList)
        res = {
            'statusCode' : "200"
        }
        self.set_header("Content-Type","application/json")
        self.write(json.dumps(res))
        self.finish()

# 加速度
class AcResultHandler(tornado.web.RequestHandler):
    def post(self):
        # print(self.request)
        data = json.loads(self.request.body)
        # result.append(data["X"])
        acList.append(data["Y"])
        # result.append(data["Z"])
        print(acList)
        res = {
            'statusCode' : "200"
        }
        self.set_header("Content-Type","application/json")
        self.write(json.dumps(res))
        self.finish()

# 雑談
class ZatsuHandler(tornado.web.RequestHandler):
    def post(self):
        # print(self.request)
        data = json.loads(self.request.body)
        zatsuList.append(data["zatsu"])
        print(zatsuList)
        res = {
            'statusCode' : "200"
        }
        self.set_header("Content-Type","application/json")
        self.write(json.dumps(res))
        self.finish()

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/vrresult', VrResultHandler),
            (r'/acresult', AcResultHandler),
            (r'/zatsu', ZatsuHandler)
        ]
        template_path = os.path.join(os.path.dirname(__file__), "templates")
        static_path = os.path.join(os.path.dirname(__file__), "static")
        tornado.web.Application.__init__(
            self,
            handlers,
            debug=True,
            template_path=template_path,
            static_path=static_path,
            cookie_secret='development secret key',
        )


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
