"""
Simple API functionality.
"""

from .core import Moment


def date(*args):
    """Create a moment."""
    return Moment(*args)


def now():
    """Create a date from the present time."""
    return Moment.now()


def utc(*args):
    """Create a date using the UTC time zone."""
    return Moment.utc(*args)


def utcnow():
    """UTC equivalent to `now` function."""
    return Moment.utcnow()


def unix(timestamp, utc=False):
    """Create a date from a Unix timestamp."""
    return Moment.unix(timestamp, utc)
