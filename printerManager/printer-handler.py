import os
import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.options
import json

from tornado.options import define, options
define("port", default=8881, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class PrinterConfigHandler(tornado.web.RequestHandler):
    def post(self):
        # you may adjust it by the page
        data = json.loads(self.request.body)
        print data
        self.request.write('1')


if __name__ == "__main__":
    # tornado.options.parse_command_line()
    application = tornado.web.Application(
        handlers=[(r"/printerUpdate", PrinterConfigHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
        )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
