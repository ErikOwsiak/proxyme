
from flask import Flask
import toml


with open("config.toml", "r") as f:
   buff: str = f.read()
CONF = toml.loads(buff)


__app__ = Flask(CONF["app"]["name"])


@__app__.route("/")
def index():
   return "<p>Hello, World!</p>"


class app(object):

   def __init__(self):
      self.hostbind = CONF["net"]["hostbind"]
      self.hostport: int = int(CONF["net"]["port"])

   def start(self):
      __app__.run(host=self.hostbind, port=self.hostport)

