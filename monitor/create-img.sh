timestart=`date +%s`
dats=`date -d @$timestart +"%Y-%m-%d %H\:%M"`
timeend=`expr $timestart - 14400`
daes=`date -d @$timeend  +"%Y-%m-%d %H\:%M"`
/usr/bin/rrdtool graph  /mnt/python/wfq/monitor/image/bitdata.png\
    --imgformat=PNG \
    --start=$timeend \
    --end=$timestart \
    --title='unique phone conn (bitdata)' \
    --base=1000 \
    --height=120 \
    --width=550 \
    --alt-autoscale-max \
    --lower-limit='0' \
    COMMENT:"From $daes  To $dats\c" \
    COMMENT:"  \n" \
    --vertical-label='' \
    --slope-mode \
    --font TITLE:10: \
    --font AXIS:7: \
    --font LEGEND:8: \
    --font UNIT:7: \
    DEF:a="/var/www/cacti-0.8.8a/rra/_bdf_59_marched_435.rrd":'bdf_34_marched':AVERAGE \
    DEF:b="/var/www/cacti-0.8.8a/rra/_bdf_59_marched_435.rrd":'bdf_40_marched':AVERAGE \
    DEF:c="/var/www/cacti-0.8.8a/rra/_bdf_59_marched_435.rrd":'bdf_53_marched':AVERAGE \
    DEF:d="/var/www/cacti-0.8.8a/rra/_bdf_59_marched_435.rrd":'bdf_55_marched':AVERAGE \
    DEF:e="/var/www/cacti-0.8.8a/rra/_bdf_59_marched_435.rrd":'bdf_57_marched':AVERAGE \
    DEF:f="/var/www/cacti-0.8.8a/rra/_bdf_59_marched_435.rrd":'bdf_59_marched':AVERAGE \
    LINE1:a#00BF47FF:"dbf_34_us_east_matched"  \
    GPRINT:a:LAST:"cur\:%8.0lf"  \
    GPRINT:a:AVERAGE:"avg\:%8.0lf"  \
    GPRINT:a:MAX:"max\:%8.0lf"  \
    GPRINT:a:MIN:"min\:%8.0lf\n"  \
    LINE1:b#004359FF:"bdf_40_us_east_matched"  \
    GPRINT:b:LAST:"cur\:%8.0lf"  \
    GPRINT:b:AVERAGE:"avg\:%8.0lf"  \
    GPRINT:b:MAX:"max\:%8.0lf"  \
    GPRINT:b:MIN:"min\:%8.0lf\n"  \
    LINE1:c#FF3932FF:"bdf_53_cn_matched"  \
    GPRINT:c:LAST:"     cur\:%8.0lf"  \
    GPRINT:c:AVERAGE:"avg\:%8.0lf"  \
    GPRINT:c:MAX:"max\:%8.0lf"  \
    GPRINT:c:MIN:"min%8.0lf\n"  \
    LINE1:d#FF9900FF:"bdf_55_eu_west_matched"  \
    GPRINT:d:LAST:"cur\:%8.0lf"  \
    GPRINT:d:AVERAGE:"avg\:%8.0lf"  \
    GPRINT:d:MAX:"max\:%8.0lf"  \
    GPRINT:d:MIN:"min\:%8.0lf\n"  \
    LINE1:e#4668E4FF:"bdf_57_sa_east_matched"  \
    GPRINT:e:LAST:"cur\:%8.0lf"  \
    GPRINT:e:AVERAGE:"avg\:%8.0lf"  \
    GPRINT:e:MAX:"max\:%8.0lf"  \
    GPRINT:e:MIN:"min\:%8.0lf\n"  \
    LINE1:f#750F7DFF:"bdf_59_jp_matched"  \
    GPRINT:f:LAST:"     cur\:%8.0lf"  \
    GPRINT:f:AVERAGE:"avg\:%8.0lf"  \
    GPRINT:f:MAX:"max\:%8.0lf"  \
    GPRINT:f:MIN:"min\:%8.0lf\n" 

