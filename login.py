__author__ = 'jackey'
#!/usr/bin/env python

import urllib
import httplib2

http = httplib2.Http()

url = 'http://exmail.qq.com/login'
body = {'USERNAME': 'chenshuhao@xiangrikui.com', 'PASSWORD': 'wocao2013'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body))

headers = {'Cookie': response['set-cookie']}
p = response.status
m = response.reason
n = response.keys()
print p
print m
print n
url = 'http://exmail.qq.com/login'
response, content = http.request(url, 'GET', headers=headers)

