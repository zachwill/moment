from calendar import timegm
from datetime import datetime, timedelta
from time import timezone

import pytz
import times

from .date import MutableDate
from .parse import parse_date_and_formula, parse_js_date


class Moment(MutableDate):
    """A class to abstract date difficulties."""

    def __init__(self, *args):
        if args:
            date, formula = parse_date_and_formula(*args)
        else:
            date, formula = (None, None)
        self._date = date
        self._formula = formula

    def now(self):
        """Create a moment with the current datetime."""
        self._date = datetime.now()
        self._formula = "%Y-%m-%d"
        return self

    def utc(self, *args):
        """Create a moment from a UTC date."""
        date, formula = parse_date_and_formula(*args)
        self._date = pytz.timezone('UTC').localize(date)
        self._formula = formula
        return self

    def utcnow(self):
        """UTC equivalent to now."""
        self._date = pytz.timezone('UTC').localize(datetime.utcnow())
        self._formula = "%Y-%m-%d"
        return self

    def unix(self, timestamp, utc=False):
        """Create a date from a Unix timestamp."""
        if utc:
            fromtimestamp = datetime.utcfromtimestamp
        else:
            fromtimestamp = datetime.fromtimestamp
        try:
            # Seconds since epoch
            self._date = fromtimestamp(timestamp)
        except ValueError:
            # Milliseconds since epoch
            self._date = fromtimestamp(timestamp / 1000)
        self._formula = "%Y-%m-%d"
        return self

    def locale(self, zone=None):
        """Explicitly set the time zone you want to work with."""
        if not zone:
            self._date = datetime.fromtimestamp(timegm(self._date.timetuple()))
        else:
            try:
                self._date = pytz.timezone(zone).normalize(self._date)
            except ValueError:
                self._date = self._date.replace(tzinfo=pytz.timezone(zone))
        return self

    def timezone(self, zone):
        """
        Change the time zone and affect the current moment's time. Note, a
        locality must already be set.
        """
        date = self._date
        try:
            date = times.to_local(times.to_universal(date), zone)
        except:
            date = times.to_local(date, zone)
        finally:
            self._date = date
        return self

    def format(self, formula):
        """Display the moment in a given format."""
        formula = parse_js_date(formula)
        return self._date.strftime(formula)

    def strftime(self, formula):
        """Takes a Pythonic format, rather than the JS version."""
        return self._date.strftime(formula)

    def diff(self, moment, measurement=None):
        """Return the difference between moments."""
        return self - moment

    def done(self):
        """Return the datetime representation."""
        return self._date

    def clone(self):
        """Return a clone of the current moment."""
        clone = Moment(self._date)
        clone._formula = self._formula
        return clone

    def copy(self):
        """Same as clone."""
        return self.clone()

    def __repr__(self):
        if self._date is not None:
            return "<Moment(%s)>" % (self._date.strftime(self._formula))
        return "<Moment>"

    def __str__(self):
        formatted = self._date.strftime('%Y-%m-%dT%H:%M:%S')
        tz = str.format('{0:+06.2f}', -float(timezone) / 3600)
        return formatted + tz
