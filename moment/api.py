"""
Simple API functionality.
"""

from .core import Moment


def date(time, formula=None):
    """Create a moment."""
    return Moment(time, formula)


def now(self):
    """Create a date from the present time."""
    return Moment().now()


def utc(self, date=None, formula=None):
    """Create a date using the UTC time zone."""
    return Moment().utc(date, formula)


def unix(self, timestamp):
    """Create a date from a Unix timestamp."""
    return Moment().unix(timestamp)
