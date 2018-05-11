import argparse
import sys
import os
from .api import WpVulnDb, WpVulnDbError, WpVulnDbNotFound


def is_smaller_version(v1, v2):
    # FIXME: may not work all the time, 4.3.10 > 4.3.2
    return (int(v1.replace(".", "")) < int(v2.replace(".", "")))

def main():
    parser = argparse.ArgumentParser(description='Request WP Vuln DB')
    parser.add_argument('--key', '-k', help='API key')
    parser.add_argument('--plugin', '-p', help='Plugin name')
    parser.add_argument('--theme', '-t', help='Theme name')
    parser.add_argument('--wordpress', '-w', help='Wordpress Version')
    parser.add_argument('--version', '-v', help='Plugin name')
    args = parser.parse_args()

    if args.key is None:
        print("You need to provide an API key with --key/-k")
        sys.exit(1)

    wp = WpVulnDb(args.key)
    if args.plugin:
        try:
            res = wp.plugin(args.plugin)
        except WpVulnDbNotFound:
            print("Plugin not found")
        except WpVulnDbError:
            print("Error, bad API key ?")
        if args.version:
            data = res[args.plugin]
            print("Last-Updated: %s in %s" % (data['last_updated'][:19], data['latest_version']))
            if len(data['vulnerabilities']) == 0:
                print("No known vulnerabilities for this plugin")
            else:
                count = 0
                for vuln in data['vulnerabilities']:
                    if vuln['fixed_in'] is None:
                        count +=1
                        print("[MAYBE] -%s - %s - %s - No info on fixed version - https://wpvulndb.com/vulnerabilities/%i" % (
                            vuln['published_date'],
                            vuln['title'],
                            vuln['vuln_type'],
                            vuln['id']
                            )
                        )
                    else:
                        if is_smaller_version(args.version, vuln['fixed_in']):
                            count += 1
                            print("[VULNERABLE] -%s - %s - %s - Fixed in %s - https://wpvulndb.com/vulnerabilities/%i" % (
                                vuln['published_date'],
                                vuln['title'],
                                vuln['vuln_type'],
                                vuln['fixed_in'],
                                vuln['id']
                                )
                            )
                if count == 0:
                    print("No vulnerability found for this version")
        else:
            data = res[args.plugin]
            print("Last-Updated: %s in %s" % (data['last_updated'][:19], data['latest_version']))
            if len(data['vulnerabilities']) == 0:
                print("No vulnerabilities")
            else:
                print("%i vulnerabilities:" % len(data['vulnerabilities']))
                for vuln in data['vulnerabilities']:
                    print("-%s - %s - %s - Fixed in %s - https://wpvulndb.com/vulnerabilities/%i" % (
                        vuln['published_date'],
                        vuln['title'],
                        vuln['vuln_type'],
                        vuln['fixed_in'],
                        vuln['id']
                        )
                    )
    elif args.wordpress:
        data = wp.wordpress(args.wordpress)[args.wordpress]
        print("Wordpress %s released on %s" % (args.wordpress, data['release_date']))
        if len(data['vulnerabilities']) == 0:
            print("No vulnerabilities for this version")
        else:
            for vuln in data['vulnerabilities']:
                print("* %s - %s - %s - https://wpvulndb.com/vulnerabilities/%i" % (
                    vuln['published_date'][:19],
                    vuln['title'],
                    vuln['vuln_type'],
                    vuln['id']
                    )
                )
    if args.theme:
        try:
            res = wp.theme(args.theme)
        except WpVulnDbNotFound:
            print("Plugin not found")
        except WpVulnDbError:
            print("Error, bad API key ?")
        if args.version:
            data = res[args.theme]
            print("Last-Updated: %s in %s" % (data['last_updated'][:19], data['latest_version']))
            if len(data['vulnerabilities']) == 0:
                print("No known vulnerabilities for this plugin")
            else:
                count = 0
                for vuln in data['vulnerabilities']:
                    if vuln['fixed_in'] is None:
                        count +=1
                        print("[MAYBE] -%s - %s - %s - No info on fixed version - https://wpvulndb.com/vulnerabilities/%i" % (
                            vuln['published_date'],
                            vuln['title'],
                            vuln['vuln_type'],
                            vuln['id']
                            )
                        )
                    else:
                        if is_smaller_version(args.version, vuln['fixed_in']):
                            count += 1
                            print("[VULNERABLE] -%s - %s - %s - Fixed in %s - https://wpvulndb.com/vulnerabilities/%i" % (
                                vuln['published_date'],
                                vuln['title'],
                                vuln['vuln_type'],
                                vuln['fixed_in'],
                                vuln['id']
                                )
                            )
                if count == 0:
                    print("No vulnerability found for this version")
        else:
            data = res[args.theme]
            print("Last-Updated: %s in %s" % (data['last_updated'][:19], data['latest_version']))
            if len(data['vulnerabilities']) == 0:
                print("No vulnerabilities")
            else:
                print("%i vulnerabilities:" % len(data['vulnerabilities']))
                for vuln in data['vulnerabilities']:
                    print("-%s - %s - %s - Fixed in %s - https://wpvulndb.com/vulnerabilities/%i" % (
                        vuln['published_date'],
                        vuln['title'],
                        vuln['vuln_type'],
                        vuln['fixed_in'],
                        vuln['id']
                        )
                    )
    else:
        print("You need to provide something to query (plugin, theme, wordpress...)")
        parser.print_help()
