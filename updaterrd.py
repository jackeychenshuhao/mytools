#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rrdtool
import logging

def updateRRD(self,rowobj):
    if str(rowobj["HTTP_CODE"])=="200":
        unavailablevalue=0
    else:
        unavailablevalue=1
    FID=rowobj["FID"]
    time_rrdpath=RRDPATH+'/'+str(self.getURL(FID))+'/'+str(FID)+'_'+\
        str(self.rrdfiletype[0])+'.rrd' #指定三个特征数据rrdtool文件位置
    download_rrdpath=RRDPATH+'/'+str(self.getURL(FID))+'/'+str(FID)+'_'+\
        str(self.rrdfiletype[1])+'.rrd'
    unavailable_rrdpath=RRDPATH+'/'+str(self.getURL(FID))+'/'+str(FID)+'_'+\
        str(self.rrdfiletype[2])+'.rrd'
    #将查询的mysql记录更新到rrd文件
    try:
        rrdtool.updatev(time_rrdpath,'%s:%s:%s:%s:%s:%s' %(str(rowobj["DATETIME"])\
            ,str(rowobj["NAMELOOKUP_TIME"]),str(rowobj["CONNECT_TIME"]),str(rowobj["PRETRANSFER_TIME"]),\
            str(rowobj["STARTTRANSFER_TIME"]),str(rowobj["TOTAL_TIME"])))
        rrdtool.updatev(download_rrdpath,'%s:%s' % (str(rowobj["DATETIME"]),\
            str(rowobj["SPEED_DOWNLOAD"]),str(unavailablevalue)))
        self.setMARK(rowobj["ID"]) #更新数据库状态
    except Exception,e:
        logging.error('update rrd error:'+str(e))

def setMARK(self,_id): #更新已标记录方法
    try:
        self.cursor.execute("update webmonitor_monitordata set \
                            MARK = '1' where ID = '%s'" % (_id))
        self.conn.commit()
    except Exception,e:
        logging.error('SetMark database error:' + str(e))

def getNewdata(self):
    try:
        self.cursor.execute("select ID,FID,NAMELOOKUP_TIME,CONNECT_TIME,PRETRANSFER_TIME,STARTTRANSFER_TIME,TOTAL_TIME,\
                            HTTP_CODE,SPEED_DOWNLOAD,DATETIME from webmonitor_monitordata where MARK='0'")
        for row in self.cursor.fetchall():
            self.updateRRD(row)
    except Exception,e:
        logging.error('Get new database error:'+str(e))

