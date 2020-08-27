### Timetils
A easy to use time util library for python

### Installation
`python3 -m pip install timetils`

### Usage
> For version 1.1.1
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

> For version >= 2.0.0
```python
import datetime
import timetils

formatter = timetils.Formatter()

# Make a timedelta object anyhow. 
delta = datetime.timedelta(days=45, seconds=288)

data = formatter.natural_delta(delta, as_string=True)
# if you set as_string = False data will be a BetterDelta class
# Output when as_string = True -> '1 Months 15 Days 4 Minutes and 48 Seconds'
# Output when as_dict = False -> <BetterDelta years=0, months=1, days=14, hours=0, minutes=4, seconds=48, string>
```

#### Available methods 
```python
natural_delta(timedelta, as_string)
natural_date(date, as_string)
natural_time(time, as_string, format)
natural_datetime(datetime, as_string)
```
