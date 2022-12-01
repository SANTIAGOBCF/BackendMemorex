#! /bin/bash

source _/bin/activate

APPS="core/ memorex/ politician/ post/ user/"

black --line-length=95 --skip-string-normalization $APPS
flake8 $APPS
isort $APPS
rm -f .coverage*;
