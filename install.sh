#!/bin/bash
sudo apt install qbittorrent
virtualenv env
source env/bin/activate
pip install -r requirements.txt
deactivate