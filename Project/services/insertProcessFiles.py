from ..repository import connectDB;


def insertPF(period: str, year: int, fullPath: str):
    query = f"insert into sandbox_azulcargo.anacbr.processfiles (period,year,fullpath) values ('{period}',{year},'{fullPath}')"
    return connectDB.executeQuery(query)

def getIdProcess():
    query = f"select max(idr) idrProcess from sandbox_azulcargo.anacbr.processfiles"
    return connectDB.executeQuery(query)