#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pycurl
import os
import sys
import time

URL = "http://www.xiangrikui.com"

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

NAMELOOKUP_TIME = Curlobj.getinfo(Curlobj.NAMELOOKUP_TIME)
CONNECT_TIME = Curlobj.getinfo(Curlobj.CONNECT_TIME)
PRETRANSFER_TIME = Curlobj.getinfo(Curlobj.PRETRANSFER_TIME)
STARTTRANSFER_TIME = Curlobj.getinfo(Curlobj.STARTTRANSFER_TIME)

TOTAL_TIME = Curlobj.getinfo(Curlobj.TOTAL_TIME)
HTTP_CODE = Curlobj.getinfo(Curlobj.HTTP_CODE)
SIZE_DOWNLOAD = Curlobj.getinfo(Curlobj.SIZE_DOWNLOAD)
HEADER_SIZE = Curlobj.getinfo(Curlobj.HEADER_SIZE)
SPEED_DOWNLOAD = Curlobj.getinfo(Curlobj.SPEED_DOWNLOAD)

print "HTTP状态码: %s" % (HTTP_CODE)
print "DNS解析时间: %.2f ms" % (NAMELOOKUP_TIME*1000)
print "建立连接时间: %.2f ms" % (CONNECT_TIME*1000)
print "准备传输时间: %.2f ms" % (PRETRANSFER_TIME*1000)
print "传输开始时间: %.2f ms" % (STARTTRANSFER_TIME*1000)
print "传输结束时间: %.2f ms" % (TOTAL_TIME*1000)
print "下载数据包大小: %d bytes/s" % (SIZE_DOWNLOAD)
print "HTTP头部大小: %d byte" % (HEADER_SIZE)
print "平均下载速度: %d bytes/s" % (SPEED_DOWNLOAD)

bodyfile.close()
Curlobj.close()


