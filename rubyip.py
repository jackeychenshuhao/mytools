__author__ = 'jackey'

#!/usr/bin/env python

#coding:utf-8
import os
import json
import httplib
import codecs
LogFile= raw_input('please input your logpath:')
ipcount = raw_input('please input ip count:')
logMess='/tmp/accruby.log'
if os.path.isfile(logMess):
 os.system('cp /dev/null %s'% logMess)
file=codecs.open(logMess,'w+',encoding='utf-8')
def cmd(cmd):
  return os.popen(cmd).readlines()
'''
def getIp(ip):
 return json.loads(os.popen("/usr/bin/curl http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip).readline())['data']
'''
conn = httplib.HTTPConnection('ip.taobao.com')
def getIpCountry(ip):
 conn.request('GET','/service/getIpInfo.php?ip=%s' % ip)
 r1=conn.getresponse()
 if r1.status == 200:
  return json.loads(r1.read())['data']
 else:
  return "Error"


file.write(u"shuoming:ip   access  ipcountry city isp  cap  area\n")
ipDb=[]
for i in cmd('''cat %s |grep ^Started|awk -F'at' '{print $1}'|awk '{print $NF}' \
|grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'|sort|uniq -c|sort -nr|head -n %s
 ''' % (LogFile,ipcount)):
 ip = i.strip().split(' ')
 ipDb.append(ip)

print "############## Access count %s ip: ###################" % ipcount
for i in ipDb:
 _tmpD=getIpCountry(i[1])

 out="%s%s%s%s%s%s%s"%(i[1].ljust(20),i[0].ljust(10),_tmpD['country'].ljust(20),_tmpD['city'
 ].ljust(16),_tmpD['isp_id'].ljust(16),_tmpD['region'].ljust(16),_tmpD['area'].ljust(16))

 print out
 file.write("%s\n"%out)
conn.close()
file.close()

