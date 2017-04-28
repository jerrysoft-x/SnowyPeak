from datetime import datetime, timedelta, timezone
import time

now = datetime.now()
# lt = time.localtime()
# str = time.strftime('%z', lt)
# print (str)
# print(lt.timezone())
utcNow = datetime.utcnow()
tz_offset = now - utcNow
print(tz_offset)
print(timezone(tz_offset))
now = now.replace(tzinfo=timezone(tz_offset))
print(now)
