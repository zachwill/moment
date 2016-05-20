from datetime import datetime


def parse_date_and_formula(*args):
    """Doesn't need to be part of core Moment class."""
    date, formula = _parse_arguments(*args)
    if date and formula:
        if '%' not in formula:
            formula = parse_js_date(formula)
        date = datetime.strptime(date, formula)
    elif isinstance(date, list) or isinstance(date, tuple):
        if len(date) == 1:
            # Python datetime needs the month and day, too.
            date = [date[0], 1, 1]
        date = datetime(*date)
    elif isinstance(date, str) or isinstance(date, unicode):
        if formula is None:
            formula = "%Y-%m-%d"
        date = datetime.strptime(date, formula)
    return date, formula


def _parse_arguments(*args):
    """Because I'm not particularly Pythonic."""
    formula = None
    if len(args) == 1:
        date = args[0]
    elif len(args) == 2:
        date = args[0]
        formula = args[1]
    else:
        date = args
    return date, formula


def parse_js_date(date):
    """
    Translate the easy-to-use JavaScript format strings to Python's cumbersome
    strftime format. Also, this is some ugly code -- and it's completely
    order-dependent.
    """
    # AM/PM
    if 'A' in date:
        date = date.replace('A', '%p')
    elif 'a' in date:
        date = date.replace('a', '%P')
    # 24 hours
    if 'HH' in date:
        date = date.replace('HH', '%H')
    elif 'H' in date:
        date = date.replace('H', '%k')
    # 12 hours
    elif 'hh' in date:
        date = date.replace('hh', '%I')
    elif 'h' in date:
        date = date.replace('h', '%l')
    # Minutes
    if 'mm' in date:
        date = date.replace('mm', '%min')
    elif 'm' in date:
        date = date.replace('m', '%min')
    # Seconds
    if 'ss' in date:
        date = date.replace('ss', '%S')
    elif 's' in date:
        date = date.replace('s', '%S')
    # Milliseconds
    if 'SSS' in date:
        date = date.replace('SSS', '%3')
    # Years
    if 'YYYY' in date:
        date = date.replace('YYYY', '%Y')
    elif 'YY' in date:
        date = date.replace('YY', '%y')
    # Months
    if 'MMMM' in date:
        date = date.replace('MMMM', '%B')
    elif 'MMM' in date:
        date = date.replace('MMM', '%b')
    elif 'MM' in date:
        date = date.replace('MM', '%m')
    elif 'M' in date:
        date = date.replace('M', '%m')
    # Days of the week
    if 'dddd' in date:
        date = date.replace('dddd', '%A')
    elif 'ddd' in date:
        date = date.replace('ddd', '%a')
    elif 'dd' in date:
        date = date.replace('dd', '%w')
    elif 'd' in date:
        date = date.replace('d', '%u')
    # Days of the year
    if 'DDDD' in date:
        date = date.replace('DDDD', '%j')
    elif 'DDD' in date:
        date = date.replace('DDD', '%j')
    # Days of the month
    elif 'DD' in date:
        date = date.replace('DD', '%d')
    elif 'D' in date:
        date = date.replace('D', '%d')
    # Moment.js shorthand
    elif 'L' in date:
        date = date.replace('L', '%Y-%m-%dT%H:%M:%SZ')
    # A necessary evil right now...
    if '%min' in date:
        date = date.replace('%min', '%M')
    return date
