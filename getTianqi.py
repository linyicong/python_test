# -*- coding: utf-8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")

import urllib2
import json
from city import city
# cityname=raw_input('你想查那个城市的天气？\n')
cityname = "广州"
#cityname = os.environ['CityName']

# Default city info
if not cityname:
    cityname = "北京"
citycode=city.get(cityname)

if citycode:
    try:    ##做一个异常处理
        url=('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode) ##定义一个变量。存放要请求的连接
        content=urllib2.urlopen(url).read()     #定义一个变量，用来存储查询的内容。urllib2.urlopen(url)是用来请求/打开这个连接。read是把内容读取放到变量中
        #print content
        data=json.loads(content)        ##定义一个字典，使用json的函数loads方法吧内容整理成一个字典，
        result = data['weatherinfo']
        str_temp = ('%s天气：\n  \t%s\n\t%s ~ %s') % (
        result['city'], 
        result['weather'],  
        result['temp1'],
        result['temp2']
        )
        print str_temp
    except:
        print '查询失败'
else:
    print '没有找到城市'
