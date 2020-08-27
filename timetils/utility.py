import datetime


def date_and_time_to_datetime(date=None, time=None):
    """Get datetime.datetime object from a only datetime.date or datetime.time object"""

    if date and time is None:
        time = datetime.time.min

    if date is None and time:
        date = datetime.date.min

    if date is None and time is None:
        date = datetime.date.min
        time = datetime.time.min

    date_time = datetime.datetime.combine(date, time)

    return date_time
