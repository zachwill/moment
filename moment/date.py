"""
Where the magic happens.
"""

import calendar
from datetime import  datetime, timedelta


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
    year = date.year + month / 12
    month = month % 12 + 1
    day = min(date.day, calendar.monthrange(year, month)[1])
    return datetime(year, month, day, date.hour, date.minute, date.second,
                    date.microsecond, date.tzinfo)


class MutableDate(object):
    """Incapsulate mutable dates in one class."""

    def __init__(self, date):
        self._date = date

    def add(self, key=None, amount=None, **kwds):
        """Add time to the original moment."""
        if not key and not amount and len(kwds):
            for k, v in kwds.iteritems():
                self.add(k, v)
        if key == 'years':
            self._date = add_month(self._date, amount * 12)
        elif key == 'months':
            self._date = add_month(self._date, amount)
        elif key == 'weeks':
            self._date += timedelta(weeks=amount)
        elif key == 'days':
            self._date += timedelta(days=amount)
        elif key == 'hours':
            self._date += timedelta(hours=amount)
        elif key == 'minutes':
            self._date += timedelta(minutes=amount)
        elif key == 'seconds':
            self._date += timedelta(seconds=amount)
        elif key == 'milliseconds':
            self._date += timedelta(milliseconds=amount)
        elif key == 'microseconds':
            self._date += timedelta(microseconds=amount)
        return self

    def sub(self, key=None, amount=None, **kwds):
        """Just in case."""
        return self.subtract(key, amount, **kwds)

    def subtract(self, key=None, amount=None, **kwds):
        """Subtract time from the original moment."""
        if not key and not amount and len(kwds):
            for k, v in kwds.iteritems():
                self.subtract(k, v)
        if key == 'years':
            self._date = subtract_month(self._date, amount * 12)
        elif key == 'months':
            self._date = subtract_month(self._date, amount)
        elif key == 'weeks':
            self._date -= timedelta(weeks=amount)
        elif key == 'days':
            self._date -= timedelta(days=amount)
        elif key == 'hours':
            self._date -= timedelta(hours=amount)
        elif key == 'minutes':
            self._date -= timedelta(minutes=amount)
        elif key == 'seconds':
            self._date -= timedelta(seconds=amount)
        elif key == 'milliseconds':
            self._date -= timedelta(milliseconds=amount)
        elif key == 'microseconds':
            self._date -= timedelta(microseconds=amount)
        return self

    def epoch(self, rounding=True):
        """Milliseconds since epoch."""
        zero = datetime.utcfromtimestamp(0)
        delta = self._date - zero
        seconds = delta.total_seconds()
        if rounding:
            seconds = round(seconds)
        return seconds

    def years(self, number):
        """Mutate the original moment by changing the year."""
        if number < 0:
            return self.subtract('years', abs(number))
        self._date = self._date.replace(year=number)
        return self

    def months(self, number):
        """Mutate the original moment by changing the month."""
        if number < 0:
            return self.subtract('months', abs(number))
        self._date = self._date.replace(month=number)
        return self

    def days(self, number):
        """Mutate the original moment by changing the day of the month."""
        if number < 0:
            return self.subtract('days', abs(number))
        self._date = self._date.replace(day=number)
        return self

    def weekdays(self, number):
        """Just in case."""
        return self.weekday(number)

    def weekday(self, number):
        """Mutate the original moment by changing the day of the week."""
        weekday = self._date.isoweekday()
        if number < 0:
            days = abs(weekday - number)
        else:
            days = weekday - number
        delta = self._date - timedelta(days)
        self._date = delta
        return self

    def hours(self, number):
        """Mutate the original moment by changing the hour."""
        if number < 0:
            return self.subtract('hours', abs(number))
        self._date = self._date.replace(hour=number)
        return self

    def minutes(self, number):
        """Mutate the original moment by changing the minutes."""
        if number < 0:
            return self.subtract('minutes', abs(number))
        self._date = self._date.replace(minute=number)
        return self

    def seconds(self, number):
        """Mutate the original moment by changing the seconds."""
        if number < 0:
            return self.subtract('seconds', abs(number))
        self._date = self._date.replace(second=number)
        return self

    def microseconds(self, number):
        """Mutate the original moment by changing the seconds."""
        if number < 0:
            return self.subtract('microseconds', abs(number))
        self._date = self._date.replace(microsecond=number)
        return self

    def datetime(self):
        """Return the mutable date's inner datetime format."""
        return self._date

    def to_date(self):
        """Return the mutable date's inner datetime format."""
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
    def hour(self):
        return self._date.hour

    @property
    def minute(self):
        return self._date.minute

    @property
    def second(self):
        return self._date.second

    @property
    def microsecond(self):
        return self._date.microsecond

    @property
    def tzinfo(self):
        return self._date.tzinfo

    def __sub__(self, other):
        if isinstance(other, datetime):
            return self._date - other
        elif isinstance(other, type(self)):
            return self._date - other.to_date()

    def __lt__(self, other):
        if isinstance(other, datetime):
            return self._date < other
        elif isinstance(other, type(self)):
            return self._date < other.to_date()

    def __le__(self, other):
        if isinstance(other, datetime):
            return self._date <= other
        elif isinstance(other, type(self)):
            return self._date <= other.to_date()

    def __eq__(self, other):
        if isinstance(other, datetime):
            return self._date == other
        elif isinstance(other, type(self)):
            return self._date == other.to_date()

    def __ne__(self, other):
        if isinstance(other, datetime):
            return self._date != other
        elif isinstance(other, type(self)):
            return self._date != other.to_date()

    def __gt__(self, other):
        if isinstance(other, datetime):
            return self._date > other
        elif isinstance(other, type(self)):
            return self._date > other.to_date()

    def __ge__(self, other):
        if isinstance(other, datetime):
            return self._date >= other
        elif isinstance(other, type(self)):
            return self._date >= other.to_date()
