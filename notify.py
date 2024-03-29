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

    def is_holiday(date):
        return date.weekday() == 6 or date in holidays

    cur = datetime.date.today()

    # Holidays are not release days.
    if is_holiday(cur):
        sys.exit(0)

    # append succeeding holidays
    delta = datetime.timedelta(days=1)
    li = []
    while True:
        li.append(cur.day)
        cur += delta
        if not is_holiday(cur):
            break

    for magazine in config.magazines:
        if magazine[1] in li:
            text = config.message % magazine[0]
            print(text)
            try:
                slack.notify(text=text)
            except ValueError:
                print('Slackweb raised ValueError. Please configure `config.py` correctly.')
        
if __name__ == '__main__':
    main()
