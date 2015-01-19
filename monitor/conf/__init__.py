__author__ = 'tongbuop'

import os,ConfigParser
class loadfile():
    def __init__(self):
        self.path=os.path.abspath(os.path.dirname(__file__))
    def conf_data(self,conf_name='init.conf'):
        conf_pn=self.path+ '/' +conf_name
        cf = ConfigParser.ConfigParser()
        cf.read(conf_pn)
        return cf


Con=loadfile()
cfd=Con.conf_data()
