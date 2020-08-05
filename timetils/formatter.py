import datetime
from timetils.utils import gets
from timetils.classes import BetterDelta, BetterDate, BetterTime, BetterDatetime

__version__ = "1.1.0"
__author__ = "shahriyardx"


class Formatter:
    def __init__(self):
        self.__version__ = __version__
        self.__author__ = __author__

    def __repr__(self):
        return "<class timetils.Formatter>"

    def __str__(self):
        return "<class timetils.Formatter>"

    def natural_delta(self, delta: datetime.timedelta, as_string=True):
        """
        Convert a timedelta object to string.

        Parameters
        - delta			A time delta object
        - as_dict=False	Whether it should return a dictionary or a string.

        return			String or dictionary according to as_dict kwarg
        """

        output = ""
        days = delta.days
        seconds = delta.seconds

        year = 0
        month = 0
        day = 0
        hour = 0
        minute = 0
        second = 0

        year, days = gets.get_year(days)
        month, day = gets.get_month(days)
        hour, seconds = gets.get_hour(seconds)
        minute, second = gets.get_minutes(seconds)

        time = BetterDelta(year, month, day, hour, minute, second)

        if days == 0 and seconds == 0:
            if not as_string:
                return time
            output = "Just now"
            return output

        if not as_string:
            return time

        output = time.string
        return output

    def natural_date(self, date: datetime.date, as_string=True):
        """
        datetime object to a human readable time

        Parameters
        - date				A datetime.date object
        - as_dict=False		Whether it should return a dictionary or a string. Default False

        return				string or dictionary according to as_dict kwarg
        """
        if not isinstance(date, datetime.date):
            raise ValueError("date must be a object of 'datetime.date'")

        dates = datetime.datetime.strftime(date, "%d")

        day_short = datetime.datetime.strftime(date, "%a")
        day_full = datetime.datetime.strftime(date, "%A")

        month_short = datetime.datetime.strftime(date, "%b")
        month_full = datetime.datetime.strftime(date, "%B")

        year_short = datetime.datetime.strftime(date, "%y")
        year_full = datetime.datetime.strftime(date, "%Y")

        date_part = datetime.datetime.strftime(date, "%A, %d %b %Y")

        better_date = BetterDate(dates, day_short, day_full, month_short, month_full, year_short, year_full, date_part)

        if as_string:
            return better_date.string

        return better_date

    def natural_time(self, time: datetime.time, as_string=True, format=12):
        """
        datetime object to a human readable time

        Parameters
        - time				a datetime.time object
        - as_dict=False		Whether it should return a dictionary or a string.
        - format=12			12/24 hour time format

        return				string or dictionary according to as_dict kwarg
        """

        valids = [12, 24]

        if format not in valids:
            raise ValueError("format must be either 12 or 24")

        if not isinstance(time, datetime.time):
            raise ValueError("time must be a object of 'datetime.time'")

        hour = time.hour
        minute = time.minute
        locale = None

        if format == 12:
            if hour > 12:
                hour = hour - 12
                locale = "PM"
            else:
                hour = hour
                locale = "AM"

            data = f"{hour}:{minute} {locale}"

        if format == 24:
            data = f"{hour}:{minute}"

        time = BetterTime(hour, minute, format, locale, data)

        if as_string:
            return time.string

        return time

    def natural_datetime(self, date_time: datetime.datetime, as_string=True):
        """
        datetime object to a human readable time

        Parameters
        - date_time			A datetime.datetime object
        - as_dict=False		Whether it should return a dictionary or a string.

        return				string or dictionary according to as_dict kwarg
        """
        if not isinstance(date_time, datetime.datetime):
            raise ValueError("date_time must be a valid 'datetime.datetime' object")

        date = datetime.datetime.strftime(date_time, "%d")

        day_short = datetime.datetime.strftime(date_time, "%a")
        day_full = datetime.datetime.strftime(date_time, "%A")

        month_short = datetime.datetime.strftime(date_time, "%b")
        month_full = datetime.datetime.strftime(date_time, "%B")

        year_short = datetime.datetime.strftime(date_time, "%y")
        year_full = datetime.datetime.strftime(date_time, "%Y")

        hour = datetime.datetime.strftime(date_time, "%I")
        minute = datetime.datetime.strftime(date_time, "%m")
        locale = datetime.datetime.strftime(date_time, "%p")

        output = datetime.datetime.strftime(date_time, "%A, %d %b %Y at %I:%M %p")

        datas = {
                "date": date,
                "day_short": day_short,
                "day_full": day_full,
                "year_short": year_short,
                "year_full": year_full,
                "month_short": month_short,
                "month_full": month_full,
                "hour": hour,
                "minute": minute,
                "locale": locale,
                "datetime_string": output
            }

        better_datetime = BetterDatetime(**datas)

        if as_string:
            return better_datetime.string

        return better_datetime
