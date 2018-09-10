import requests
import dateparser

MAX_RETRIES = 5


def POST(api, **kwargs):
    for x in range(MAX_RETRIES):
        try:
            r = requests.post(api, **kwargs)
            if r.ok:
                return r
        except Exception as e:
            pass
    return None


class DucklingDateParser(object):
    def __init__(self, **kwargs):
        self.host = kwargs.get('host', '0.0.0.0')
        self.port = kwargs.get('port', '8000')

    def parse(self, date, **kwargs):
        data = {
            'locale': 'en_GB',
            'text': date
        }

        duck_api = "http://{}:{}/parse".format(self.host, self.port)
        r = POST(duck_api, data=data)
        if r is None:
            return None
        return self._format_date(r.json(), **kwargs)

    @staticmethod
    def _format_date(response, **kwargs):
        try:
            result = response[0]
            _date = result['value']['value']
            return dateparser.parse(_date, **kwargs)
        except (IndexError, KeyError):
            return None




