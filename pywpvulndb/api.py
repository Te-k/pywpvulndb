import requests


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
