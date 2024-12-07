from datetime import datetime
#import datetime

now = datetime.now()
print(now)

current_date = datetime.today()
print(current_date)


current_date = now.date()

print(current_date)

formated_time = now.strftime("%d-%m-%Y %H:%M:%S")
print(formated_time)