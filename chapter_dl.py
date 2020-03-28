#! /usr/bin/python3

import os
import shutil
import sys
import requests
from bs4 import BeautifulSoup as BS
from PIL import Image

URL = sys.argv[1]
DIR = os.path.join(os.getcwd(), sys.argv[2])
os.mkdir(DIR, 0o755)
page = requests.get(URL)
soup = BS(page.content, 'html.parser')

img_list = soup.find_all('img')
path_list = []

#Image download
for img in img_list[1:]:
    try:
        filename = img['alt'] + "." + img['src'].rsplit('.', 1)[-1]
    except:
        filename = img['src'].rsplit('/', 1)[-1]
    filename=filename.replace(' ', '_')
    path = os.path.join(DIR, filename)
    if os.path.exists(path) is not True:
        try:
            binary = requests.get(img['src'])
            open(path,'wb').write(binary.content)
            path_list.append(path)
        except:
            print(filename + ' not downloaded, trying next')
