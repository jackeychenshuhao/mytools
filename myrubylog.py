__author__ = 'jackey'
#coding=utf-8
import linecache
import re
import time,datetime
import glob
import os
#import conn
w = '''112.224.65.85 - - [20/Aug/2013:00:01:02 +0800] \
"POST /api/topic/comments HTTP/1.1" 200 3804 "-" "Corax/0.7.0 CFNetwork/609.1.4 Darwin/13.0.0" "-" "1.173" "0.005"'''
files_dir = "/home/jackey/"
bak_dir = "/opt"

def readfile(path):
    filename = []
    files = glob.glob(path + '*.log')
    return files

def readtime(path):
    read_time = []
    files = glob.glob(path + '*.log')
    print files
    for i in files:
        read_time.append(i.split('_')[1].split('.')[0])
    read_time = set(read_time)
    return read_time

def timestamp(time_file):
    return time.mktime(time.strptime(time_file,'%Y%b%d %H:%M:%S'))

def datestamp(date_name):
    return time.strptime(date_name,'%Y%b%d')

def handle_log(log_file):
    ip = r"?P<ip>[\d.]*"
    date = r"?P<date>\d+"
    month = r"?P<month>\w+"
    year = r"?P<year>\d+"
    log_time = r"?P<time>\S+"
    method = r"?P<method>\S+"
    request = r"?P<request>\S+"
    status = r"?P<status>\d+"
    bodyBytesSent = r"?P<bodyBytesSent>\d+"
    refer = r"""?P<refer>
             [^\"]*
             """
    userAgent=r"""?P<userAgent>
                \S*
               """
    forwardr=r"""?P<forwardr>
                [^\"]*
               """
    request_time=r"""?P<request_time>
                [^\"]*
               """
    response_time=r"""?P<response_time>
                [^\"]*
               """
    p = re.compile(r"(%s)\ -\ -\ \[(%s)/(%s)/(%s)\:(%s)\ [\S]+\]\ \"(%s)?[\s]?(%s)?.*?\"\ (%s)\ (%s)\ \"(%s)\"\ \"(%s).*?\"\ \"(%s)\"\ \"(%s)\"\ \"(%s)\"" %(ip, date, month, year, log_time, method, request, status, bodyBytesSent, refer, userAgent, forwardr, request_time, response_time ), re.VERBOSE)

    s = time.time()

    log_list = []
    for l in log_file:
        f = open(l,'r')
        file_all = f.read()
        m = re.findall(p,file_all)
        for g in m:
            time_all = '%s%s%s %s'%(g[3], g[2], g[1], g[4])
            time_format = timestamp(time_all)
            date = time.strftime("%Y%m%d",datestamp('%s%s%s'%(g[3], g[2], g[1])))
            hour = g[4].split(":")[0]
            # print date,hour
            if g[12] != "-":
                req_time = float(g[12])
            else:
                req_time = None
            if g[13] != "-" and len(g[13])<=5:
                res_time = float(g[13])
            else:
                res_time =  None
            log = {'ip':g[0],'time':time_format,'method':g[5],'request':g[6],'status':g[7],'bodyBytesSent':g[8],'refer':g[9],'userAgent':g[10],'forwardr':g[11],'request_time':req_time,'response_time':res_time,'date':int(date),'hour':int(hour)}

            conn.db.log.insert(log)
        f.close()
        print "mv %s %s "%(l,bak_dir)
        os.system("mv %s %s "%(l,bak_dir))
    print time.time() - s

if __name__ == '__main__':
    lf = readfile(files_dir)
    print lf
    read_time = readtime(files_dir)
    print read_time
    handle_log(lf)