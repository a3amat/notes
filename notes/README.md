# Мой проект

Данный проект развивается для изучения Django и так же для создания прототипов приложений для Django, которые можно будет использовать в будущих проектах.
Приложения:
- Home - главная страница
- Article - приложение для создания статьи и сообщений
- Gallery - картинная галерея
- TelegramBot - интеграция с телеграм каналом
- и много еще чего...

### Автоматическая установка
Первоначальную настроку можно провести с помощью баш скрипта:
```
bash start.sh <name>
```
name - необходимо задать имя проекту

По завершение работы скрипта, вы получаете рабочую Django, в котором настройки будут храниться в директории config.

### Ручная установка
Либо тоже самое можно сделать ручками, перейдите нужную директорию и выполните следующие команды:
```
python3 -m venv env
source env/bin/activate
pip install -U pip
pip install django
django-admin startproject <name>
cd <name>
git clone https://github.com/a3amat/notes.git
cp -r notes/. ./
rm -rf notes

./manage.py runserver
```

### После установовчная настройка
Дале нужно будет подключить наши приложения к проекту для этого нам понадобятся файлы в директории config/urls.py и config/settings.py

В файле urls.py в urlpatterns необходимо добавить строчки:
```
path('', include('home.urls'), name='home'),
path('article/', include('article.urls'), name='article'),
```
А так же нужно будет импортировать include
```
from django.urls import path, include
```
Файл должен выгледить следующим образом:
```
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('article/', include('article.urls'), name='article'),
]
```
Далее манипуляции в файле settings.py
В разделе INSTALLED_APPS добавляем наши приложения home, article как указано ниже
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
В разделе TEMPLATES приводим к следующиму виду, пункте DIRS укажим путь к нашим шаблонам BASE_DIR / 'templates'. Общий вид:
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
### Запуск проекта
Следующим шагом можем запустить Django сервер и проверить, как работает наш проект, но перед этим нужно будет выполнить следующие команды:
```
#провести миграцию
./manage.py makemigrations
./manage.py migrate
#создадим суперпользователя
./manage.py createsuperuser
./manage.py migrate
#запускаем проект
./manage.py runserver
```
По всем вопросам пишите:
<br>e-mail: a3amat9@yandex.ru
