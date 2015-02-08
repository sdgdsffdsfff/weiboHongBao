# /usr/bin/env python
# encoding:utf-8
# use Python2

import requests
import re
import smtplib
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
    mailHost = "smtp.126.com"
    mailUser = "user****@126.com"
    mailPassword = "password******"
    toMail = "usr@qq.com"
    subject = message
    msg = msg = MIMEMultipart("alternative")
    msg["Subject"] = Header(subject,"utf-8")
    part = MIMEText(subject +';'+ url,"html") #设置以html格式发送内容
    msg.attach(part)

    smtp = smtplib.SMTP()
    smtp.connect(mailHost) 
    smtp.login(mailUser,mailPassword) 
    smtp.sendmail(mailUser,toMail,msg.as_string())
    print "Send Email Finish"
    smtp.quit() 



if __name__ == "__main__":
    # url = [
    #     "http://huodong.weibo.com/hongbao/1610436341", #神州租车
    #     "http://huodong.weibo.com/hongbao/2411842134", #360
    #     "http://huodong.weibo.com/hongbao/1830346007", #易到用车
    #     "http://huodong.weibo.com/hongbao/1768198384", #天猫
    #     "http://huodong.weibo.com/hongbao/1935767654" #测试红包

    # for i in url:
    #     #print i
    #     weiboHongBao(i)

    import hongbao
    for x in hongbao.weiboHongBaoList():
        #print x
        weiboHongBao(x)

