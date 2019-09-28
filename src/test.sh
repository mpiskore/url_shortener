#!/usr/bin/env bash

pip install -r requirements_dev.txt
./manage.py test
