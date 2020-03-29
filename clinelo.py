#! /usr/bin/python3

import json
import os
import argparse
import shutil

global HOME

HOME = os.environ['HOME']
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", action="store_true", help="To add Manga")
parser.add_argument("-n", "--name", type=str ,help="Name of the Manga")
parser.add_argument("-l", "--url", type=str, help="URL of the Manga")
parser.add_argument("-u", "--update", action="store_true", help="To check updates and download latest chapter")
parser.add_argument("-d", "--delete", action="store_true", help="To delete manga")
parser.add_argument("-L", "--list", action="store_true", help="To list out all mangas stored locally")
args = parser.parse_args()

listDB = '{}/clinelo/DB/manga_list.json'.format(HOME)

if os.path.isfile(listDB):
    with open(listDB, 'r') as f:
        db = json.load(f)
        f.close()
else:
    db = {}

if args.add is True:
    if args.name not in db:
        db[args.name] = args.url
        with open(listDB, 'w') as f:
            json.dump(db,f)
            f.close()
        DIRNAME=args.name.replace(' ', '_')
        os.mkdir(os.path.join('{}/clinelo/library'.format(HOME), DIRNAME))
        os.system('./chapter_list_update.py "' + args.name + '" ' + args.url)

if args.update is True:
   os.system('./chapter_list_update.py "' + args.name + '" ' + db[args.name])     

if args.delete is True:
    shutil.rmtree(os.path.join('{}/clinelo/library'.format(HOME), args.name.replace(' ', '_')))
    os.remove(os.path.join('{}/clinelo/DB'.format(HOME), args.name.replace(' ', '_') + '.json'))
    del db[args.name]

if args.list is True:
    for manga in db:
        print(manga)

with open(listDB, 'w') as f:
    json.dump(db,f)
    f.close()
