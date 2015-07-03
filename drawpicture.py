# -*- coding: utf-8 -*-  
'''
Created on 2014年12月24日

@author: rayrma
'''
from pylab import *
import re

class draw(object): 
    def getAllVersion(self):
        key = 0
        timeVersionAllList = []
        logs_object = open ('C:\\Users\\Administrator\\Desktop\\iTimeConfig.txt')
        try :
            logs = logs_object.read()
        finally:
            logs_object.close()    
            if len(logs) == 0: 
                return (key)
            lines = logs.split("\n")
            for line in lines:
                if line.__contains__("timeVersion"):#读取带有keyTimeMonitoryFeedLayout关键字的行
                    x = re.compile(r'timeVersion\[(.*?)\]').findall(str(line))#获取average的值
                    #print x
                    if x:
                        timeVersion = [int(x[0])]
                        timeVersionElement = int(timeVersion[-1]) 
                    print timeVersionElement
                    timeVersionAllList.append(timeVersionElement)
                else :
                    pass                                    
            result = timeVersionAllList 
            #print result          
            return result  
    
    def drawpicture(self): 
        mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  
        mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题 
        version = self.getAllVersion()
        keyTimeMonitoryFeedLayout = [1,3,5,6,8]# Make an array of y values for each x value
        keyTimeMonitoryFeedDraw = [3, 4, 5, 6, 4]
        keyTimeMonitoryOpenActiveFeedVC = [2,5,5,3,2]
        keyTimeMonitoryClickAddBtn = [2,5,5,3,2]
        plt.title(u"耗时监控")
        plt.xlabel("Version")
        plt.ylabel("Time")
        plt.plot(version,keyTimeMonitoryFeedLayout,'bo:',label=u'整个feed排版时间')# use pylab to plot x and y   blue
        plt.plot(version,keyTimeMonitoryFeedDraw,'yo:',label=u'绘制时间')#yellow
        plt.plot(version,keyTimeMonitoryOpenActiveFeedVC,'ro:',label=u'好友动态打开开始时间')#red
        plt.plot(version,keyTimeMonitoryClickAddBtn,'ko:',label=u'加号打开开始时间')#
        plt.legend() 
        plt.savefig('itime.png', dpi=100)
        plt.show()# show the plot on the screen
    
if __name__ == "__main__":
    obj = draw()
    obj.drawpicture()