import sys,os
from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)
from email.MIMEText import MIMEText
reload(sys)
sys.setdefaultencoding('utf8')
filename=sys.argv[0][sys.argv[0].rfind(os.sep)+1:]

class Mail():
    def __init__(self):
        self.text_subtype = 'plain'
        self.html_subtype ='html'
        self.SMTPserver = 'smtp.126.com'
        self.sender =     'wfuqiang_mail@126.com'
        self.USERNAME = "wfuqiang_mail@126.com"
        self.PASSWORD = "wang123fufu"
    def Sendmail(self,to_users=['513914894@qq.com'],subject='',subtoye='html',content='null',filename=''):
        to_users=to_users
        filename=filename
        subject=subject
        subtoye=subtoye
        content=content
        html = """\
<html>
  <head></head>
  <body>
  <h1 align="center"><font size="5" face="arial" color="red">Airdroid Ports status </font></h1>
  <p><b>    %s</b></p>
  <p><i>(from %s)</i></p>
  </body>
</html>
"""  % (content,filename)
        try:
            msg = MIMEText(html,subtoye)
            msg['Subject']= subject
            msg['From']   = self.sender # some SMTP servers will do this automatically, not all
            conn = SMTP(self.SMTPserver)
            conn.set_debuglevel(False)
            conn.login(self.USERNAME, self.PASSWORD)
            try:
                conn.sendmail(self.sender,to_users, msg.as_string())
            finally:
                conn.close()
        except Exception, exc:
                print str(exc)
                return 'fail'
#                sys.exit( "mail failed; %s" % str(exc) )



