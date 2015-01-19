#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pycurl
import os
import sys
import time
from decimal import Decimal

URL = "http://www.baidu.com"

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
self.NAMELOOKUP_TIME = Decimal(str(round(Curlobj.getinfo(Curlobj.NAMELOOKUP_TIME), 2)))
self.CONNECT_TIME = Decimal(str(round(Curlobj.getinfo(Curlobj.CONNECT_TIME), 2)))
self.PRETRANSFER_TIME = Decimal(str(round(Curlobj.getinfo(Curlobj.PRETRANSFER_TIME), 2)))
self.STARTTRANSFER_TIME = Decimal(str(round(Curlobj.getinfo(Curlobj.STARTTRANSFER_TIME), 2)))

self.TOTAL_TIME = Decimal(str(round(Curlobj.getinfo(Curlobj.TOTAL_TIME), 2)))
HTTP_CODE = Curlobj.getinfo(Curlobj.HTTP_CODE)
SIZE_DOWNLOAD = Curlobj.getinfo(Curlobj.SIZE_DOWNLOAD)
HEADER_SIZE = Curlobj.getinfo(Curlobj.HEADER_SIZE)
SPEED_DOWNLOAD = Curlobj.getinfo(Curlobj.SPEED_DOWNLOAD)




Curlobj.close()


