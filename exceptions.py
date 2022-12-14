class ResponseError(Exception):
    """Не верный ответ на запрос к API."""

    pass


class ResponseFalse(Exception):
    """Ответ API не соответствует документации."""

    pass


class UnknownStatusHomework(Exception):
    """Неверный статус домашней работы."""

    pass


class MessegeError(Exception):
    """Ошибка отправки сообщения бота."""

    pass


class CriticalTokkenError(Exception):
    """Ошибка отправки сообщения бота."""

    pass
