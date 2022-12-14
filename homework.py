import requests
import os
import sys
import time
from exceptions import MessegeError, CriticalTokkenError
from exceptions import UnknownStatusHomework, ResponseError
import logging
from http import HTTPStatus
from telegram import Bot
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
load_dotenv()

PRACTICUM_TOKEN = os.getenv('YP_TOKEN')
# PRACTICUM_TOKEN = None
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('CHAT_ID')
# TELEGRAM_CHAT_ID = None

# RETRY_PERIOD = 30
RETRY_PERIOD = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}


HOMEWORK_VERDICTS = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}


def check_tokens():
    """Проверка переменных окружения."""
    try:
        variables = {
            'Токен практикума': PRACTICUM_TOKEN,
            'Токен телеграмм бота': TELEGRAM_TOKEN,
            'ID чата сообщения': TELEGRAM_CHAT_ID,

        }
    except NameError as err:
        raise CriticalTokkenError(err)

    missing = list(filter(
        lambda x: not bool(variables.get(x)), variables.keys()
    ))
    if missing:
        raise CriticalTokkenError(
            f'Неверно определенно: {", ".join(missing)}'
        )


def send_message(bot, message):
    """Отправка сообщения в Telegram чат."""
    try:
        bot.send_message(TELEGRAM_CHAT_ID, message)
        logger.debug(f'Отправленно сообщение "{message}"')
    except Exception:
        logger.error(f'Ошибка при отправке сообщения "{message}"')
        raise MessegeError(f'Ошибка при отправке сообщения "{message}"')


def get_api_answer(timestamp=0):
    """Запрос к единственному эндпоинту API-сервиса."""
    PAYLOADS = {'from_date': timestamp}
    try:
        homework_statuses = requests.get(
            ENDPOINT,
            headers=HEADERS,
            params=PAYLOADS,
        )
    except Exception as err:
        raise ResponseError(f'Ошибка запроса {err}')
    if homework_statuses.status_code != HTTPStatus.OK:
        raise ResponseError('Неверный ответ запрооса')
    return homework_statuses.json()


def check_response(response):
    """Проверка ответа API на соответствие документации."""
    equivalent = ('homeworks', 'current_date')
    if not isinstance(response, dict):
        raise TypeError(
            f'Ответ не соответствует документации, {type(response)} не dict'
        )
    if not equivalent == tuple(response.keys()):
        raise KeyError('Ответ содержит не верные ключи')
    homeworks = response.get('homeworks')
    if not isinstance(homeworks, list):
        raise TypeError(
            f'Ответ не соответствует документации, {type(homeworks)} не list'
        )


def parse_status(homework):
    """Извлечение статуса из информации о конкретной домашней работе."""
    homework_name = homework.get('homework_name')
    status = homework.get('status')
    verdict = HOMEWORK_VERDICTS.get(status)
    if homework_name and status in list(HOMEWORK_VERDICTS.keys()):
        return f'Изменился статус проверки работы "{homework_name}". {verdict}'
    raise UnknownStatusHomework('Неверный статус работы')


def main():
    """Основная логика работы бота."""
    try:
        check_tokens()
    except Exception as error:
        logger.critical(f'Критическая ошибка:{error}')
        sys.exit('Конец программы')

    bot = Bot(token=TELEGRAM_TOKEN)
    timestamp = int(time.time())
    # timestamp = 0

    while True:
        try:
            response = get_api_answer(timestamp)
            check_response(response)
            homeworks = response.get('homeworks')
            if homeworks:
                for homework in response.get('homeworks'):
                    message = parse_status(homework)
                    send_message(bot, message)
                # message = parse_status(homeworks[0])
                # send_message(bot, message)
                timestamp = response.get('current_date')
                # timestamp = int(time.time())
        except Exception as error:
            message = f'Сбой в работе программы: {error}'
            logger.error(error)
            send_message(bot, message)

        time.sleep(RETRY_PERIOD)


if __name__ == '__main__':
    # logging.basicConfig(
    #     level=logging.CRITICAL,
    #     filename='my_logger.log',
    #     filemode='a',
    #     encoding="utf-8",
    #     format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
    # )
    logger.setLevel(logging.DEBUG)
    streamHandler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)
    handler = RotatingFileHandler(
        'my_logger.log',
        maxBytes=500000,
        backupCount=5,
        encoding="utf-8"
    )
    logger.addHandler(handler)
    handler.setFormatter(formatter)
    main()
