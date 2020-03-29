#! /bin/bash

mkdir library
mkdir DB

chmod +x clinelo.py
chmod +x chapter_dl.py
chmod +x chapter_list_update.py
chmod +x remove.sh
pip3 install --user requests
pip3 install --user beautifulsoup4

ln -s $PWD/clinelo.py $HOME/.local/bin/clinelo
