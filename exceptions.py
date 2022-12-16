class BaseException(Exception):
    message_defolt = ''
    code_defolt = 0

    def __init__(
            self,
            message: str = '',
            *args: object
    ) -> None:
        super().__init__(*args)
        self.message = message or self.message_defolt


    # def __str__(self) -> str:
    #     return self.message + f'{self.args}'
    def __str__(self):
        if self.args:
            return f'{self.message} {self.args}'
        return {'Error': self.message, 'Code': self.code_defolt}


class ResponseError(BaseException):
    """Не верный ответ на запрос к API."""
    message_defolt = 'Неверный ответp запроса'
    code_defolt = -2

    pass


class ResponseFalse(BaseException):
    """Ответ API не соответствует документации."""
    message_defolt = 'Неверный ответp запроса'
    code_defolt = -2
    pass


class UnknownStatusHomework(BaseException):
    """Неверный статус домашней работы."""
    message_defolt = 'Неверный статус работы'
    code_defolt = -4
    pass


class MessegeError(BaseException):
    """Ошибка отправки сообщения бота."""
    message_defolt = 'Ошибка при отправке сообщения'
    code_defolt = -3
    pass


class CriticalTokkenError(BaseException):
    """Ошибка отправки сообщения бота."""
    message_defolt = 'Неверно определенно имя токкена'
    code_defolt = -1
    pass
