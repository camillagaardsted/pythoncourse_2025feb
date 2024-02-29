# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:32:06 2024

@author: Camilla

You can run this script with default values
or you can specify cmd line arguments for foldername,fileformat and intervalInSeconds

e.g. python collect_data.py c:\temp json 15

"""

import psutil # for data collecting
import datetime
import os
import json
import sys

foldername=r'C:\pythoncourse'
fileformat='csv'
intervalInSeconds=10

if not os.path.exists(foldername):
    os.mkdir(foldername)

# only use cmd line parameters if there are four
if len(sys.argv)==4:
    scriptpath = sys.argv[0] # this will always be the script path - we don't use it to anything here - just to show it is there in sys.argv
    foldername=sys.argv[1]
    fileformat=sys.argv[2]
    intervalInSeconds=int(sys.argv[3])

sep=";"
columns=['timestamp','cpu_usage','ram_usage']  

def collectData(intervalInSeconds,fileformat):     
    startTime = datetime.datetime.now()
    currentTime=datetime.datetime.now()    
    localdataList=[]
    while currentTime - startTime < datetime.timedelta(seconds=intervalInSeconds):    
        now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")    
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent                
        if fileformat=='json':
            dictItem = {columns[0]:now
                        ,columns[1]:cpu_usage
                        ,columns[2]:ram_usage
                    }
            print(dictItem)
            localdataList.append(dictItem)
        elif fileformat=='csv':    
            csvdata=f"{now}{sep}{cpu_usage}{sep}{ram_usage}\n"
            print(csvdata)
            localdataList.append(csvdata)
        else:
            print(fileformat,'fileformat not supported')        
        currentTime=datetime.datetime.now()
    return localdataList

def createcsvfile(csvdataList):
    currentTime=datetime.datetime.now()
    filename=os.path.join(foldername,f"datafile_{currentTime:%Y_%m_%d_%H_%M_%S}.csv")    
    with open(filename,'w',encoding='utf-8') as datafile:
        print(f'Creating file with filename {filename}')
        datafile.write(sep.join(columns))
        datafile.write("\n")
        datafile.writelines(csvdataList)

def createjsonfile(jsondataList):
    currentTime=datetime.datetime.now()
    # json dump        
    filename=os.path.join(foldername,f"datafile_{currentTime:%Y_%m_%d_%H_%M_%S}.json") 
    # Convert and write JSON object to file
    with open(filename, "w") as outfile:
        print(f'Creating file with filename {filename}')
        json.dump(jsondataList, outfile)


while True:    
    dataList=collectData(intervalInSeconds,fileformat)
    if fileformat=='csv':        
        createcsvfile(dataList)
    elif fileformat=='json':
        createjsonfile(dataList)
    else:
        print(fileformat,'Fileformat not supported!')
        break
