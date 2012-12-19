import calendar
from datetime import datetime
from .date import MutableDate
from .parse import parse_js_date


class Moment(MutableDate):
    """A class to abstract date difficulties."""

    def __init__(self, date=None, formula=None):
        if date and formula:
            if '%' not in formula:
                formula = parse_js_date(formula)
            date = datetime.strptime(date, formula)
        elif isinstance(date, list) or isinstance(date, tuple):
            date = datetime(*date)
        self._date = date
        self._local = False
        self._formula = formula

    def now(self):
        self._date = datetime.now()
        return self

    def utc(self, date=None, formula=None):
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
        """Toggle a flag on the original moment to internally use UTC."""
        self._local = not self._local
        return self

    def format(self, formula):
        """Display the moment in a given format."""
        return "format"

    def strftime(self, formula):
        """Takes a Pythonic format, rather than the JS version."""
        return "format"

    def diff(self, moment, measurement=None):
        return self

    def __repr__(self):
        if self._formula is not None:
            formula = self._formula
        else:
            formula = "%m-%d-%Y, %l:%m %p"
        if self._date is not None:
            return "<Moment(%s)>" % (self._date.strftime(formula))
        return "<Moment>"
