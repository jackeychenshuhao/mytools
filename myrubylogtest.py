__author__ = 'jackey'
#coding=utf-8
import re
import os
w = '''112.224.65.85 - - [20/Aug/2013:00:01:02 +0800] \
"POST /api/topic/comments HTTP/1.1" 200 3804 "-" "Corax/0.7.0 CFNetwork/609.1.4 Darwin/13.0.0" "-" "1.173" "0.005"'''

'''Started GET "/352335_15_15.html" for 157.55.39.60 at 2015-01-02 00:00:02 +0800
source=rack-timeout id=95910b34a0e2176f9947ec52698f2939 timeout=10000ms state=ready
Processing by Mobile::HomeController#index as HTML
  Parameters: {"xrk_source"=>"www", "xrk_medium"=>"xrk_dingzhi_mobile", "xrk_campaign"=>"shaoer-new_detail", "xrk_content"=>"notset", "gadevice"=>"mobile"}
source=rack-timeout id=95910b34a0e2176f9947ec52698f2939 timeout=10000ms service=24ms state=completed
get_city_by_name  url : http://127.0.0.1:5000/locate/cities/find_by_names.json?names=局域网
Processing by InsuranceController#pinpai_static as */*
  Parameters: {"static"=>nil, "select"=>"0_35_1-2-4_3_31_0"}
Completed 500 Internal Server Error in 50ms '''
log = "/opt/production.log"
txt = "/tmp/test.txt"
loglist = []

def cmd(cmd):
    return os.popen(cmd).readlines()
for i in cmd("cat %s |grep  -E '(^Started)'" % log):
    print i
'''    truelog = i.strip().split(' ')
    loglist.append(truelog)
    for y in range(len(loglist)):
        print loglist[y]
txt.write("%s\n"%loglist)
'''