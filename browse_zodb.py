import pdb
import sys

from ZODB import DB
from ZODB.FileStorage import FileStorage

fs = sys.argv[1]
storage = FileStorage(fs)

db = DB(storage)
connection = db.open()
root = connection.root()

app_root = root["gulliver"]

# fsi = storage.iterator()
pdb.set_trace()
