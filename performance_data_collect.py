# -*- coding: utf-8 -*-

# https://pypi.org/project/psutil/
import psutil # for data collecting
import datetime
import time 
import os
import json
import sys 

# these are the default values
foldername='C:\pythoncourse\data'
intervalInSeconds=20
fileformat='csv'

if len(sys.argv)>3:
    # Remember zero element in argv is just the full script file name path
    foldername=sys.argv[1]
    intervalInSeconds=int(sys.argv[2])
    fileformat=sys.argv[3]

columns=['timestamp','cpu_usage','ram_usage']
sep=";"

while True:
    
    startTime = datetime.datetime.now()
    currentTime=datetime.datetime.now()
    dictdataList = []
    csvdataList=[]
    while currentTime - startTime < datetime.timedelta(seconds=intervalInSeconds):    
        now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        dictItem = {columns[0]:now
                    ,columns[1]:cpu_usage
                    ,columns[2]:ram_usage
                   }
        print(dictItem)
        dictdataList.append(dictItem)
        csvdata=f"{now}{sep}{cpu_usage}{sep}{ram_usage}\n"
        csvdataList.append(csvdata)
        currentTime=datetime.datetime.now()
    
    if fileformat == 'csv':    
        filename=os.path.join(foldername,f"datafile_{currentTime:%Y_%m_%d_%H_%M_%S}.csv")    
        with open(filename,'w',encoding='utf-8') as datafile:
            print(f'Creating file with filename {filename}')
            datafile.write(sep.join(columns))
            datafile.write("\n")
            datafile.writelines(csvdataList)
    elif fileformat=='json':                
        # json dump        
        filename=os.path.join(foldername,f"datafile_{currentTime:%Y_%m_%d_%H_%M_%S}.json") 
        # Convert and write JSON object to file
        with open(filename, "w") as outfile:
            print(f'Creating file with filename {filename}')
            json.dump(dictdataList, outfile)
    else:
        print('File format is not supported - we only print the values here!!!')