from calendar import timegm
from datetime import datetime

import pytz
import times
from .date import MutableDate
from .parse import parse_date_and_formula, parse_js_date


class Moment(MutableDate):
    """A class to abstract date difficulties."""

    def __init__(self, date=None, formula=None):
        date, formula = parse_date_and_formula(date, formula)
        self._date = date
        self._formula = formula

    def now(self, utc=False):
        if utc:
            self._date = pytz.timezone('UTC').localize(datetime.utcnow())
        else:
            self._date = datetime.now()
        return self

    def utc(self, date=None, formula=None):
        date, formula = parse_date_and_formula(date, formula)
        self._date = pytz.timezone('UTC').localize(date)
        self._formula = formula
        return self

    def unix(self, timestamp, utc=False):
        """Create a date from a Unix timestamp."""
        if utc:
            self._date = datetime.utcfromtimestamp(timestamp)
        else:
            self._date = datetime.fromtimestamp(timestamp)
        return self

    def add(self, key, amount):
        """Add time to the original moment."""
        return self

    def subtract(self, key, amount):
        """Subtract time from the original moment."""
        return self

    def local(self):
        """Turn your UTC datetime into a local time zone datetime."""
        self._date = datetime.fromtimestamp(timegm(self._date.timetuple()))
        return self

    def timezone(self, zone):
        """Explicitly set the time zone you want to work with."""
        try:
            self._date = pytz.timezone(zone).localize(self._date)
        except ValueError:
            self._date = self._date.replace(tzinfo=pytz.timezone(zone))
        return self

    def to_zone(self, zone):
        """Change the time zone and affect the current moment's time."""
        try:
            times.to_local(times.to_universal(self._date), zone)
        except:
            times.to_local(self._date, zone)
        return self

    def format(self, formula):
        """Display the moment in a given format."""
        formula = parse_js_date(formula)
        return self._date.strftime(formula)

    def strftime(self, formula):
        """Takes a Pythonic format, rather than the JS version."""
        return self._date.strftime(formula)

    def diff(self, moment, measurement=None):
        return self

    def __repr__(self):
        if self._date is not None:
            return "<Moment(%s)>" % (self._date.strftime(self._formula))
        return "<Moment>"
