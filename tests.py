#!/usr/bin/env python

from unittest import TestCase, main
from datetime import datetime
import moment


class DateFunction(TestCase):

    def test_date_function_takes_a_string(self):
        d = moment.date("December 18, 2012", "MMMM D, YYYY")
        self.assertEquals(d.to_date(), datetime(2012, 12, 18))


if __name__ == '__main__':
    main()
