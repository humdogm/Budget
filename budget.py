from datetime import *
moneyleft = float(input(" How much money do you have left? \n $"))

Today = datetime.today()

LastDay = date(2016,5,14)

SpringBreakWeekendDays = [date(2016,3,12), date(2016,3,13), date(2016,3,19)]

TodayDate = date(Today.year,Today.month,Today.day)
#TodayDate = date(2016,3,9)
TodayAdd = TodayDate

diff = (LastDay - TodayDate).days

WeekendDays = -3
for day in SpringBreakWeekendDays:
	if day <= TodayDate:
		WeekendDays += 1

if TodayDate.weekday() < 5:
	print("Today isn't a weekend!")
	
else:
	for i in range(0, diff-1):
		if TodayAdd.weekday() == 5 or TodayAdd.weekday() == 6:
			WeekendDays += 1
		TodayAdd += timedelta(days = 1)
	print("You can spend $"  + str((moneyleft/WeekendDays)/1.0825)[0:7] + " excluding tax.")
	print("You can spend $"  + str(moneyleft/WeekendDays)[0:7] + " including tax.")