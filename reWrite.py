# -*- coding: utf-8 -*-
'''
修改文件代码

Created on 2014年12月23日

@author: rayrma
'''
#打开耗时监控开关
def reWriteTimeMonitorTurnOn(codefilepath):
    lines = open(codefilepath).readlines()
    open(codefilepath).close()
    output  = open(codefilepath,'w');
    for line in lines:
        if not line:
            break
        if '' in line:
            date ='        QZONE_LOG_EVENT(QZONE_MODULE_TIME_MONITOR, "%s:%.3f", [mainKey UTF8String], time);'
            output.write(date)           
        else:  
            output.write(line)
    output.close()
    print"successful"

#修改log格式
def reWriteLog(codefilepath):
    lines = open(codefilepath).readlines()
    open(codefilepath).close()
    output  = open(codefilepath,'w');
    for line in lines:
        if not line:
            break
        if '%.4d-%.2d-%.2d %.2d:%.2d:%.2d.%.3ld ' in line:
            date ='    fprintf(fileHandle, "%.4d-%.2d-%.2d %.2d:%.2d:%.2d.%.3ld|%s|%d|%05d|%s:%d|%s|%s|%s\n",'
            output.write(date)
        else:  
            output.write(line)
    output.close()
    print"successful"
 
#修改Qzone耗时监控log格式    
def reWriteTimeMonitor(codefilepath):
    lines = open(codefilepath).readlines()
    open(codefilepath).close()
    output  = open(codefilepath,'w');
    for line in lines:
        if not line:
            break
        if 'QZONE_LOG_EVENT(QZONE_MODULE_TIME_MONITOR, "%s %s [%s] duration[%.3f]", [indexPathString UTF8String], [mainKey UTF8String], [subKey UTF8String], time);' in line:
            date ='        QZONE_LOG_EVENT(QZONE_MODULE_TIME_MONITOR, "%s:%.3f", [mainKey UTF8String], time);'
            output.write(date)
        elif 'QZONE_LOG_EVENT(QZONE_MODULE_TIME_MONITOR, "%s %s duration[%.3f] average[%.3f] total[%.3f] count[%d] [%s]",' in line:
            date ='        QZONE_LOG_EVENT(QZONE_MODULE_TIME_MONITOR, "%s:%.3f", [mainKey UTF8String], time);'
            output.write(date)
        elif '[indexPathString UTF8String], [mainKey UTF8String], time, item.totoalDuration/item.totalCount, item.totoalDuration, item.totalCount, [__VALID_NSSTRING(item.userParam) UTF8String]);' in line:
            date ='            '
            output.write(date)            
        else:  
            output.write(line)
    output.close()
    print"successful"

#修改邮件中url路径   
def reWriteUrl(codefilepath):
    lines = open(codefilepath).readlines()
    open(codefilepath).close()
    output  = open(codefilepath,'w');
    for line in lines:
        if not line:
            break
        if '/Users/rayrma/Documents/' in line:
            output.write(line.replace('/Users/rayrma/Documents/','file://xx.com/项目/文档共享/Performance/'))
        else:  
            output.write(line)
    output.close()
    print"successful"

if __name__ == "__main__":
    pass