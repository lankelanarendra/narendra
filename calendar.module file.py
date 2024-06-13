import calendar
for i in calendar.month_name:
    print(i)
x=list(calendar.month_name)
print(x)

for i in calendar.day_name:
    print(i)
y=list(calendar.day_name)
print(y)
print(type(y))

x=calendar.calendar(2024)
print(x)

y=calendar.month(2024,3)
print(y)
print("\n")
x=calendar.TextCalendar(calendar.MONDAY)
for i in range(1,13):
    y=x.formatmonth(2024,i)
    print(y)