/usr/bin/rrdtool graph /mnt/python/wfq/monitor/image/data.png\
    --imgformat=PNG \
    --start=$timeend \
    --end=$timestart \
    --title='data-succed' \
    --base=1000 \
    --height=120 \
    --width=550 \
    --alt-autoscale-max \
    --lower-limit='0' \
    COMMENT:"From $daes  To $dats\c" \
    COMMENT:"  \n" \
    --vertical-label='' \
    --slope-mode \
    --font TITLE:10: \
    --font AXIS:7: \
    --font LEGEND:8: \
    --font UNIT:7: \
    DEF:a="/var/www/cacti-0.8.8a/rra/_df_56_succeed_446.rrd":'df_41_succeed':AVERAGE \
    DEF:b="/var/www/cacti-0.8.8a/rra/_df_56_succeed_446.rrd":'df_42_succeed':AVERAGE \
    DEF:c="/var/www/cacti-0.8.8a/rra/_df_56_succeed_446.rrd":'df_52_succeed':AVERAGE \
    DEF:d="/var/www/cacti-0.8.8a/rra/_df_56_succeed_446.rrd":'df_54_succeed':AVERAGE \
    DEF:e="/var/www/cacti-0.8.8a/rra/_df_56_succeed_446.rrd":'df_56_succeed':AVERAGE \
    DEF:f="/var/www/cacti-0.8.8a/rra/_df_56_succeed_446.rrd":'df_58_succeed':AVERAGE \
    CDEF:cdefa='TIME,1408777497,GT,a,a,UN,0,a,IF,IF,TIME,1408777497,GT,b,b,UN,0,b,IF,IF,TIME,1408777497,GT,c,c,UN,0,c,IF,IF,TIME,1408777497,GT,d,d,UN,0,d,IF,IF,TIME,1408777497,GT,e,e,UN,0,e,IF,IF,TIME,1408777497,GT,f,f,UN,0,f,IF,IF,+,+,+,+,+' \
    AREA:cdefa#FAFD9EFF:"df-succed-total"  \
    GPRINT:cdefa:LAST:"     cur\:%8.0lf\n"  \
    LINE1:a#00BF47FF:"df-41-succed"  \
    GPRINT:a:LAST:"        cur\:%8.0lf"  \
    GPRINT:a:AVERAGE:"avg\:%8.0lf"  \
    GPRINT:a:MAX:"max\:%8.0lf"  \
    GPRINT:a:MIN:"min\:%8.0lf\n"  \
    LINE1:b#004359FF:"df-42-succed"  \
    GPRINT:b:LAST:"        cur\:%8.0lf"  \
    GPRINT:b:AVERAGE:"avg\:%8.0lf"  \
    GPRINT:b:MAX:"max\:%8.0lf"  \
    GPRINT:b:MIN:"min\:%8.0lf\n"  \
    LINE1:c#FF3932FF:"df-52-cn-succed"  \
    GPRINT:c:LAST:"     cur\:%8.0lf"  \
    GPRINT:c:AVERAGE:"avg\:%8.0lf"  \
    GPRINT:c:MAX:"max\:%8.0lf"  \
    GPRINT:c:MIN:"min\:%8.0lf\n"  \
    LINE1:d#FF9900FF:"df-54-EU-west-succed"  \
    GPRINT:d:LAST:"cur\:%8.0lf"  \
    GPRINT:d:AVERAGE:"avg\:%8.0lf"  \
    GPRINT:d:MAX:"max\:%8.0lf"  \
    GPRINT:d:MIN:"min\:%8.0lf\n"  \
    LINE1:e#4668E4FF:"df-56-sa-east-succed"  \
    GPRINT:e:LAST:"cur\:%8.0lf"  \
    GPRINT:e:AVERAGE:"avg\:%8.0lf"  \
    GPRINT:e:MAX:"max\:%8.0lf"  \
    GPRINT:e:MIN:"min\:%8.0lf\n"  \
    LINE1:f#750F7DFF:"df-58-jp-succed"  \
    GPRINT:f:LAST:"     cur\:%8.0lf"  \
    GPRINT:f:AVERAGE:"avg\:%8.0lf"  \
    GPRINT:f:MAX:"max\:%8.0lf"  \
    GPRINT:f:MIN:"min\:%8.0lf\n" 
