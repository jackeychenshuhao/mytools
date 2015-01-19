import socket,yaml
import ast
import time,os,sys
import commands
from sendmail2 import Mail
from conf  import cfd

config_file='config.yml'
config_file = os.path.dirname(os.path.realpath(__file__)) + os.sep +'conf'+os.sep+ config_file

f=open(config_file)
configMap=yaml.load(f)
f.close()

checkhost=configMap['checkhost']





#checkhost=ast.literal_eval(cfd.get('checkhost','checkhost'))
mail=Mail()

font1="""<br><font  face="arial" color="red">%s</font><br>"""


PATH=os.path.abspath(sys.argv[0])
PATH=os.path.dirname(PATH)+"/"

def openSocket(ip,ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    result = sock.connect_ex((ip,ports))
    sock.settimeout(None)
    return result





class Runcheck:
    def check_ports(self,dic,num,data=[]):
        num = num - 1 
        dicbroke={}
        for ip in dic:
            di = 0
            for ports in dic[ip]:
                result=openSocket(ip,ports)
                if result != 0:
                    dicbroke[ip]=dic[ip]
                    if num != 0:
                        continue
                    else:
                        if (di == 0):
                            if  ports  in [9990,9991,9992,8555,9980]:
                                data.append("http://%s:9992/srv_stat" % ip)
                                di = 1
                            if  ports  in [9088,8088]:
                                data.append("https://%s:9088/srv_stat" % ip)
                                di = 1
                        data.append(ip+':'+str(ports)+'&nbsp;&nbsp;&nbsp;is&nbsp;&nbsp;down!!')

        if (dicbroke and num):
            time.sleep(1)
            self.check_ports(dicbroke,num,data)
        return data








if __name__ == '__main__':
    imgpath=PATH + 'image/'
    picname_or=['bitdata.png','data.png']
    imgname=[]
    for pic in picname_or:
        imgname.append(imgpath + pic)
    r=Runcheck()
    data=r.check_ports(checkhost,3)
    print data
    print (time.ctime(),data)
    if data:
        try:
            commands.getstatusoutput('sh %screate-img.sh' % PATH)
        except Exception, exc:
            print str(exc)
        maildata="=====================================<br>"
        for i in data:
            maildata = maildata + (font1 % i)
        #result=mail.Sendmail(picname=imgname,to_users=['513914894@qq.com','xiaojxiao1203@qq.com','0x0000e000@gmail.com','75635875@qq.com'],filename=__file__,subject="airdroid ports check",content=maildata)
        #if result:
        #    time.sleep(10)
        #    result2=mail.Sendmail(to_users=['513914894@qq.com','xiaojxiao1203@qq.com','0x0000e000@gmail.com','75635875@qq.com'],filename=__file__,subject="airdroid ports check",content=maildata,picname=imgname)
        #    if result2:
        #        time.sleep(20)
        #        mail.Sendmail(to_users=['513914894@qq.com','xiaojxiao1203@qq.com','0x0000e000@gmail.com','75635875@qq.com'],filename=__file__,subject="airdroid ports check",content=maildata,picname=imgname)


#




