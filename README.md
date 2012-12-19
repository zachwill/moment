moment
======

A Python library for dates/times inspired by [Moment.js](http://momentjs.com/docs/)
and the simplicity of Kenneth Reitz's [requests](http://docs.python-requests.org/)
library.


Installation
------------

`pip install moment`


Usage
-----

```python
import moment

# Create a moment from a string
moment.date("12-18-2012", "M-D-YYYY")

# Create a moment with strftime format
moment.date("12-18-2012", "%m-%d-%Y")

# Create a moment from the current datetime
moment.now()

# Create a moment with the UTC time zone
moment.utc("12-18-2012", "M-D-YYYY")

# Create a moment from a Unix timestamp
moment.unix(1355875153626)

# Update your moment to the correct UTC time
moment.date([2012, 12, 18]).local().to_date()

# Update your moment to a different time zone
moment.date(datetime(2012, 12, 18)).timezone("America/Chicago")
```
