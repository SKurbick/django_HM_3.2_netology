import datetime

date = [datetime.date(2010, 7, 15),
        datetime.date(2010, 9, 13),
        datetime.date(2030, 5, 13),
        datetime.date(2020, 5, 13),
        datetime.date(2017, 5, 12),
        datetime.date(2024, 7, 5)]

d = sorted([str(da) for da in date])
print((d))
b = '2017-05-12'
print(d[d.index(b)])
