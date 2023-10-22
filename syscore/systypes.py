
import enum


class httpMethod(enum.IntEnum):
   POST = 0
   GET = 1
   PUT = 2


class httpVerb(object):
   POST = "POST"
   GET = "GET"
   PUT = "PUT"


class sysCode(enum.IntEnum):
   OK = 0
   ERROR = 1000
