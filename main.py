import pandas as pd
from Project.business import listProcess,rawDims
from Project.services import rawInsert,executeProcs,insertProcessFiles

# dataframes com informação segmentada. 
listFiles = listProcess.processFile()
df,fullPath,period,year = listProcess.anacFile(listFiles)

# insert de dados para seguimento da carga
insertProcessFiles.insertPF(period,year,fullPath)
idrProcess = insertProcessFiles.getIdProcess()[0][0]
# Separa o arquivo para criar as dims aw
dfCompany,dfDigitIndent,dfTypeLine,dfPlane,dfAirports = rawDims.rawDims(df)
rawsDims = {'rawCompany': dfCompany,'rawTypeLine': dfTypeLine,'rawPlane': dfPlane,'rawAirports': dfAirports,'rawDigitIndent': dfDigitIndent}
for tableName, dfInser in rawsDims.items():
    rawInsert.insertRaws(tableName, dfInser, idrProcess)

# Executa procs para tratar as dimns final 
execProcs = ["DIMAIRPORTS"]
for procName in execProcs:
    status = executeProcs.executeProcs(procName, idrProcess)
    

# for proc, dimProcess in execProcs.items():
#     rawInsert.insertRaws(dimProcess)

rawInsert.closeConn()