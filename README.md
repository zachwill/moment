moment
======

A Python library for dealing with dates/times. Inspired by both
[**Moment.js**](http://momentjs.com/docs/) and the simplicity of Kenneth Reitz's
[**Requests**](http://docs.python-requests.org/) library. Ideas were also taken from
the [**Times**](https://github.com/nvie/times) Python module.


Installation
------------

This is extremely alpha software right now. Eventually you'll be able to install
it with:

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
moment.date([2012, 12, 18]).to_date()

# Update your moment's time zone
moment.date(datetime(2012, 12, 18)).timezone('US/Central')

# Alter the moment's datetime with a different locale
moment.utcnow().locale('US/Eastern').to_date()

# Create and format a moment using JavaScript semantics
moment.now().format('YYYY-M-D')

# Create and format a moment with strftime semantics
moment.date((2012, 12, 18)).strftime('%Y-%m-%d')
```

Chaining
--------

Moment allows you to chain commands, which turns out to be super useful.

```python
# Customize your moment by chaining commands
moment.date([2012, 12, 18]).add('days', 2).subtract('weeks', 3).to_date()

# Imagine trying to do this with datetime, right?
moment.utcnow().add('years', 3).add('months', 2).format('YYYY-M-D h:m A')

# In addition to adding/subtracting, we can also set values
moment.now().hours(5).minutes(15).seconds(0).epoch()

# And, if you'd prefer to keep the microseconds on your epoch value
moment.now().hours(5).minutes(15).seconds(0).epoch(False)
```
