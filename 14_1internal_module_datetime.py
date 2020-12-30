#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#datetime
from datetime import datetime, timedelta, timezone
now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015, 4, 19, 12, 20, 18)
print(dt)
print(dt.timestamp())
# 注意Python的timestamp是一个浮点数，整数位表示秒。
t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))
print(now.strftime('%a, %b %d %H:%M'))

# datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
print(now + timedelta(hours=10))
# datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
print(now - timedelta(days=1))
# datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
print(now + timedelta(days=2, hours=12))
# datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)

# 本地时间转换为UTC时间
tz_utc_ca = timezone(timedelta(hours=-8))
print(datetime.now())
dt = now.replace(tzinfo=tz_utc_ca)
print(dt)

# 时区转换
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：

# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    #获取时区
    zone = re.match(r'UTC([+-]\d+):(\d{2})', tz_str)

    tz_utc = timezone(timedelta(hours=int(zone.group(1)),minutes=int(zone.group(2))))
    tz_dt = cday.replace(tzinfo=tz_utc)
    print(tz_dt.timestamp())
    return tz_dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')