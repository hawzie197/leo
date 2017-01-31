# Author: Michael Hawes
# Date: 25 December 2016
# Project Leo
# date_time.py

import time, datetime
from subprocess import call

week = {"Mon":"Monday","Tue":"Tuesday",
        "Wed":"Wednesday","Thu":"Thursday",
        "Fri":"Friday","Sat":"Saturday","Sun":
        "Sunday"}

months = {"Jan":"January","Feb":"February",
        "Mar":"March","Apr":"April","May":"May",
        "Jun":"June","Jul":"July","Aug":"August",
        "Sep":"September","Oct":"October","Nov":"November",
        "Dec":"December"}

days_month = {"01":"first","02":"second","03":"third",
    "04":"fourth","05":"fifth","06":"sixth","07":"seventh",
    "08":"eighth","09":"ninth","10":"tenth","11":"eleventh",
    "12":"twelfth","13":"thirteenth","14":"fourteenth","15":"fifteenth",
    "16":"sixteenth","17":"seventeenth","18":"eighteenth","19":"nineteenth",
    "20":"twentieth","21":"twenty-first","22":"twenty-second","23":"twenty-third",
    "24":"twenty-fourth","25":"twenty-fifth","26":"twenty-sixth","27":"twenty-seventh","28":"twenty-eighth",
    "29":"twenty-ninth","30":"thirtieth","31":"thirty-first"}

class DateTime:

    def get_date(self):
        """
        returns the current date
        """
        today = datetime.date.today()

        day = "{:%a}".format(today)
        month = "{:%b}".format(today)
        day_month = "{:%d}".format(today)
        year = "{:%Y}".format(today)

        day = week[day]
        month = months[month]
        day_month = days_month[day_month]

        date = day + ',' + month + ',' + day_month + ',' + year
        call(["espeak", "-ven-us+m1", "-s170","Today's date is" + date])


    def get_time(self):
        """
        returns the the current time
        """
        hour = time.strftime('%H')
        print(hour)
        new_hour = abs(int(hour)-12)
        current_time = time.strftime('%M')   # ex.  06:23
        if int(hour) >= 12:
            call(["espeak", "-ven-us+m1", "-s170","It is currently " + str(new_hour) + ':' + current_time + 'P.M.'])
        else:
            call(["espeak", "-ven-us+m1", "-s170","It is currently " + str(new_hour) + ':' + current_time + 'A.M.'])

    def get_datetime(self):
        """
        returns the current date and time
        """
        today = datetime.date.today()

        day = "{:%a}".format(today)
        month = "{:%b}".format(today)
        day_month = "{:%d}".format(today)
        year = "{:%Y}".format(today)

        day = week[day]
        month = months[month]
        day_month = days_month[day_month]

        date = day + ',' + month + ',' + day_month + ',' + year
        hour = time.strftime('%H')
        hour = abs(int(hour)-12)
        current_time = time.strftime('%M')   # ex.  06:23
        call(["espeak", "-ven-us+m1", "-s170","It is currently " + str(hour) + ':' + current_time + 'on' + date])
