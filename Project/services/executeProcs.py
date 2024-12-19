from ..repository import connectDB;


def executeProcs(procName: str, idrProcess: int):
    try:
        return connectDB.executeProc(procName,idrProcess)
    except Exception as e:
        raise e