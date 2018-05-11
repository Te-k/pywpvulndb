import requests
import re


class WpVulnDbError(Exception):
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, message)


class WpVulnDbNotFound(WpVulnDbError):
    def __init__(self):
        self.message = "Resource not found in Wordpress Vulnerability Database"
        WpVulnDbError.__init__(self, self.message)


class WpVulnDb(object):
    def __init__(self, key):
        self.key = key
        self.base_url = "https://wpvulndb.com/api/v3/"
        self.user_agent = "PyWPVulnDb"

    def _request(self, path):
        headers = {
            'user-agent': self.user_agent,
            'Authorization': 'Token token=' + self.key
        }
        res = requests.get(self.base_url + path, headers=headers)
        if res.status_code == 404:
            raise WpVulnDbNotFound()
        if res.status_code != 200:
            raise WpVulnDbError("Bad HTTP Status Code %i" % res.status_code)
        return res.json()

    def wordpress(self, version):
        return self._request('wordpresses/' + version.replace(".", ""))

    def theme(self, name):
        return self._request('themes/' + name)

    def plugin(self, name):
        return self._request('plugins/' + name)


class PluginVersion(object):
    def __init__(self, version):
        self.version = version
        self.values = [int(a) for a in re.sub("[^0-9\.]", "", version).split(".")]

    def __str__(self):
        return self.version

    def __gt__(self, other):
        start = 0
        while True:
            if self.values[start] == other.values[start]:
                if len(self.values) == start + 1:
                    if len(other.values) == start + 1:
                        # equal
                        return False
                    else:
                        # if equality (1.2 == 1.2.0), still false
                        return False
                elif len(other.values) == start + 1:
                    return True
                else:
                    # Check next value
                    start += 1
            else:
                return (self.values[start] > other.values[start])

    def __eq__(self, v1):
        # FIXME: does not consider "1.2" == "1.2.0"
        return (self.values == v1.values)
