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
        date = date.replace('mm', '%M')
    elif 'm' in date:
        date = date.replace('m', '%M')
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
    return date
