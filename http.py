__author__ = 'jackey'
#!/usr/bin/python
import httplib
import urllib
conn = httplib.HTTPConnection('exmail.qq.com')

conn.request('GET', '/')
http = conn.getresponse()
print http.status
print http.reason
print http.read()