# -*- coding: utf-8 -*-  
'''
Created on 2015年1月9日
自动签到
@author: rayrma
'''
from selenium import webdriver
import time
import smtplib  
from email.header import Header
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText

class checkIn(object):
    def checkAutomation(self):
        #打开浏览器
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get("http://Attendance/StaffAttend.aspx")
        time.sleep(1)
        #输入用户名和密码，用outlook密码
        browser.find_element_by_id("txtLoginName").send_keys("xxx")#用户名
        browser.find_element_by_id("txtPassword").send_keys("")#密码
        browser.find_element_by_css_selector("p.login_outlook").click()
        browser.find_element_by_id("ibnLogin").click()
        time.sleep(5)
        #进入签到页面
        browser.find_element_by_name("ctl00$m$Button_AllDay").click()
        alert= browser.switch_to_alert() 
        alert.accept() 
        time.sleep(20)
        print alert.text
        content = alert.text
        alert.accept()
        time.sleep(3)
        browser.close()
        return content
  
    def send_mail(self,content):
        #发邮件
        msg = MIMEMultipart()
        msg['Subject'] = Header(u"签到", 'utf8')
        content += u"</body></html>"
        if isinstance(content, unicode):
            content = content.encode('utf8')
        html_part = MIMEText(content, 'html', 'utf-8')
        msg.attach(html_part)
        try:  
            smtp = smtplib.SMTP()
            smtp.connect("tsmtp.xxx.com", 25)
            smtp.login("xxx", "xxx")
            smtp.sendmail("xxx@xxx.com", "xxx@xxx.com", msg.as_string())
            print "successful"  
        except Exception:  
            print 'Error: unable to send email'
if __name__ == '__main__':
    obj = checkIn()
    obj.send_mail(obj.checkAutomation())
    