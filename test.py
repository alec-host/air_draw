import pytz
import time
import datetime

zone = pytz.timezone("Africa/Nairobi")
my_time_zone = zone.localize(datetime.datetime.now(),is_dst=True)

local_now = datetime.datetime.now().astimezone()
local_tz = local_now.tzinfo
local_tzname = local_tz.tzname(local_now)

if(local_tzname != 'E. Africa Standard Time'):
	EAT = my_time_zone + datetime.timedelta(hours = 3)
	date = EAT.strftime('%Y-%m-%d %H:%M:%S')
else:
	date = (my_time_zone.strftime('%Y-%m-%d %H:%M:%S'))