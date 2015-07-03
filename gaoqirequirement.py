# -*- coding: utf-8 -*-  
'''
Created on 2015.7.3
高琪灌水需求
@author: marui
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import xlrd
import random


class flooding_posts(object):
    #获取评论
    def content(self):
        filepath ="D:\\content.xlsx" 
        data = xlrd.open_workbook(filepath)
        table = data.sheets()[0] 
        table.col_values(1)
        content = table.col_values(1)
        #commentresult = content[random.randint(0, len(content)-1)]
        print content
        return content
        
    #获取商家url
    def business(self):
        filepath ="D:\\url.xlsx" 
        data = xlrd.open_workbook(filepath)
        table = data.sheets()[0] 
        table.col_values(2)
        url = table.col_values(2)
        return url
    
    #获取用户名和密码
    def user(self):
        filepath ="D:\\user.xlsx" 
        data = xlrd.open_workbook(filepath)
        table = data.sheets()[0] 
        username=table.col_values(0)
        keyword=table.col_values(1)
        return username,keyword
        
    def comment(self):
        #打开浏览器
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get("http://koubei.baidu.com/?nav=index")
        browser.implicitly_wait(30)
        
        #搜索商家
        businessurl = self.business()
        for i in range(1,len(businessurl)):
            browser.find_element_by_xpath("//input[@id='search-input']").send_keys(businessurl[i])
            time.sleep(3)
            browser.find_element_by_xpath("//input[@id='search-input']").send_keys(Keys.ENTER)
            time.sleep(3)
        
            #登录
            browser.find_element_by_id("log").click()
            browser.implicitly_wait(30)
            username,keyword = self.user()
            print username,keyword
            for k in range(0,len(username)):
                browser.find_element_by_id("TANGRAM__PSP_8__userName").send_keys(username[k])
                browser.find_element_by_id("TANGRAM__PSP_8__password").send_keys(keyword[k])
                browser.find_element_by_id("TANGRAM__PSP_8__submit").click()        
                time.sleep(3)
                #点评
                comment = self.content()
                time.sleep(3)
                browser.find_element_by_css_selector("a[class=\"kb-btn\ resbar-comt-btn\ thm-btn-confirm\"]").click()
                #browser.find_element_by_xpath("//a[contains(concat(' ', @class, ' '), ' resbar-comt-btn ')]").click()
                time.sleep(3)
                
                all_handles = browser.window_handles
                now_handle = browser.current_window_handle
                for handle in all_handles:
                    if handle != now_handle:
                        print handle    
                browser.switch_to_window(handle)
                time.sleep(3)
                browser.find_element_by_xpath("//span[@id='kb-add-comt-rate']/a[2]").click()
                browser.find_element_by_id("kb-add-input").clear()
                time.sleep(3)
                for j in range(1,len(comment)+1):
                    print j
                    if j%2!=0:
                        print comment[j]
                        commentresult = comment[j]                  
                        browser.find_element_by_id("kb-add-input").send_keys(commentresult)
                        browser.find_element_by_id("w-add-comt").click()  
                        browser.implicitly_wait(30)
                        unknowntime = random.randint(30, 300)
                        print unknowntime
                        #time.sleep(unknowntime)
                       
                    else:
                        j -= 1
                    time.sleep(3)
                    #退出
                    logout = browser.find_element_by_class_name("con")
                    ActionChains(browser).move_to_element(logout).perform()
                    time.sleep(5)
                    browser.find_element_by_xpath("//div[contains(concat(' ', @class, ' '), ' user-menu ')]//a[3]").click()
                    browser.implicitly_wait(30)
                    time.sleep(3)
                
if __name__ == '__main__':
    obj = flooding_posts()
    obj.comment()