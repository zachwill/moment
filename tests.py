#!/usr/bin/env python

from unittest import TestCase, main
from datetime import datetime
import pytz
import moment


class SimpleAPI(TestCase):

    def test_date_function_takes_a_string(self):
        d = moment.date("December 18, 2012", "MMMM D, YYYY")
        self.assertEqual(d, datetime(2012, 12, 18))

    def test_date_function_with_datetime(self):
        d = moment.date(datetime(2012, 12, 18))
        self.assertEqual(d, datetime(2012, 12, 18))

    def test_date_function_with_iterable(self):
        d = moment.date((2012, 12, 18))
        self.assertEqual(d, datetime(2012, 12, 18))

    def test_date_function_with_args(self):
        d = moment.date(2012, 12, 18)
        self.assertEqual(d, datetime(2012, 12, 18))

    def test_date_function_with_string(self):
        d = moment.date("2012-12-18")
        self.assertEqual(d, datetime(2012, 12, 18))

    def test_date_function_with_unicode(self):
        d = moment.date(u"2012-12-18")
        self.assertEqual(d, datetime(2012, 12, 18))

    def test_utc_function_with_args(self):
        d = moment.utc(2012, 12, 18)
        self.assertEqual(d, datetime(2012, 12, 18, tzinfo=pytz.utc))

    def test_now_function_with_current_date(self):
        d = moment.now().date
        now = datetime.now()
        self.assertEqual(d.year, now.year)
        self.assertEqual(d.month, now.month)
        self.assertEqual(d.day, now.day)
        self.assertEqual(d.hour, now.hour)
        self.assertEqual(d.second, now.second)

    def test_utcnow_function(self):
        d = moment.utcnow()
        now = datetime.utcnow()
        self.assertEqual(d.year, now.year)
        self.assertEqual(d.month, now.month)
        self.assertEqual(d.day, now.day)
        self.assertEqual(d.hour, now.hour)
        self.assertEqual(d.second, now.second)

    def test_moment_can_transfer_between_datetime_and_moment(self):
        d = moment.now().date
        self.assertEqual(d, moment.date(d).date)

    def test_moment_unix_command(self):
        d = moment.unix(1355788800, utc=True).date
        expected = moment.utc((2012, 12, 18)).date
        self.assertEqual(d, expected)

    def test_moment_can_subtract_another_moment(self):
        d = moment.date((2012, 12, 19))
        self.assertTrue(d - moment.date((2012, 12, 18)))

    def test_moment_can_subtract_a_datetime(self):
        d = moment.date((2012, 12, 19))
        self.assertTrue(d - datetime(2012, 12, 18))

    def test_a_datetime_can_subtract_a_moment(self):
        d = moment.date((2012, 12, 18))
        self.assertTrue(datetime(2012, 12, 19) - d)

    def test_date_property(self):
        d = moment.date(2012, 12, 18).date
        self.assertEqual(d, datetime(2012, 12, 18))

    def test_zero_property(self):
        d = moment.date(2012, 12, 18, 1, 2, 3)
        self.assertEqual(d.zero.date, datetime(2012, 12, 18))

    def test_cloning_a_UTC_date(self):
        utc = moment.utc("2016-01-13T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
        self.assertEqual(utc.hours, 0)
        self.assertEqual(utc.format("YYYY-MM-DD"), "2016-01-13")
        usa = utc.clone().locale("US/Eastern")
        self.assertEqual(usa.hours, 19)
        self.assertEqual(usa.format("YYYY-MM-DD"), "2016-01-12")

    def test_copy_method_is_same_as_clone(self):
        d = moment.date(2016, 5, 21)
        copy = d.copy().subtract(weeks=1)
        self.assertEqual(d, datetime(2016, 5, 21))
        self.assertEqual(copy, datetime(2016, 5, 14))


class AdvancedDateParsing(TestCase):

    def test_today(self):
        d = moment.date("today").zero
        now = moment.now().zero
        self.assertEqual(d.date, now.date)

    def test_yesterday(self):
        d = moment.date("yesterday").zero
        expecting = moment.now().zero.subtract(days=1)
        self.assertEqual(d.date, expecting.date)

    def test_future(self):
        d = moment.date("tomorrow").zero
        expecting = moment.now().zero.add(days=1)
        self.assertEqual(d.date, expecting.date)

    def test_2_weeks_ago(self):
        d = moment.date("2 weeks ago").zero
        expecting = moment.now().zero.subtract(weeks=2)
        self.assertEqual(d.date, expecting.date)

    def test_2_weeks_from_now(self):
        d = moment.date("2 weeks from now").zero
        expecting = moment.now().zero.add(weeks=2)
        self.assertEqual(d, expecting)

    def test_date_with_month_as_word(self):
        d = moment.date("December 12, 2012").zero
        expecting = moment.date((2012, 12, 12))
        self.assertEqual(d, expecting)

    def test_date_with_month_abbreviation(self):
        d = moment.date("Dec 12, 2012").zero
        expecting = moment.date((2012, 12, 12))
        self.assertEqual(d, expecting)

    def test_date_without_days_defaults_to_first_day(self):
        d = moment.date("Dec 2012").zero
        expecting = moment.date((2012, 12, 1))
        self.assertEqual(d.date, expecting.date)


class Replacement(TestCase):

    def test_simple_chaining_commands(self):
        d = moment.date([2012, 12, 18])
        expecting = moment.date((2012, 12, 18, 1, 2, 3))
        d.replace(hours=1, minutes=2, seconds=3)
        self.assertEqual(d, expecting)

    def test_chaining_with_format(self):
        d = moment.utc((2012, 12, 18))
        d.replace(hours=1).add(minutes=2).replace(seconds=3)
        expecting = "2012-12-18 01:02:03"
        self.assertEqual(d.format('YYYY-MM-DD hh:mm:ss'), expecting)

    def test_properties_after_chaining(self):
        d = moment.now().replace(years=1984, months=1, days=1)
        self.assertEqual(d.year, 1984)

    def test_add_with_keywords(self):
        d = moment.date((2012, 12, 19))
        d.add(hours=1, minutes=2, seconds=3)
        expecting = moment.date((2012, 12, 19, 1, 2, 3))
        self.assertEqual(d, expecting)

    def test_subtract_with_keywords(self):
        d = moment.date((2012, 12, 19, 1, 2, 3))
        d.subtract(hours=1, minutes=2, seconds=3)
        expecting = moment.date((2012, 12, 19))
        self.assertEqual(d, expecting)

    def test_chaining_with_replace_method(self):
        d = moment.date((2012, 12, 19))
        d.replace(hours=1, minutes=2, seconds=3)
        expecting = moment.date((2012, 12, 19, 1, 2, 3))
        self.assertEqual(d, expecting)


class Weekdays(TestCase):

    def test_weekdays_can_be_manipulated(self):
        d = moment.date([2012, 12, 19])
        yesterday = moment.date([2012, 12, 18])
        self.assertEqual(d.date.isoweekday(), 3)
        self.assertEqual(d.replace(weekday=3), d)
        self.assertEqual(d.replace(weekday=2).done(), yesterday.done())

    def test_week_addition_equals_weekday_manipulation(self):
        d = moment.date([2012, 12, 19])
        upcoming = d.clone().add('weeks', 1)
        expecting = moment.date([2012, 12, 26]).date
        self.assertEqual(upcoming, expecting)
        self.assertEqual(d.replace(weekday=10), upcoming)

    def test_weekdays_with_zeros(self):
        d = moment.date([2012, 12, 19])
        sunday = moment.date([2012, 12, 16])
        self.assertEqual(d.replace(weekday=0), sunday)

    def test_weekdays_with_negative_numbers(self):
        d = moment.date((2012, 12, 19))
        expecting = moment.date([2012, 12, 9]).date
        self.assertEqual(d.replace(weekday=-7), expecting)

    def test_weekdays_with_larger_number_into_new_year(self):
        d = moment.date((2012, 12, 19))
        expecting = moment.date("2013-01-09").date
        self.assertEqual(d.replace(weekday=24).date, expecting)


class SubtractMonth(TestCase):

    def test_subtract_twelve_month_from_last_month(self):
        d = moment.date((2012, 12, 1))
        expecting = moment.date((2011, 12, 1)).date
        self.assertEqual(d.subtract(months=12).date, expecting)

    def test_subtract_one_month_from_first_month(self):
        d = moment.date((2012, 1, 1))
        expecting = moment.date((2011, 12, 1)).date
        self.assertEqual(d.subtract(months=1).date, expecting)

    def test_subtract_less_then_cur_month(self):
        d = moment.date((2012, 3, 1))
        expecting = moment.date((2011, 9, 1)).date
        self.assertEqual(d.subtract(months=6).date, expecting)

    def test_subtract_zero_months(self):
        d = moment.date((2012, 3, 1))
        expecting = moment.date((2012, 3, 1)).date
        self.assertEqual(d.subtract(months=0).date, expecting)

if __name__ == '__main__':
    main()
