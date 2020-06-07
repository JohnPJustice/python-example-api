from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json 

names = []

class NameList(RequestHandler):
  def get(self):
    self.write({'names': names})


class Name(RequestHandler):
  def post(self):
    names.append(self.request.body)
    self.write({'message': self.request.body})

def make_app():
  urls = [
    ("/", NameList),
    ("/api/name/", Name)
  ]
  return Application(urls, debug=True)
  
if __name__ == '__main__':
  app = make_app()
  app.listen(3000)
  IOLoop.instance().start()