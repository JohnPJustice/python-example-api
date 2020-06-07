import tornado.ioloop
import tornado.web

class Main(tornado.web.RequestHandler):
    def get(self):
        self.write("I hate mangos!!!")

def first_app():
    return tornado.web.Application([
        (r"/", Main),
    ])

if __name__ == "__main__":
    app = first_app()
    app.listen(3000)
    tornado.ioloop.IOLoop.current().start()