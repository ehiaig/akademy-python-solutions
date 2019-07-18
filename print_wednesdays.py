from datetime import datetime, timedelta, time, date
import calendar

# today = datetime(year=2001, month=1, day=1)

# print(f"{today:}")
# print(f"{today:%B}")
# print(f"{today:%A}")

# print(f"{today:%B %d, %Y}")

#print days that are wednesday in year 2001
# year = 2001
# d_o = date(year, 1, 1)
# d_o += timedelta(days=3-d_o.isoweekday())

# while d_o.year <= year:
# 	print(f"{d_o:%A}", d_o)
# 	d_o += timedelta(days=7)


#loop through, find all wednesday from 2001 to 2100, print wednesdays that fall on last day of the month.
year = 2001
d_o = date(year, 1, 1)
d_o += timedelta(days=3-d_o.isoweekday())
end_year = 2100

while d_o.year <= 2100:
	# print(f"{d_o:%A}", d_o)

	for month in range(1,13):
		new = str(d_o)

		start_date  = datetime.strptime(new, '%Y-%m-%d')
		last_wed = max(week[-1] for week in new)
		print(last_wed)

	d_o += timedelta(days=7)






# def weekday_count(start, end):
#   start_date  = datetime.datetime.strptime(start, '%d/%m/%Y')
#   end_date    = datetime.datetime.strptime(end, '%d/%m/%Y')
#   week        = {}
#   for i in range((end_date - start_date).days):
#     day       = calendar.day_name[(start_date + datetime.timedelta(days=i+1)).weekday()]
#     week[day] = week[day] + 1 if day in week else 1
#   return week
# print(weekday_count("01/01/2001", "31/12/2100"))
