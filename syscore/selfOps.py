
import sqlite3


class selfOps(sqlite3):

   NAME: str = "self"

   def __init__(self):
      pass

   def imprint(self, data: str) -> str:
      try:
         path: str = f"_self/data/{selfOps.NAME}.db"
         conn = self.connect(path)
         return data
      except Exception as e:
         print(e)
