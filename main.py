import pandas as pd
from Project.business import listProcess
from Project.business import rawDims
from Project.services import rawInsert

# dataframes com informação segmentada. 
listFiles = listProcess.processFile()
df = listProcess.anacFile(listFiles)
dfCompany,dfDigitIndent,dfTypeLine,dfPlane,dfAirports = rawDims.rawDims(df)

rawsDims = {'rawCompany': dfCompany,'rawTypeLine': dfTypeLine,'rawPlane': dfPlane,'rawAirports': dfAirports,'rawDigitIndent': dfDigitIndent}

for tableName, dfInser in rawsDims.items():
    rawInsert.insertRaws(tableName, dfInser)