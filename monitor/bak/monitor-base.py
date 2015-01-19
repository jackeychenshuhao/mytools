import socket
import ast
import time
from sendmail import Mail
from conf  import cfd
checkhost=ast.literal_eval(cfd.get('checkhost','checkhost'))
mail=Mail()

font1="""<br><font  face="arial" color="red">%s</font><br>"""

def openSocket(ip,ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    result = sock.connect_ex((ip,ports))
    sock.settimeout(None)
    return result

class Runcheck:
    def __init__(self):
        pass
    def check_ports(self,dic):
        data=[]
        for ip in dic:
            for ports in dic[ip]:
                result=openSocket(ip,ports)
                if result != 0:
                    data.append(ip+':'+str(ports)+'&nbsp;&nbsp;&nbsp;is&nbsp;&nbsp;down!!')
        return data



if __name__ == '__main__':
    r=Runcheck()
    data=r.check_ports(checkhost)
    print (time.ctime(),data)
    if data:
        maildata="=====================================<br>"
        for i in data:
            maildata = maildata + (font1 % i)
        re_code=mail.Sendmail(filename=__file__,to_users=['513914894@qq.com','xiaojxiao1203@qq.com','0x0000e000@gmail.com','75635875@qq.com'],subject="airdroid ports check",content=maildata)
        if re_code:
            time.sleep(10)
            re_code2=mail.Sendmail(filename=__file__,to_users=['513914894@qq.com','xiaojxiao1203@qq.com','0x0000e000@gmail.com','75635875@qq.com'],subject="airdroid ports check",content=maildata)
            if re_code2:
                time.sleep(20)
                mail.Sendmail(filename=__file__,to_users=['513914894@qq.com','xiaojxiao1203@qq.com','0x0000e000@gmail.com','75635875@qq.com'],subject="airdroid ports check",content=maildata)
