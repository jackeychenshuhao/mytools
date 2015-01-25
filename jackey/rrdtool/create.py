# -*- coding: utf-8 -*-
#!/usr/bin/python
import rrdtool
import time
cur_time=str(int(time.time()))
# 获取当前 Linux 时间戳作为 rrd 起始时间
# 数据写频率 --step 为 300 秒 ( 即 5 分钟一个数据点 )
rrd=rrdtool.create('XRK.rrd', '--step', '300', '--start', cur_time, \
# 定义数据源 eth0_in( 入流量 )、eth0_out( 出流量 );类型都为 COUNTER( 递增 );600 秒为心跳值,
# 其含义是 600 秒没有收到值,则会用 UNKNOWN 代替;0 为最小值;最大值用 U 代替,表示不确定
'DS:wlan0_in:COUNTER:600:0:U',
'DS:wlan0_out:COUNTER:600:0:U',
#RRA 定义格式为 [RRA:CF:xff:steps:rows],CF 定义了 AVERAGE、MAX、MIN 三种数据合并方式
#xff 定义为 0.5,表示一个 CDP 中的 PDP 值如超过一半值为 UNKNOWN,则该 CDP 的值就被标为 UNKNOWN
# 下列前 4 个 RRA 的定义说明如下,其他定义与 AVERAGE 方式相似,区别是存最大值与最小值
# 每隔 5 分钟 (1*300 秒 ) 存一次数据的平均值 , 存 600 笔,即 2.08 天
# 每隔 30 分钟 (6*300 秒 ) 存一次数据的平均值 , 存 700 笔,即 14.58 天(2 周)
# 每隔 2 小时 (24*300 秒 ) 存一次数据的平均值 , 存 775 笔,即 64.58 天(2 个月)
# 每隔 24 小时 (288*300 秒 ) 存一次数据的平均值 , 存 797 笔,即 797 天 (2 年 )
'RRA:AVERAGE:0.5:1:600',
'RRA:AVERAGE:0.5:6:700',
'RRA:AVERAGE:0.5:24:775',
'RRA:AVERAGE:0.5:288:797',
'RRA:MAX:0.5:1:600',
'RRA:MAX:0.5:6:700',
'RRA:MAX:0.5:24:775',
'RRA:MAX:0.5:444:797',
'RRA:MIN:0.5:1:600',
'RRA:MIN:0.5:6:700',
'RRA:MIN:0.5:24:775',
'RRA:MIN:0.5:444:797')
if rrd:
    print rrdtool.error()