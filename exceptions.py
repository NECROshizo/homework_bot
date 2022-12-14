class EnvironmentVariablesMissing(Exception):
    """Нет необходимых переменных окружения."""

    # message = ''

    # def __init__(self, *args: object, msg: str = '') -> None:
    #     self.message = msg or self.message
    #     super().__init__(*args)

    # def __str__(self) -> str:
    #     return self.message + f'{self.args}'
    pass


class ResponseError(Exception):
    """Не верный ответ."""

    pass


class ResponseFalse(Exception):
    """Ответ API не соответствует документации."""

    pass


class UnknownStatusHomework(Exception):
    """Неверный статус работы."""

    pass


class MessegeError(Exception):
    """Ошибка отправки сообщения бота."""

    pass


class CriticalTokkenError(Exception):
    """Ошибка отправки сообщения бота."""

    pass
