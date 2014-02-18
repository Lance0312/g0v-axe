#!/usr/bin/env python3

from urllib import request
from urllib.error import URLError
from bs4 import BeautifulSoup

import json


def main():
    try:
        r = request.urlopen('http://axe-level-1.herokuapp.com/')

        html_content = r.read().decode('UTF-8')
        soup = BeautifulSoup(html_content)
        rows = soup.find_all('tr')
        rows.remove(rows[0])
        scorelist = list()
        for row in rows:
            columns = row.find_all('td')
            scorelist.append({
                'name': columns[0].string,
                'grades': {
                    '國語': int(columns[1].string),
                    '數學': int(columns[2].string),
                    '自然': int(columns[3].string),
                    '社會': int(columns[4].string),
                    '健康教育': int(columns[5].string)
                }
            })
        print(json.dumps(scorelist))
    except URLError as e:
        print(e)


if __name__ == '__main__':
    main()

# vim: sw=4 sts=4 et
