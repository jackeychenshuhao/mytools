#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pycurl
import os
import sys
import time
import MySQLdb
import os, sys, string
from jackey.jiankong import *
from decimal import Decimal
DATETIME = str(int(time.time()))
URL = "http://www.baidu.com"
#def rowobj(self):
Curlobj=pycurl.Curl()
Curlobj.setopt(pycurl.URL, URL)
Curlobj.setopt(pycurl.CONNECTTIMEOUT, 10)
Curlobj.setopt(pycurl.TIMEOUT, 10)
Curlobj.setopt(pycurl.NOPROGRESS, 1)
Curlobj.setopt(pycurl.FORBID_REUSE, 1)
Curlobj.setopt(pycurl.MAXREDIRS, 1)
Curlobj.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)

bodyfile = open(os.path.dirname(os.path.realpath(__file__)) + "/tmp/_body", "wb")

Curlobj.setopt(pycurl.WRITEHEADER, bodyfile)
Curlobj.setopt(pycurl.WRITEDATA, bodyfile)
Curlobj.perform()
bodyfile.close()
"""
 定义getinfo响应返回常量
"""
NAMELOOKUP_TIME = Decimal(str(round(Curlobj.getinfo(Curlobj.NAMELOOKUP_TIME), 2)))
CONNECT_TIME = Decimal(str(round(Curlobj.getinfo(Curlobj.CONNECT_TIME), 2)))
PRETRANSFER_TIME = Decimal(str(round(Curlobj.getinfo(Curlobj.PRETRANSFER_TIME), 2)))
STARTTRANSFER_TIME = Decimal(str(round(Curlobj.getinfo(Curlobj.STARTTRANSFER_TIME), 2)))

TOTAL_TIME = Decimal(str(round(Curlobj.getinfo(Curlobj.TOTAL_TIME), 2)))
HTTP_CODE = Curlobj.getinfo(Curlobj.HTTP_CODE)
SIZE_DOWNLOAD = Curlobj.getinfo(Curlobj.SIZE_DOWNLOAD)
HEADER_SIZE = Curlobj.getinfo(Curlobj.HEADER_SIZE)
SPEED_DOWNLOAD = Curlobj.getinfo(Curlobj.SPEED_DOWNLOAD)


Curlobj.close()

host = "192.168.1.100"
try:
    conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='redhat',db='test')
except Exception, e:
    print e
    sys.exit()
cursor = conn.cursor()
#val = "insert into xrk_hostinfo(ID, URL) values (%s, %s)" % (1, URL)
sql = "insert into xrk_monitordata(FID, NAMELOOKUP_TIME, CONNECT_TIME, PRETRANSFER_TIME, TOTAL_TIME, HTTP_CODE, \
  SIZE_DOWNLOAD, HEADER_SIZE, SPEED_DOWNLOAD, STARTTRANSFER_TIME, REQUEST_TIME, CONNENET_LENGTH_DOWNLOAD, DATETIME) \
  values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (1, NAMELOOKUP_TIME, \
    CONNECT_TIME, PRETRANSFER_TIME, TOTAL_TIME, HTTP_CODE, SIZE_DOWNLOAD, HEADER_SIZE, SPEED_DOWNLOAD, STARTTRANSFER_TIME, \
    0.1, 0.2, DATETIME)
try:
    cursor.execute(sql)
except Exception, e:
    print e
#查询出数据
meizi = "select * from xrk_monitordata"
cursor.execute(meizi)
alldata = cursor.fetchall()

if alldata:
    print alldata
    for rec in alldata:
        print rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8], rec[9], rec[10], rec[11], rec[12]



cursor.close()

conn.close()