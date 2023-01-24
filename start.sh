#!/bin/bash

python3 -m venv env
source env/bin/activate
pip install -U pip
pip install django
django-admin startproject note

sleep 3

cd note
git clone git@github.com:a3amat/notes.git
mv notes/* ./
rm -rf notes

echo 'Можете проверить запущенный Django'

./manage.py runserver


echo 'Exit'
