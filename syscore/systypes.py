
import enum


class httpMethod(enum.IntEnum):
   POST = 0
   GET = 1
   PUT = 2


class sysCode(enum.IntEnum):
   OK = 0
   ERROR = 1000
