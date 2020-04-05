import time
import datetime
import calendar;
cal = calendar.month(2020,2)

print(cal)
print(calendar.prcal(2020))


print(datetime.datetime.now())

print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
if datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day,8)<datetime.datetime.now()<datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day,16):
    print("Working hours....")
else:
    print("fun hours")
for i in range(0,8):
    print(i)
    time.sleep(1)
