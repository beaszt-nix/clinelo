#! /usr/bin/python3

import json
import sys
import requests
import os
from bs4 import BeautifulSoup as BS

global HOME
HOME = os.environ['HOME']
URL = sys.argv[2]
page = requests.get(URL)
soup = BS(page.content, 'html.parser')
mangaDB = os.path.join( HOME + '/clinelo/DB', sys.argv[1].replace(' ', '_') + ".json")

global db
global DIRNAME

if os.path.isfile(mangaDB):
    with open(mangaDB, 'r') as f:
        db = json.load(f)
        f.close()
else:
    db = {}

results = soup.find_all('a', attrs={'class': 'chapter-name text-nowrap'})

for r in reversed(results):
    if r['title'] not in db:
        db[r['title']] = r['href']

with open(mangaDB, 'w') as f:
    json.dump(db, f)
    f.close()

DIRNAME=sys.argv[1].replace(' ', '_')

for ch in db:
    if os.path.isdir(os.path.join(HOME + '/clinelo/library/' + DIRNAME, ch)) is False:
        os.chdir('{}/clinelo/library/'.format(HOME) + DIRNAME)
        os.system("python3 {}/clinelo/chapter_dl.py ".format(HOME) + db[ch] + " " + ch.replace(' ', '_'))
        os.chdir("{}/clinelo".format(HOME))
