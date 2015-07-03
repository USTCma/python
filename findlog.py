# -*- coding: UTF-8 -*-
'''
Created on 2014年11月28日

@author: rayrma
'''
import re


def getTimeResult():
    '''
    从log中获取时间
    keyTimeMonitoryFeedLayout                  整个feed排版时间
    keyTimeMonitoryFeedDraw                    绘制时间
    keyTimeMonitoryOpenActiveFeedVC            好友动态打开开始时间
    keyTimeMonitoryClickAddBtn                 加号打开开始时间      
    '''
    keyTimeMonitoryFeedLayout = 0
    keyTimeMonitoryFeedDraw   = 0                 
    keyTimeMonitoryOpenActiveFeedVC = 0
    keyTimeMonitoryClickAddBtn  = 0
    logs_object = open ('/Users/rayrma/Desktop/QQ2014-12-03.log')
    try :
        logs = logs_object.read()
    finally:
        logs_object.close()    
        if len(logs) == 0: 
            return (keyTimeMonitoryFeedLayout,keyTimeMonitoryFeedDraw,keyTimeMonitoryOpenActiveFeedVC,keyTimeMonitoryClickAddBtn)
        lines = logs.split("\n")
        for line in lines:
            if line.__contains__("keyTimeMonitoryFeedLayout"):#读取带有keyTimeMonitoryFeedLayout关键字的行
                x = re.compile(r'average\[(.*?)\]').findall(str(line))#获取average的值
                if x:
                    keyTimeMonitoryFeedLayoutList = [float(x[0])] #把所有average存入list，取最后一位list[-1]即可   
                    keyTimeMonitoryFeedLayout = float(keyTimeMonitoryFeedLayoutList[-1])
            else :
                pass                                    
        result = 'keyTimeMonitoryFeedLayout:' + str(keyTimeMonitoryFeedLayout) 
        print result          
        return result  
def line():
    '''
    从log中获取时间
    keyTimeMonitoryFeedLayout                  整个feed排版时间
    keyTimeMonitoryFeedDraw                    绘制时间
    keyTimeMonitoryOpenActiveFeedVC            好友动态打开开始时间
    keyTimeMonitoryClickAddBtn                 加号打开开始时间      
    '''
    #datalist = []
    logs_object = open ('/Users/rayrma/Desktop/2.txt')
    try :
        logs = logs_object.read()
    finally:
        logs_object.close()    
        lines = logs.split("\n")
        for line in lines:
            if line.__contains__("TimeMonitor"):#读取带有keyTimeMonitoryFeedLayout关键字的行
                x = re.compile(r'\-\[QZTimeMonitor\sendMonitor:subKey:\]\|keyTimeMonitoryFeedDraw:(.*?)$').findall(str(line))#获取average的值
                if x:
                    keyTimeMonitoryFeedLayoutList = [float(x[0])] #把所有average存入list，取最后一位list[-1]即可   
                    keyTimeMonitoryFeedLayout = float(keyTimeMonitoryFeedLayoutList[0])
            else :
                pass                                    
        result = 'keyTimeMonitoryFeedLayout:' + str(keyTimeMonitoryFeedLayout) 
        print result  
         

'''    
def write2txt():
    file_object = open("/Users/rayrma/Desktop/hello.txt","a+")
    list_of_time_resualt='timeVersion:' + str(getTimeResult())+'\n'
    file_object.writelines(list_of_time_resualt)
    file_object.close()
'''    
        

if __name__=='__main__':
    line()
