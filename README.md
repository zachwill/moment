moment
======

[![Build Status](https://travis-ci.org/zachwill/moment.svg?branch=master)](https://travis-ci.org/zachwill/moment)

A Python library for dealing with dates/times. Inspired by both
[**Moment.js**][moment] and the simplicity of Kenneth Reitz's
[**Requests**][requests] library. Ideas were also taken from the
[**Times**][times] Python module.

[moment]: http://momentjs.com/docs/
[requests]: http://docs.python-requests.org/
[times]: https://github.com/nvie/times


Installation
------------

I would advise that this is alpha-quality software.

`pip install moment`


Usage
-----

```python
import moment
from datetime import datetime

# Create a moment from a string
moment.date("12-18-2012", "M-D-YYYY")

# Create a moment with strftime format
moment.date("12-18-2012", "%m-%d-%Y")

# By default, the "%Y-%m-%d" strftime format is used
moment.date("2012-12-18")

# Create a moment from the current datetime
moment.now()

# The moment can also be UTC-based
moment.utcnow()

# Create a moment with the UTC time zone
moment.utc("2012-12-18", "YYYY-M-D")

# Create a moment from a Unix timestamp
moment.unix(1355875153626)

# Create a moment from a Unix UTC timestamp
moment.unix(1355875153626, utc=True)

# Return a datetime instance
moment.date(2012, 12, 18).date

# We can do the same thing with the UTC method
moment.utc(2012, 12, 18).date

# Create and format a moment using Moment.js semantics
moment.now().format("YYYY-M-D")

# Create and format a moment with strftime semantics
moment.date(2012, 12, 18).strftime("%Y-%m-%d")

# Update your moment's time zone
moment.date(datetime(2012, 12, 18)).locale("US/Central").date

# Alter the moment's UTC time zone to a different time zone
moment.utcnow().timezone("US/Eastern").date

# Set and update your moment's time zone. For instance, I'm on the
# west coast, but want NYC's current time.
moment.now().locale("US/Pacific").timezone("US/Eastern")

# In order to manipulate time zones, a locale must always be set or
# you must be using UTC.
moment.utcnow().timezone("US/Eastern").date

# You can also clone a moment, so the original stays unaltered
now = moment.utcnow().timezone("US/Pacific")
future = now.clone().add(weeks=2)

# Return human readable intervals for past dates...
d = moment.date("2012-12-18")
d.from_date(moment.date("2012-12-17")) # a day ago

# ... with reference to now
d = moment.now().subtract('hour', 4)
d.from_now() # 4 hours ago

# ... or future dates
d = moment.date("2012-12-18")
d.to_date(moment.date("2013-01-17")) # in a month

# Human readable calendar dates
d = moment.now().subtract('hour', 10)
d.calendar_time()

```

Chaining
--------

Moment allows you to chain commands, which turns out to be super useful.

```python
# Customize your moment by chaining commands
moment.date(2012, 12, 18).add(days=2).subtract(weeks=3).date

# Imagine trying to do this with datetime, right?
moment.utcnow().add(years=3, months=2).format("YYYY-M-D h:m A")

# You can use multiple keyword arguments
moment.date(2012, 12, 19).add(hours=1, minutes=2, seconds=3)

# And, a similar subtract example...
moment.date(2012, 12, 19, 1, 2, 3).subtract(hours=1, minutes=2, seconds=3)

# In addition to adding/subtracting, we can also replace values
moment.now().replace(hours=5, minutes=15, seconds=0).epoch()

# And, if you'd prefer to keep the microseconds on your epoch value
moment.now().replace(hours=5, minutes=15, seconds=0).epoch(rounding=False)

# Years, months, and days can also be set
moment.now().replace(years=1984, months=1, days=1, hours=0, minutes=0, seconds=0)

# Also, datetime properties are available
moment.utc(2012, 12, 19).year == 2012

# Including plural ones (since I'm bad at remembering)
moment.now().seconds

# We can also manipulate to preferred weekdays, such as Monday
moment.date(2012, 12, 19).replace(weekday=1).strftime("%Y-%m-%d")

# Or, this upcoming Sunday
moment.date("2012-12-19").replace(weekday=7).date

# We can even go back to two Sundays ago
moment.date(2012, 12, 19).replace(weekday=-7).format("YYYY-MM-DD")

# It's also available as a property
moment.utcnow().weekday

# And, there's an easy way to zero out the hours, minutes, and seconds
moment.utcnow().zero
```
