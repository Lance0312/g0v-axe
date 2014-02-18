#!/usr/bin/env python3

from urllib import request
from urllib.error import URLError
from html.parser import HTMLParser

import json


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__(self)
        self.previous_tag = ""
        self.current_tag = ""
        self.name = ""
        self.scores = list()
        self.scorelist = list()

    def handle_starttag(self, tag, attrs):
        #print("Start: ", tag)
        self.previous_tag = self.current_tag
        self.current_tag = tag

    def handle_endtag(self, tag):
        #print("End  : ", tag)
        if tag == 'tr':
            if self.name != '姓名':
                self.scorelist.append({
                    "name": self.name,
                    "grades": {
                        "國語": int(self.scores[0]),
                        "數學": int(self.scores[1]),
                        "自然": int(self.scores[2]),
                        "社會": int(self.scores[3]),
                        "健康教育": int(self.scores[4]),
                    }
                })
            self.scores = list()

        if tag == 'table':
            print(json.dumps(self.scorelist))

    def handle_data(self, data):
        if self.previous_tag == 'tr' and self.current_tag == 'td':
            if data.strip():
                self.name = data.strip()

        if self.previous_tag == 'td' and self.current_tag == 'td':
            if data.strip():
                self.scores.append(data.strip())


def main():
    try:
        r = request.urlopen('http://axe-level-1.herokuapp.com/')

        html_content = r.read().decode('UTF-8')
        parser = MyHTMLParser()
        parser.feed(html_content)
        parser.close()
    except URLError as e:
        print(e)


if __name__ == '__main__':
    main()

# vim: sw=4 sts=4 et
