def get_year(days):
    year = days // 365
    day = days % 365
    return [year, day]


def get_month(days):
    month = int(days // 30.417)
    day = int(days % 30.417)
    return [month, day]


def get_hour(seconds):
    hour = seconds // 3600
    second = seconds % 3600
    return [hour, second]


def get_minutes(seconds):
    minute = seconds // 60
    second = seconds % 60
    return [minute, second]
