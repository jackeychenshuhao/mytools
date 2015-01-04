__author__ = 'jackey'
#!/usr/bin/env python

#coding:utf-8
import os
import json
import httplib
import codecs
#LogFile= raw_input('please input your logpath:')
LogFile='/opt/nginx.log'
logMess='/tmp/accnginx.log'

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
    r1 = conn.getresponse()

    if r1.status == 200:
        return json.loads(r1.read())['data']

    else:
        return "Error"


file.write(u"shuoming:ip   access  ipcountry city isp  cap  area\n")
ipDb=[]



for i in cmd('''/usr/bin/awk '{print $1}' %s |sort|uniq -c|sort -nr|head ''' % LogFile):
    ip = i.strip().split(' ')
    ipDb.append(ip)
print ipDb
print "############## Access count 10 ip: ###################"

for i in ipDb:
    _tmpD=getIpCountry(i[1])
#    out="%s%s%s%s%s%s%s"%(i[1].ljust(20),i[0].ljust(10),_tmpD['country'].ljust(15),_tmpD['city'
#    ].ljust(16),_tmpD['isp_id'].ljust(16),_tmpD['region'].ljust(16),_tmpD['area'].ljust(16))
    out="%s%s%s%s%s%s"%(i[1].ljust(20),i[0].ljust(10),_tmpD['country'].ljust(15),_tmpD['region'].ljust(16),_tmpD['city'
    ].ljust(16),_tmpD['isp_id'].ljust(16))
    print out

file.write("%s\n"%out)
conn.close()
file.close()

