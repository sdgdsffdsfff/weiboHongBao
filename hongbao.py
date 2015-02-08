#! /usr/bin/env python
#! encoding:utf-8

def weiboHongBaoList():
    global info
    info = [
        "http://huodong.weibo.com/hongbao/1610436341", #神州租车
        "http://huodong.weibo.com/hongbao/2411842134", #360
        "http://huodong.weibo.com/hongbao/1830346007", #易到用车
        "http://huodong.weibo.com/hongbao/1768198384", #天猫
        "http://huodong.weibo.com/hongbao/1746687693", #航美传媒
        "http://huodong.weibo.com/hongbao/3535169894"  #百度卫士  
        ]
    return info

if __name__ == "__main__":
    for i in weiboHongBaoList():
        print i
