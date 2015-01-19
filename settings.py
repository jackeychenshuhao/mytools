import runmonitor
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

SYSTEM_NAME='监控平台'
IDC = {'ct':'电信'}
RRDPATH = BASE_DIR+"/rrd"
PNGPATH = BASE_DIR+"/site_media/rrdtool"


MAINAPPPATH = BASE_DIR+"/webmonitor"

TIME_ALARM = 1
TIME_YMAX = 1
DOWN_APEED_YMAX = 8388608