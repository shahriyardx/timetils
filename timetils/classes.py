class BetterDelta:
    """A better timedelta class"""

    def __init__(self, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def string(self):
        output = f"{f'{self.years} years ' if self.years > 0 else ''}{f'{self.months} months ' if self.months > 0 else ''}{f'{self.days} days ' if self.days > 0 else ''}{f'{self.hours} hours ' if self.hours > 0 else ''}{f'{self.minutes} minutes ' if self.minutes > 0 else ''}{f'{self.seconds} seconds' if self.seconds > 0 else ''}"
        output_list = [item for item in output.split(" ") if not item == ""]

        if len(output_list) > 2:
            first_part = output_list[: len(output_list) - 2]
            last_part = [item for item in output_list if item not in first_part]

            part1 = " ".join(first_part)
            part2 = " ".join(last_part)

            output = part1 + " and " + part2

        return output

    def __str__(self):
        return self.string

    def __repr__(self):
        return (
                "<BetterDelta years=%r, months=%r, days=%r, hours=%r, minutes=%r, seconds=%r, string>"
                % (
                    self.years,
                    self.months,
                    self.days,
                    self.hours,
                    self.minutes,
                    self.seconds,
                )
        )


class BetterDate:
    """A better datetime.date"""

    def __init__(self, date, day_short, day_full, month_short, month_full, year_short, year_full, date_string=None):
        self.date = date
        self.day_short = day_short
        self.day_full = day_full
        self.month_short = month_short
        self.month_full = month_full
        self.year_short = year_short
        self.year_full = year_full
        self.__date_string = date_string

    @property
    def string(self):
        return self.__date_string

    def __str__(self):
        return self.string

    def __repr__(self):
        return (
                "<BetterDate date=%r, day_short=%r, day_full=%r, month_short=%r, month_full=%r, year_short=%r, year_full=%r, string>"
                % (
                    self.date,
                    self.day_short,
                    self.day_full,
                    self.month_short,
                    self.month_full,
                    self.year_short,
                    self.year_full
                )
        )


class BetterTime:
    """A better time class"""

    def __init__(self, hour, minute, locale='NA', format=12, time_string=''):
        self.hour = hour
        self.minute = minute
        self.locale = locale
        self.format = format
        self.__time_string = time_string

    @property
    def string(self):
        return self.__time_string

    def __str__(self):
        return self.string

    def __repr__(self):
        return (
                "<BetterTime hour=%r, minute=%r, format=%r locale=%r, string>"
                % (
                    self.hour,
                    self.minute,
                    self.format,
                    self.locale
                )
        )


class BetterDatetime:
    """A better datetime class"""

    def __init__(self, date, day_short, day_full, month_short, month_full, year_short, year_full, hour, minute, locale, datetime_string):
        self.date = date
        self.day_short = day_short
        self.day_full = day_full
        self.month_short = month_short
        self.month_full = month_full
        self.year_short = year_short
        self.year_full = year_full
        self.hour = hour
        self.minute = minute
        self.locale = locale
        self.__datetime_string = datetime_string

    @property
    def string(self):
        return self.__datetime_string

    def __repr__(self):
        return (
                "<BetterDatetime date=%r, day_short=%r, day_full=%r, month_short=%r, month_full=%r, year_short=%r, year_full=%r, hour=%r, minute=%r, locale=%r, string>"
                % (
                    self.date,
                    self.day_short,
                    self.day_full,
                    self.month_short,
                    self.month_full,
                    self.year_short,
                    self.year_full,
                    self.hour,
                    self.minute,
                    self.locale
                )
        )