import math
import random
import datetime
number = -3.147
a = 22, 33
print(abs(number)) #القيمة المطلقة
print(round(number))#يقرب لاقرب عدد صحيح
print(round(number, 2)) #سقرب الخانة 2 بعد الفاصلة
print(pow(number, 2)) #power of 2
print(max(1,4,6,99))
print(min(1,4,6,99))
print(sum(a))
print(math.sqrt(144)) #الجذر التربيعي من مكتبة ماث
print(math.remainder(9, 3)) #باقي القسمة من مكتبة ماث
print(random.randint(1,100)) #random number from 1 to 100
## date time ##
date = datetime.date(2026,1,1) # y, m ,d
print(date)
print(date.year)
print(date.month)
time = datetime.time(12, 0,0) # h, m ,s
print(time)
print(time.hour)
print(time.minute)
now = datetime.datetime.today() #الوقت الحالي 
print(now)
print(now.year)
print(now.day)
print(now.hour)
print(date.strftime('%A %B %Y')) #سطبع التاريخ كلام + طويل
print(date.strftime('%a %b %y'))  #سطبع التاريخ كلام + مختصر
print(time.strftime('%I %M %S'))  #يطبع الوقت بتنسيق مختلف -بدون :-
