# /usr/bin/env python
# encoding:utf-8
# use Python2

import requests
import re
import smtplib
import ConfigParser
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


#==================================================
def weiboHongBao(url):
    '''
    分析指定微博红包页面是否有红包可以领取
    如果有红包可以领取就调用sendMail函数来发送邮件提醒
    '''
    regexGain = u"抢红包"
    regexShare = u"分享"
    r = requests.get(url)
    if r.status_code == 200:
        txt = r.text
        if re.search(regexGain, txt) != None:
            hongbao = re.search(regexGain, txt)
            result = "Have a HongBao"
            print result,url
            sendEmail(url,result)
        elif re.search(regexShare, txt) != None:
            hong = re.search(regexShare, txt)
            result =  "Don't have a HongBao"
            print result,url
        else:
            print "Error"



#=======================================================
def sendEmail(url, message):
    '''
    发送邮件到指定邮箱地址
    '''
    #获取配置信息
    cf = ConfigParser.ConfigParser()
    cf.read("config.ini")
    mailHost = cf.get("info", "mailHost")
    mailUser = cf.get("info", "mailUser")
    mailPassword = cf.get("info", "mailPassword")
    toMail = cf.get("info", "toMail")

    #设置邮件信息
    subject = message
    msg = msg = MIMEMultipart("alternative")
    msg["Subject"] = Header(subject,"utf-8")
    part = MIMEText(subject +';'+ url,"html") #设置以html格式发送内容
    msg.attach(part)

    #发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(mailHost) 
    smtp.login(mailUser,mailPassword) 
    smtp.sendmail(mailUser,toMail,msg.as_string())
    print "Send Email Finish"
    smtp.quit() 



if __name__ == "__main__":
    import hongbao
    for x in hongbao.weiboHongBaoList():
        #print x
        weiboHongBao(x)
    sendEmail("http://www.hiadmin.org","OK")

