import datetime
from timetils.utils import gets

class Formatter:
	def __init__(self):
		pass

	def natural_delta(self, delta:datetime.timedelta, as_dict=False):
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

		if days == 0 and seconds == 0:
			if as_dict:
				return {'years': year, 'months': month, 'days' : day, 'hours': hour, 'minutes': minute, 'seconds': second}
			output = "Just now"
			return output

		year, days = gets.get_year(days)
		month, day = gets.get_month(days)
		hour, seconds = gets.get_hour(seconds)
		minute, second = gets.get_minutes(seconds)

		if as_dict:
			return {'years': year, 'months': month, 'days' : day, 'hours': hour, 'minutes': minute, 'seconds': second}
		output = f"{f'{year} years ' if year > 0 else ''}{f'{month} months ' if month > 0 else ''}{f'{day} days ' if day > 0 else ''}{f'{hour} hours ' if hour > 0 else ''}{f'{minute} minutes ' if minute > 0 else ''}{f'{second} seconds' if second > 0 else ''}"
		
		output_list = [item for item in output.split(" ") if not item == ""]

		if len(output_list) > 2:

			first_part = output_list[:len(output_list)-2]
			last_part = [item for item in output_list if item not in first_part]

			part1 = " ".join(first_part)
			part2 = " ".join(last_part)

			output = part1 + " and " + part2
		
		return output

	def natural_date(self, date:datetime.date, as_dict=False):
		"""
		datetime object to a human readable time

		Parameters
		- date				A datetime.date object
		- as_dict=False		Whether it should return a dictionary or a string. Default False

		return				string or dictionary according to as_dict kwarg
		"""
		if not isinstance(date, datetime.date):
			raise ValueError("date must be a object of 'datetime.date'")

		date = datetime.datetime.strftime(date, "%d")

		day_short = datetime.datetime.strftime(date, "%a")
		day_full = datetime.datetime.strftime(date, "%A")

		month_short = datetime.datetime.strftime(date, "%b")
		month_full = datetime.datetime.strftime(date, "%B")

		year_short = datetime.datetime.strftime(date, "%y")
		year_full = datetime.datetime.strftime(date, "%Y")

		if as_dict:
			return {'date': date, 'day_short': day_short, 'day_full': day_full, 'year_short': year_short, 'year_full': year_full, 'month_short': month_short, 'month_full': month_full, 'date': date}


		date_part = datetime.datetime.strftime(date, "%A, %d %b %Y")

		return date_part

	def natural_time(self, time:datetime.time, as_dict=False, format=12):
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
			raise ValueError("for must be either 12 or 24")

		if not isinstance(time, datetime.time):
			raise NotValidObject("time must be a object of 'datetime.time'")

		hour = time.hour
		minute = time.minute
		locale = None

		if format == 12:
			if hour >12:
				hour = hour-12
				locale = "PM"
			else:
				hour = hour
				locale = "AM"

			data = f"{hour}:{minute} {locale}"

		if format == 24:
			data = f"{hour}:{minute}"

		if as_dict and format == 12:
			return {'hour':hour, 'minute': minute, 'locale':locale}

		if as_dict and format == 24:
			return {'hour':hour, 'minute': minute}

		return data

	def natural_datetime(self, date_time:datetime.datetime, as_dict=False):
		"""
		datetime object to a human readable time

		Parameters
		- date_time			A datetime.datetime object
		- as_dict=False		Whether it should return a dictionary or a string.

		return				string or dictionary according to as_dict kwarg
		"""
		if not isinstance(date_time, datetime.datetime):
			raise ValueError('date_time must be a valid \'datetime.datetime\' object')

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

		if as_dict:
			return {'date': date, 'day_short': day_short, 'day_full': day_full, 'year_short': year_short, 'year_full': year_full, 'month_short': month_short, 'month_full': month_full, 'date': date, 'hour':hour, 'minute': minute, 'locale': locale}

		output = datetime.datetime.strftime(date_time, "%A, %d %b %Y at %I:%M %p")

		return output


