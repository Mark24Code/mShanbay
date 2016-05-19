#!/bin/bash

SCRIPTPATH=`dirname "${BASH_SOURCE[0]}"`
cd $SCRIPTPATH

python3 manage.py runserver 0.0.0.0:8000