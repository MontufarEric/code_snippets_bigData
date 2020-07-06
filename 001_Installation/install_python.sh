#!/usr/bin/env bash
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
cd /opt
wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz
tar –xf Python-3.7.5.tgz
cd python-3.7.5
sudo make altinstall
python3 ––version
