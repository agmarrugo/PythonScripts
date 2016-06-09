# -*- coding: utf-8 -*-
"""
Get Fridays
Created on Tue Jan 19 10:52:10 2016

@author: Andre
"""

import calendar
from tabulate import tabulate
import holidays

c = calendar.Calendar(firstweekday=calendar.MONDAY)

co_holidays = holidays.CO()

year = 2016
months = [2, 3, 4, 5, 6]
monthName = {k: v for k, v in enumerate(calendar.month_abbr)}
class_day = calendar.MONDAY

listFridays = []
for month in months:

    monthcal = c.monthdatescalendar(year, month)

    for week in monthcal:
        for day in week:
            if (day.weekday() == class_day and day.month == month and
                    day not in co_holidays):
                listFridays.append(
                    [monthName[day.month] + " " + str(day.day), " ", " "])

# headers = ["Date", "Lecture", "Lecture Topics"]
headers = ["Fecha", u"Tópico", "Responsable"]

print tabulate(listFridays, headers, )
