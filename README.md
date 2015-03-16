Простая платформа для создания набора вопросов и проведения тестирования.

Поддерживаются:

* Общее ограничение по времени
    * НЕТ ограничения на отдельные вопросы
* Вопросы с несколькими правильными вариантами ответа
* Просмотр истории теста
* Оценки (по кол-ву правильных ответов)
* Аккаунты (для каждого тестируемого - отдельный аккаунт)
* Редактирование вопросов и ответов
* Создание наборов вопросов (тестов)


Installing
=========

* Install pip (http://pip.readthedocs.org/en/latest/installing.html)
* Install requirements
```
pip install -r requirements.txt
```
* $ cd sources
* Initialize database
```
$ ./manage.py syncdb
```
* Run
```
$ ./manage.py runserver
```
* Open browser and go to
```
http://localhost:8000
```
