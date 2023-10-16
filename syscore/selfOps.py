
import typing as t
import os.path, sqlite3
import uuid
# -- system --
from syscore.systypes import *


HOME_PATH: str = "/home/erik"
DATA_PATH: str = f"{HOME_PATH}/proxyme/_self/data"


class selfOps(object):

   def __init__(self):
      self.path: str = f"{DATA_PATH}/self.db"
      self.conn: sqlite3.Connection = t.Any

   def init(self):
      if not os.path.exists(self.path):
         cwd: str = os.getcwd()
         raise FileNotFoundError(self.path)
      # -- -- -- --
      self.conn: sqlite3.Connection = sqlite3.connect(self.path)

   def imprint(self, _type: str, data: str) -> [sysCode, None | str]:
      try:
         guid = uuid.uuid4().hex
         qry: str = (f"insert into patterns_in values('{guid}',"
            f" datetime('now'), '{_type}', '{data}');")
         cur: sqlite3.Cursor = self.conn.cursor()
         res = cur.execute(qry)
         if res.rowcount != 1:
            pass
         # -- -- -- --
         self.conn.commit()
         # -- -- -- --
         return sysCode.OK, None
      except Exception as e:
         return sysCode.ERROR, str(e)
      finally:
         pass

   def process(self):
      pass
