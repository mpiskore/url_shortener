#!/usr/bin/env bash

pip install -r requirements_dev.txt
cd src || exit
./manage.py test
