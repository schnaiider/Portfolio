import pandas as pd
from datetime import date
from ..repository import connectDB;


def insertRaws(tableName: str, dfInser: list, idrProcess: int):
    dfInser['IDRPROCESS'] = idrProcess
    connectDB.blkInsert(tableName, dfInser)

def closeConn():
    connectDB.closeConnection()

