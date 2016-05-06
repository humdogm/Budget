from datetime import *
import o

url = "http://mavmoney.uta.edu"
os.startfile(url)

moneyleft = float(input(" How much money do you have left? \n $"))

Today = datetime.today()

LastDay = date(2016,5,14)

Holidays = [date(2016,3,12), date(2016,3,13), date(2016,3,19)]

TodayDate = date(Today.year,Today.month,Today.day)
#TodayDate = date(2016,3,9)
TodayAdd = TodayDate

diff = (LastDay - TodayDate).days

WeekendDays = -int(len(Holidays))
for day in Holidays:
	if day < TodayDate:
		WeekendDays += 1

for i in range(0, diff-1):
	if TodayAdd.weekday() == 5 or TodayAdd.weekday() == 6:
		WeekendDays += 1
	TodayAdd += timedelta(days = 1)
	
if TodayDate.weekday() < 5:
	print("You can spend $"  + str((moneyleft/WeekendDays)/1.0825)[0:8] + " excluding tax on Saturday.")
	print("You can spend $"  + str(moneyleft/WeekendDays)[0:8] + " including tax on Saturday.")
else:
	print("You can spend $"  + str((moneyleft/WeekendDays)/1.0825)[0:8] + " excluding tax today.")
	print("You can spend $"  + str(moneyleft/WeekendDays)[0:8] + " including tax today")