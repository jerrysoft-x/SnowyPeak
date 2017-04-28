from datetime import datetime
now = datetime.now()
print(now.strptime('2017-4-19 16:19:30', '%Y-%m-%d %H:%M:%S'))