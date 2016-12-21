"""
Where the magic happens.
"""

import calendar
from datetime import datetime, timedelta

from .utils import _iteritems


# ----------------------------------------------------------------------------
# Utilities
# ----------------------------------------------------------------------------

def add_month(date, number):
    """Add a number of months to a date."""
    month = date.month - 1 + number
    return update_month(date, month)


def subtract_month(date, number):
    """Subtract a number of months from a date."""
    month = date.month - 1 - number
    return update_month(date, month)


def update_month(date, month):
    """Create a new date with a modified number of months."""
    year = date.year + int(month / 12)
    month = month % 12 + 1
    day = min(date.day, calendar.monthrange(year, month)[1])
    return date.replace(year=year, month=month, day=day)


# ----------------------------------------------------------------------------
# Main functionality
# ----------------------------------------------------------------------------

class MutableDate(object):
    """Incapsulate mutable dates in one class."""

    def __init__(self, date):
        self._date = date

    def add(self, key=None, amount=None, **kwds):
        """Add time to the original moment."""
        if not key and not amount and len(kwds):
            for k, v in _iteritems(kwds):
                self.add(k, v)
        if key == 'years' or key == 'year':
            self._date = add_month(self._date, amount * 12)
        elif key == 'months' or key == 'month':
            self._date = add_month(self._date, amount)
        elif key == 'weeks' or key == 'week':
            self._date += timedelta(weeks=amount)
        elif key == 'days' or key == 'day':
            self._date += timedelta(days=amount)
        elif key == 'hours' or key == 'hour':
            self._date += timedelta(hours=amount)
        elif key == 'minutes' or key == 'minute':
            self._date += timedelta(minutes=amount)
        elif key == 'seconds' or key == 'second':
            self._date += timedelta(seconds=amount)
        elif key == 'milliseconds' or key == 'millisecond':
            self._date += timedelta(milliseconds=amount)
        elif key == 'microseconds' or key == 'microsecond':
            self._date += timedelta(microseconds=amount)
        return self

    def sub(self, key=None, amount=None, **kwds):
        """Just in case."""
        return self.subtract(key, amount, **kwds)

    def subtract(self, key=None, amount=None, **kwds):
        """Subtract time from the original moment."""
        if not key and not amount and len(kwds):
            for k, v in _iteritems(kwds):
                self.subtract(k, v)
        if key == 'years' or key == 'year':
            self._date = subtract_month(self._date, amount * 12)
        elif key == 'months' or key == 'month':
            self._date = subtract_month(self._date, amount)
        elif key == 'weeks' or key == 'week':
            self._date -= timedelta(weeks=amount)
        elif key == 'days' or key == 'day':
            self._date -= timedelta(days=amount)
        elif key == 'hours' or key == 'hour':
            self._date -= timedelta(hours=amount)
        elif key == 'minutes' or key == 'minute':
            self._date -= timedelta(minutes=amount)
        elif key == 'seconds' or key == 'second':
            self._date -= timedelta(seconds=amount)
        elif key == 'milliseconds' or key == 'millisecond':
            self._date -= timedelta(milliseconds=amount)
        elif key == 'microseconds' or key == 'microsecond':
            self._date -= timedelta(microseconds=amount)
        return self

    def replace(self, **kwds):
        """A Pythonic way to replace various date attributes."""
        for key, value in _iteritems(kwds):
            if key == 'years' or key == 'year':
                self._date = self._date.replace(year=value)
            elif key == 'months' or key == 'month':
                self._date = self._date.replace(month=value)
            elif key == 'days' or key == 'day':
                self._date = self._date.replace(day=value)
            elif key == 'hours' or key == 'hour':
                self._date = self._date.replace(hour=value)
            elif key == 'minutes' or key == 'minute':
                self._date = self._date.replace(minute=value)
            elif key == 'seconds' or key == 'second':
                self._date = self._date.replace(second=value)
            elif key == 'microseconds' or key == 'microsecond':
                self._date = self._date.replace(microsecond=value)
            elif key == 'weekday':
                self._weekday(value)
        return self

    def epoch(self, rounding=True, milliseconds=False):
        """Milliseconds since epoch."""
        zero = datetime.utcfromtimestamp(0)
        delta = self._date - zero
        seconds = delta.total_seconds()
        if rounding:
            seconds = round(seconds)
        if milliseconds:
            seconds *= 1000
        return seconds

    def _weekday(self, number):
        """Mutate the original moment by changing the day of the week."""
        weekday = self._date.isoweekday()
        if number < 0:
            days = abs(weekday - number)
        else:
            days = weekday - number
        delta = self._date - timedelta(days)
        self._date = delta
        return self

    def isoformat(self):
        """Return the date's ISO 8601 string."""
        return self._date.isoformat()

    def from_date(self, other):
        """Returns a readable interval since a date before"""
        return "{} ago".format(self._readable_timedelta(self - other))

    def from_now(self):
        """Returns a readable interval since now until the date"""
        return self.from_date(datetime.now())

    def to_date(self, other):
        """Returns a readable interval until a future date"""
        return "in {}".format(self._readable_timedelta(other - self))

    def to_now(self):
        """Returns a readable interval since the date until now"""
        return self.to_date(datetime.now())
    
    def _readable_timedelta(self, td):
        """Translate a timedelta into a readable and short string"""
        if td.total_seconds() < 0:
            td = -td

        m = 60
        h = 60*m
        d = 24*h
        rangemap = {
            (0, 45):        "a few seconds",
            (45, 90):       "a minute",
            (90, 45*m):     "{minutes} minutes",
            (45*m, 90*m):   "an hour",
            (90*m, 22*h):   "{hours} hours",
            (22*h, 36*h):   "a day",
            (36*h, 26*d):   "{days} days",
            (26*d, 45*d):   "a month",
            (45*d, 320*d):  "{months} months",
            (320*d, 548*d): "a year",
        }

        inrange = lambda value, lbound, ubound: value >= lbound and value < ubound

        for secrange, fmt in _iteritems(rangemap):
            if inrange(td.total_seconds(), secrange[0], secrange[1]):
                return fmt.format(
                    minutes=td.seconds/60, 
                    hours=td.seconds/3600, 
                    days=td.days,
                    months=td.days/30)
        else:
            return "{} years".format(td.days/365)

    def calendar_time(self, reference_date=datetime.now()):
        """Returns a readable string containing the time relative to the reference_date"""
        weekday = calendar.day_name[calendar.weekday(self.year, self.month, self.day)]
        td = self.copy().zero - MutableDate(reference_date).zero

        if td.days == 0:
            dayref = "Today"
        elif td.days == 1:
            dayref = "Tomorrow"
        elif td.days == -1:
            dayref = "Yesterday"
        elif td.days > 1 and td.days <= 7:
            dayref = "Next {}".format(weekday)
        elif td.days < -1 and td.days >= -7:
            dayref = "Last {}".format(weekday)
        else:
            return self.format("MM/DD/YYYY")

        hourref = "at {}".format(self.format("HH:mm"))

        return "{dayref} {hourref}".format(dayref=dayref, hourref=hourref)

    @property
    def zero(self):
        """Get rid of hour, minute, second, and microsecond information."""
        self.replace(hours=0, minutes=0, seconds=0, microseconds=0)
        return self

    @property
    def datetime(self):
        """Return the mutable date's inner datetime format."""
        return self._date

    @property
    def date(self):
        """Access the internal datetime variable."""
        return self._date

    @property
    def year(self):
        return self._date.year

    @property
    def month(self):
        return self._date.month

    @property
    def day(self):
        return self._date.day

    @property
    def weekday(self):
        return self._date.isoweekday()

    @property
    def hour(self):
        return self._date.hour

    @property
    def hours(self):
        return self._date.hour

    @property
    def minute(self):
        return self._date.minute

    @property
    def minutes(self):
        return self._date.minute

    @property
    def second(self):
        return self._date.second

    @property
    def seconds(self):
        return self._date.second

    @property
    def microsecond(self):
        return self._date.microsecond

    @property
    def microseconds(self):
        return self._date.microsecond

    @property
    def tzinfo(self):
        return self._date.tzinfo

    def __sub__(self, other):
        if isinstance(other, datetime):
            return self._date - other
        elif isinstance(other, type(self)) or issubclass(other.__class__, MutableDate):
            return self._date - other.date

    def __rsub__(self, other):
        return self.__sub__(other)

    def __lt__(self, other):
        if isinstance(other, datetime):
            return self._date < other
        elif isinstance(other, type(self)):
            return self._date < other.date

    def __le__(self, other):
        if isinstance(other, datetime):
            return self._date <= other
        elif isinstance(other, type(self)):
            return self._date <= other.date

    def __eq__(self, other):
        if isinstance(other, datetime):
            return self._date == other
        elif isinstance(other, type(self)):
            return self._date == other.date

    def __ne__(self, other):
        if isinstance(other, datetime):
            return self._date != other
        elif isinstance(other, type(self)):
            return self._date != other.date

    def __gt__(self, other):
        if isinstance(other, datetime):
            return self._date > other
        elif isinstance(other, type(self)):
            return self._date > other.date

    def __ge__(self, other):
        if isinstance(other, datetime):
            return self._date >= other
        elif isinstance(other, type(self)):
            return self._date >= other.date
