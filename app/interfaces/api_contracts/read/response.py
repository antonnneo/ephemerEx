import os

class ReadResponse(dict):
    """Описывает структуру ответа ручки чтения секретного сообщения."""
    def __init__(
        self,
        message_text: str = None,
        error: str = None,
        instance_id: str = os.environ.get("HOSTNAME")
    ):
        """Инициализатор тела ответа ручки чтения сообщения.

        :param message_text: текст секретного сообщения сохраненного в базе.
        :param error: сообщение об ошибке, возникшей в ходе обработки запроса.
        :param instance_id: id инстанса, представлен значением переменной окружения HOSTNAME контейнера.
        """
        result = {
            "message_text": message_text,
            "error": error,
            "instance_id": instance_id
        }
        return super().__init__(result)

    @property
    def message_text(self):
        """Возвращает текст секретного сообщения."""
        return self["message_text"]

    @message_text.setter
    def message_text(self, message_text):
        """Устанавливает текст секретного сообщения."""
        self["message_text"] = message_text

    @property
    def error(self):
        """Возвращает текст ошибки."""
        return self["error"]
    
    @error.setter
    def error(self, error):
        """Устанавливает текст ошибки."""
        self["error"] = error

    @property
    def instance_id(self):
        """Возвращает id инстанса."""
        return self["instance_id"]
