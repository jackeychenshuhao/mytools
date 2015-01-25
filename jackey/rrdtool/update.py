# -*- coding: utf-8 -*-
#!/usr/bin/python
import rrdtool
import time,psutil
total_input_traffic = psutil.net_io_counters()[1]
# 获取网卡入流量
total_output_traffic = psutil.net_io_counters()[0]
# 获取网卡出流量
starttime=int(time.time())
# 获取当前 Linux 时间戳
# 将获取到的三个数据作为 updatev 的参数,返回 {'return_value': 0L} 则说明更新成功,反之失败
update=rrdtool.updatev('/opt/mytools/mytools/rrdtool/XRK.rrd','%s:%s:%s' %
(str(starttime),str(total_input_traffic),str(total_output_traffic)))
print update