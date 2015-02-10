# weiboHongBao

微博抢红包提醒通知
--------------------------
最近微博上开始抢红包之后发现发红包的人都是随机不定时的在发红包；

为了能够及时的知道是否有红包可以抢；所以弄了下面这个脚本。

功能
----
    这个脚本的功能很简单；就是检测制定红包页面；如果发现可以抢红包就发送一个邮件到指定邮箱做一个提醒

下载安装第三方库
----
    1.  requests
    2.  python 2.x

使用
----
    1.  将你需要访问的红包页面添加到hongbao.py里面；如http://huodong.weibo.com/hongbao/1768198384这样的
    2.  修改config.ini配置文件；
    3.  填写发送邮件的host和账号密码；以及接收邮件地址；建议用QQ邮件接收；QQ有邮件提醒很方便
    4.  运行weibo.py即可
    
config.ini配置文件说明
--------
    [info]
    mailHost = smtp.126.com ;发送邮件的host
    mailUser = userxxxx@126.com ；发送邮件账号
    mailPassword = *******      ；发送邮件密码
    toMail = *******@qq.com     ；接收邮件的账号

