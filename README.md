# Проект Homework Bot
## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=gray)](https://www.python.org/) [![python telegram bot](https://img.shields.io/badge/Python%20telegram%20bot-464646?style=flat&logo=telegram&logoColor=56C0C0&color=gray)](https://github.com/python-telegram-bot/python-telegram-bot) [![requests/](https://img.shields.io/badge/-Requests-464646?style=flat&logo=pypi&logoColor=56C0C0&color=gray)](https://pypi.org/project/requests/)
## Линтеры
[![Flake8](https://img.shields.io/badge/-Flake8-464646?style=flat&logo=flake8&logoColor=56C0C0&color=gray)](https://flake8.pycqa.org/)

Полный список модулей, используемых в проекте, доступен в [homework_bot/requirements.txt](https://github.com/NECROshizo/homework_bot/blob/master/requirements.txt)
## Описание проекта
Проект телеграмм-бота Homework Bot использует API Яндекс.Практикума для проверки статуса домашней работы. Запрос статуса происходит по средствам опроса [endpoint](https://practicum.yandex.ru/api/user_api/homework_statuses/) через заданное время.

## Установка и настройки
#### Создание виртуального окружения:

```
python -m venv venv
```

#### Запуск виртуального окружения:

```
source venv/Scripts/activate - команда для Windows
source venv/bin/activate - команда для Linux и macOS
```
#### Установка зависимостей:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
#### Настройка параметров допуска оуружения
```
touch .env
```
Шаблон файла **.env**
```
TELEGRAM_TOKEN = <Токен телеграмм бота>
YP_TOKEN = 'Токен Яндекс.Правктикума'
CHAT_ID = 'ID телеграмм чата'
```
Получения телеграмм токена [BotFather](https://t.me/botfather)
Получения индивидуально токена Яндекс.Практикум [здесь]( https://oauth.yandex.ru/authorize?response_type=token&client_id=1d0b9dd4d652455a9eb710d450ff456a)
#### Запуск
```
python homework.py
```
Локальные настройки работы телеграмм бота находятся в [homework_bot/setting.py](https://github.com/NECROshizo/homework_bot/blob/master/setting.py)
## Автор
[**Оганин Пётр**](https://github.com/NECROshizo) 
2023 г.
