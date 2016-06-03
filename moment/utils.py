"""
Added for Python 3 compatibility.
"""

import sys


STRING_TYPES = (basestring, ) if sys.version_info < (3, 0) else (str, )


def _iteritems(data):
    "For Python 3 support."
    if sys.version_info < (3, 0):
        return data.iteritems()
    else:
        return data.items()
