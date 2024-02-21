# ex1
from datetime import datetime, timedelta

current_data = datetime.now()
new_data = current_data - timedelta(days = 5)

print("Current Data: ", current_data)
print("New Date: ", new_data)

print("---------")
# ex2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

print("today: " ,today)
print("yesterday: ", yesterday)
print("tomorrow: " ,tomorrow)

print("---------")
# ex3
from datetime import datetime, timedelta

cur_datetime = datetime.now()
micro_datetime = cur_datetime.replace(microsecond=0)

print("current datetime: ", cur_datetime)
print("withmicrotime: ", micro_datetime)

print("---------")
# ex4
from datetime import datetime , timedelta

date1 = datetime.now()
date2 = date1 - timedelta(days= 1)

timedif= date1 - date2
dif_in_sec = timedif.total_seconds()

print(dif_in_sec)
