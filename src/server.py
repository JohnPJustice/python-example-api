import tornado.ioloop
import tornado.web

class Main(tornado.web.RequestHandler):
    def get(self):
        self.write("I hate mangos!!!")

def _app():
    return tornado.web.Application([
        (r"/", Main),
    ])

if __name__ == "__main__":
    app = _app()
    app.listen(3000)
    tornado.ioloop.IOLoop.current().start()