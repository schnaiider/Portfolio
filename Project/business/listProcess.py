import pandas as pd
from Project.services import readCFG as cfg
from Project.models import file
from datetime import date
from dateutil.relativedelta import relativedelta
from Project.services import readFile as read


config = cfg.readCFG()

def processFile():
    
    listProcessFiles = []
    listProcessFiles.append(file.file(
                            urlBase = config['pathBasicAnac']['url']
                            ,period = date.today().strftime("%Y-%m")
                            ,year = date.today().strftime("%Y")
                            ,fullPath = config['pathBasicAnac']['url'] +  date.today().strftime("%Y") +'/basica'+ date.today().strftime("%Y-%m") + '.zip')
    )
    listProcessFiles.append(file.file(
                            urlBase = config['pathBasicAnac']['url']
                            ,period = (date.today() + relativedelta(months=-1)).strftime("%Y-%m")
                            ,year = (date.today() + relativedelta(months=-1)).strftime("%Y")
                            ,fullPath = config['pathBasicAnac']['url'] + (date.today() + relativedelta(months=-1)).strftime("%Y") +'/basica'+ (date.today() + relativedelta(months=-1)).strftime("%Y-%m") + '.zip')
    )
    listProcessFiles.append(file.file(
                            urlBase = config['pathBasicAnac']['url']
                            ,period = (date.today() + relativedelta(months=-2)).strftime("%Y-%m")
                            ,year = (date.today() + relativedelta(months=-2)).strftime("%Y")
                            ,fullPath = config['pathBasicAnac']['url'] + (date.today() + relativedelta(months=-2)).strftime("%Y") +'/basica'+ (date.today() + relativedelta(months=-2)).strftime("%Y-%m") + '.zip')
    )
    return listProcessFiles

def anacFile(listProcessFiles):
    for files in listProcessFiles:
        df = read.readFileZip(files.fullPath, f"basica_{files.period}.zip",config['SaveAs']['saveAsPath'],';','"','latin1')
        if df is not None and not df.empty:
            return df,files.fullPath,files.period,files.year