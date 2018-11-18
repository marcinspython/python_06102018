import datetime

now = datetime.datetime.today()

print(now)
print(now.day)
print(now.weekday())

# x = datetime.datetime.strptime("2018/11/18", "%y/%m/%d")
# # print(x)

my_birthday = datetime.datetime(1983, 2, 18)
print(my_birthday.weekday())

delta = now - my_birthday

print(delta.days)
print(delta.microseconds)


for i in range(20):
    print(now + datetime.timedelta(hours=i))
