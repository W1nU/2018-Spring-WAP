from datetime import datetime, timedelta

time = datetime.now()

if int(time.strftime("%M")) >= 40:
    basetime = time.strftime("%H00")
    print(basetime)
date_today = datetime.now() - timedelta(days = 1)
print(date_today)
