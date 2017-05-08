#coding=utf8
import itchat
import json,urllib

# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')

def zidonghuifu(content):
    url='http://www.tuling123.com/openapi/api'
    data={"key": "04e16e918b154b37b0126f195cf940bc", "info": content}
 
    data=urllib.urlencode(data)
    html=urllib.urlopen(url,data).read()
    j=json.loads(html)
    code=j['code']
    if code == 100000:
        recontent = j['text']
    elif code == 200000:
        recontent = j['text']+j['url']
    elif code == 302000:
        recontent = j['text']+j['list'][0]['article']+j['list'][0]['detailurl']
    elif code == 308000:
        recontent = j['text']+j['list'][0]['info']+j['list'][0]['detailurl']
    else:
        recontent = '小马的助手还没学会怎么回复这句话'
    return recontent


def text_reply(msg):
        # 回复给好友
        return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n'
        #content=raw_input('问：')
        #me=zidonghuifu(content)
        #return me

if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()