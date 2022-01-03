# fonts https://www.programiz.com/python-programming/datetime/strftime

from datetime import date, datetime, timezone, timedelta


print("-------------------------------")
today = date.today()  # It take the function now of date

print(today)
print(today.strftime("%d-%m-%Y"))  # date with format
print(today.strftime("%d-%b-%Y"))  # date with abreviate month
print(today.strftime("%d-%B-%Y"))  # date with month

print("-------------------------------")
now = datetime.now()

print(now)  # currenctly time
print(now.strftime("%d-%b-%Y -- %H:%M:%S %p"))  # time with format

time = "20-September-2021 -- 12:30"
# this function give format to a string time it need the same format in both string-strptime to match
print(datetime.strptime(time, "%d-%B-%Y -- %H:%M"))
print(datetime.timestamp(now))  # this return a timestamp


print("-----------Range Time---------------")

startDate = "2021-11-01"
endDate = "2021-11-03"

start_date_formated = datetime.strptime(startDate, "%Y-%m-%d")
end_date_formated = datetime.strptime(endDate, "%Y-%m-%d")

start_day = start_date_formated.strftime("%d")
end_day = end_date_formated.strftime("%d")

print(int(start_day))

for d in range(int(start_day) - 1, int(end_day)):
    future_date = start_date_formated + timedelta(days=d)
    print(future_date.strftime("%Y-%m-%d"))


# timedelta(
#     days=10,
#     seconds=3,
#     microseconds=5,
#     milliseconds=3200,
#     minutes=5,
#     hours=12,
#     weeks=6
# )
print("-------------------------------")
dates = "2021-11-26 19:29:00.0"

print(datetime.strftime(
    datetime.now(), "%Y-%m-%d %H:%M"))
