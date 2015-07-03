# -*- coding: UTF-8 -*-
'''
Created on 2014年11月28日

@author: rayrma
'''
import re

def getoldtimeVersion(): 
    oldtimeVersion=0 
    logs_object = open ("/Users/rayrma/Documents/iTimeResult/iTimeConfig.txt")
    try :
        logs = logs_object.read()
    finally:
        logs_object.close()    
    lines = logs.split("\n")
    print lines[-2]
    if lines[-2]:
        x = re.compile(r'timeVersion\[(.*?)\]').findall(str(lines[-2]))
        if x:
            oldtimeVersion = int(x[0])
        else :
            pass                                                  
    print 'oldtimeVersion:' + str(oldtimeVersion)
    return oldtimeVersion  

print getoldtimeVersion()