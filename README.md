# notes

Приложение для ведения заметок и напоминаний.

Первоначальную настроку можно провести с помощью баш скрипта:
```
bash start.sh
```

Либо тоже самое можно сделать ручками, перейдите нужную директорию и выполните следующие команды:
```
python3 -m venv env
source env/bin/activate
pip install -U pip
pip install django
django-admin startproject note
cd note
git clone https://github.com/a3amat/notes.git 
mv notes/* ./
rm -rf notes
./manage.py runserver
```
Дале нужно будет подключить наши приложения к проекту для этого нам понадобятся файлы в директории note/urls.py и note/settings.py

В файле urls.py в urlpatterns необходимо добавить строчки:
```
path('', include('home.urls'), name='home'),
path('article/', include('article.urls'), name='article'),
```
А так же нужно будет импортировать include
```
from django.urls import path, include
```

Далее манипуляции в файле settings.py
В разделе INSTALLED_APPS добавляем наши приложения
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'home',
    'article',
```
В разделе TEMPLATES приводим к следующиму виду, пункте DIRS укажим путь к нашим шаблонам:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
Следующим шагом можем запустить Django сервер и проверить, как работает наш проект
```
./manage.py runserver
```
