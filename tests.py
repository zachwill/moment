#!/usr/bin/env python

from unittest import TestCase, main
from datetime import datetime
import moment


class SimpleAPI(TestCase):

    def test_date_function_takes_a_string(self):
        d = moment.date("December 18, 2012", "MMMM D, YYYY")
        self.assertEquals(d.to_date(), datetime(2012, 12, 18))

    def test_date_function_with_datetime(self):
        d = moment.date(datetime(2012, 12, 18))
        self.assertEquals(d.datetime(), datetime(2012, 12, 18))

    def test_date_function_with_iterable(self):
        d = moment.date((2012, 12, 18))
        self.assertEquals(d.datetime(), datetime(2012, 12, 18))

    def test_now_function_with_current_date(self):
        d = moment.now().to_date()
        now = datetime.now()
        self.assertEquals(d.year, now.year)
        self.assertEquals(d.month, now.month)
        self.assertEquals(d.day, now.day)
        self.assertEquals(d.hour, now.hour)


if __name__ == '__main__':
    main()
