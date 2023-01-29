#!/bin/bash

python3 -m venv env
source env/bin/activate
pip install -U pip
pip install django
django-admin startproject $1

name=$1

cd ${name}
git clone git@github.com:a3amat/notes.git
cp -r notes/. ./
rm -rf notes

mv ${name} config
sed -i "s/${name}/config/g" config/asgi.py
sed -i "s/${name}/config/g" config/wsgi.py
sed -i "s/${name}/config/g" config/settings.py
sed -i "s/${name}/config/g" config/settings.py
sed -i "s/${name}/config/g" manage.py


echo 'Можете проверить запущенный Django'

./manage.py runserver

echo 'Exit'
