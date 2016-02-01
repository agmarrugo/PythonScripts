# -*- coding: utf-8 -*-
"""
Get Fridays
Created on Tue Jan 19 10:52:10 2016

@author: Andre
"""

import calendar
from tabulate import tabulate

c = calendar.Calendar(firstweekday=calendar.MONDAY)

year = 2016
months = [2, 3, 4, 5]
monthName = {k: v for k, v in enumerate(calendar.month_abbr)}

listFridays = []
for month in months:

    monthcal = c.monthdatescalendar(year, month)

    for week in monthcal:
        for day in week:
            if day.weekday() == calendar.FRIDAY and day.month == month:
                listFridays.append(
                    [monthName[day.month] + " " + str(day.day), " ", " "])

headers = ["Date", "Lecture", "Lecture Topics"]

print tabulate(listFridays, headers, tablefmt='pipe')
