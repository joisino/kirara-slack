#!/usr/bin/env python3

import yaml
import os
import sys
import datetime

import slackweb

import config

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    slack = slackweb.Slack(url=config.slack_url)

    filename = './holiday_jp/holidays.yml'
    if not os.path.exists(filename):
        print('holidays.yml not found. Please try "git submodule update -i"', file=sys.stderr)
        sys.exit(1)

    with open(filename) as f:
        holidays = yaml.load(f.read())

    cur = datetime.date.today()

    # Holidays are not release days.
    if cur in holidays:
        sys.exit(0)

    # append succeeding holidays
    delta = datetime.timedelta(days=1)
    li = []
    while True:
        li.append(cur.day)
        cur += delta
        if cur not in holidays:
            break

    for magazine in config.magazines:
        if magazine[1] in li:
            text = "今日は%sの発売日です。" % magazine[0]
            print(text)
            slack.notify(text=text)
        
if __name__ == '__main__':
    main()
