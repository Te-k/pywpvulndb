# pywpvulndb

Python 2 and 3 wrapper around https://wpvulndb.com/ API

## Installation

```
git clone https://github.com/Te-k/pywpvulndb.git
cd pywpvulndb
pip install .
```

## Library

Three functions in the API:
```py
pvulnz = wp.plugin("eshop")
tvulnz = wp.theme("pagelines")
wpvulnz = wp.wordpress("4.7.1")
```

Example of code:
```py
from pywpvulndb import WpVulnDb, WpVulnDbError, WpVulnDbNotFound

wp = WpVulnDb(KEY)

try:
    vulnz = wp.plugin("eshop")
except WpVulnDbNotFound:
    print("Plugin not found")
except WpVulnDbError:
    print("Bad API key")

for v in vulnz['eshop']['vulnerabilities']:
    print(v)
```

For more information, see :
* [Wordpress Vuln API specifications](https://wpvulndb.com/api)
* [The code of the Command-Line Interface](https://github.com/Te-k/pywpvulndb/blob/master/pywpvulndb/cli.py)

## Command-Line Interface

You have two ways to store the key:
* Give the key as a `-k` parameter with every command
* Store the key in `~/.wpvulndb` under the format:
```
[WpVulnDb]
key: KEYHERE
```

Help:
```
usage: wpvulndb [-h] [--key KEY] [--plugin PLUGIN] [--theme THEME]
                [--wordpress WORDPRESS] [--version VERSION]

Request WP Vuln DB

optional arguments:
  -h, --help            show this help message and exit
  --key KEY, -k KEY     API key
  --plugin PLUGIN, -p PLUGIN
                        Plugin name
  --theme THEME, -t THEME
                        Theme name
  --wordpress WORDPRESS, -w WORDPRESS
                        Wordpress Version
  --version VERSION, -v VERSION
                        Plugin name
```

Examples :
```
$ wpvulndb -k APIKEY -p eshop
Last-Updated: 2015-10-13T11:07:00 in 6.3.14
5 vulnerabilities:
-None - eShop - wp-admin/admin.php Multiple Parameter XSS - XSS - Fixed in 6.2.9 - https://wpvulndb.com/vulnerabilities/7004
-2015-05-06T00:00:00.000Z - eShop <= 6.3.11 - Remote Code Execution - RCE - Fixed in 6.3.12 - https://wpvulndb.com/vulnerabilities/7967
[SNIP]

$ wpvulndb -k APIKEY -p eshop -v 6.3.11
Last-Updated: 2015-10-13T11:07:00 in 6.3.14
[VULNERABLE] -2015-05-06T00:00:00.000Z - eShop <= 6.3.11 - Remote Code Execution - RCE - Fixed in 6.3.12 - https://wpvulndb.com/vulnerabilities/7967
[SNIP]

$ wpvulndb -k APIKEY -w 4.7.1
Wordpress 4.7.1 released on 2017-01-11
* 2017-01-26T00:00:00 - WordPress 4.2.0-4.7.1 - Press This UI Available to Unauthorised Users - BYPASS - https://wpvulndb.com/vulnerabilities/8729
* 2017-01-26T00:00:00 - WordPress 3.5-4.7.1 - WP_Query SQL Injection - SQLI - https://wpvulndb.com/vulnerabilities/8730
[SNIP]

$ wpvulndb -t pagelines
Last-Updated: 2015-01-19T00:00:00 in 1.4.6
1 vulnerabilities:
-None - Pagelines Theme <= 1.4.5 - Privilege escalation - BYPASS - Fixed in 1.4.6 - https://wpvulndb.com/vulnerabilities/7763

$ wpvulndb -t pagelines -v 1.4.7
Last-Updated: 2015-01-19T00:00:00 in 1.4.6
No vulnerability found for this version
```

## LICENSE

This code is licensed under the MIT License, which basically says that you can do whatever you want with this code, but don't blame me if it fails. See details [here](https://github.com/Te-k/pywpvulndb/blob/master/LICENSE)

The wpvulndb.com API is free for non-commercial use, but requires payment and permission for any potential commercial use. Read [here](https://wpvulndb.com/api) for more information.
