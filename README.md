### Timetils
A easy to use time util library for python

### Installation
`python3 -m pip install timetils`

### Usage
```python
import datetime
import timetils

formatter = timetils.Formatter()

# Make a timedelta object anyhow. 
delta = datetime.timedelta(days=45, seconds=288)

data = formatter.natural_delta(delta, as_dict=False)
# if you set as_dict = True data will be a dict of years, months, days, hours, minutes and seconds
# Output when as_dict = False -> '1 Months 15 Days 4 Minutes and 48 Seconds'
# Output when as_dict = True -> {'years': 0, 'months': 1, 'days': 15, 'hours': 0, 'minutes': 4, 'seconds': 48}
```

#### Available methods 
```python
natural_delta(timedelta, as_dict)
natural_date(date, as_dict)
natural_time(time, as_dict, format)
natural_datetime(datetime, as_dict)
```
