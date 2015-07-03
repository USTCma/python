# -*- coding: UTF-8 -*-
'''
Created on 2014年12月4日

@author: rayrma
'''
def ui(self,oldtime,newtime): 
    if oldtime >= newtime:
        print u'<font color="green">'+abs(oldtime-newtime)+'</font>'
    else:
        print u'<font color="red">'+abs(oldtime-newtime)+'</font>'

print ui(5, 3)