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

    def add(self, key, amount):
        """Add time to the original moment."""
        if key == 'years':
            self._date = add_month(self._date, amount * 12)
        elif key == 'months':
            self._date = add_month(self._date, amount)
        elif key == 'weeks':
            self._date += timedelta(weeks=amount)
        elif key == 'days':
            self._date += timedelta(days=amount)
        elif key == 'minutes':
            self._date += timedelta(minutes=amount)
        elif key == 'seconds':
            self._date += timedelta(seconds=amount)
        elif key == 'milliseconds':
            self._date += timedelta(milliseconds=amount)
        elif key == 'microseconds':
            self._date += timedelta(microseconds=amount)
        return self

    def subtract(self, key, amount):
        """Subtract time from the original moment."""
        if key == 'years':
            self._date = subtract_month(self._date, amount * 12)
        elif key == 'months':
            self._date = subtract_month(self._date, amount)
        elif key == 'weeks':
            self._date -= timedelta(weeks=amount)
        elif key == 'days':
            self._date -= timedelta(days=amount)
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
        seconds = delta.total_seconds() * 1000
        if rounding:
            seconds = round(seconds)
        return seconds

    def year(self, number):
        """Mutate the original moment by changing the year."""
        if number < 0:
            return self.subtract('years', abs(number))
        date = self._date
        self._date = datetime(number, date.month, date.day, date.hour, date.minute,
                              date.second, date.microsecond, date.tzinfo)
        return self

    def month(self, number):
        """Mutate the original moment by changing the month."""
        if number < 0:
            return self.subtract('months', abs(number))
        date = self._date
        self._date = datetime(date.year, number, date.day, date.hour, date.minute,
                              date.second, date.microsecond, date.tzinfo)
        return self

    def day(self, number):
        """Mutate the original moment by changing the day of the month."""
        if number < 0:
            return self.subtract('days', abs(number))
        date = self._date
        self._date = datetime(date.year, date.month, number, date.hour, date.minute,
                              date.second, date.microsecond, date.tzinfo)
        return self

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
        date = self._date
        self._date = datetime(date.year, date.month, date.day, number, date.minute,
                              date.second, date.microsecond, date.tzinfo)
        return self

    def minutes(self, number):
        """Mutate the original moment by changing the minutes."""
        if number < 0:
            return self.subtract('minutes', abs(number))
        date = self._date
        self._date = datetime(date.year, date.month, date.day, date.hour, number,
                              date.second, date.microsecond, date.tzinfo)
        return self

    def seconds(self, number):
        """Mutate the original moment by changing the seconds."""
        if number < 0:
            return self.subtract('seconds', abs(number))
        date = self._date
        self._date = datetime(date.year, date.month, date.day, date.hour, date.minute,
                              number, date.microsecond, date.tzinfo)
        return self

    def microseconds(self, number):
        """Mutate the original moment by changing the seconds."""
        if number < 0:
            return self.subtract('microseconds', abs(number))
        date = self._date
        self._date = datetime(date.year, date.month, date.day, date.hour, date.minute,
                              date.second, number, date.tzinfo)
        return self

    def datetime(self):
        """Return the mutable date's inner datetime format."""
        return self._date

    def to_date(self):
        """Return the mutable date's inner datetime format."""
        return self._date
