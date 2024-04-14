import os


class NewResponse(dict):
    """Описывает структуру ответа ручки создания сообщения."""
    def __init__(
        self,
        message_id: str = None,
        error: str = None,
        instance_id: str = os.environ.get("HOSTNAME")
    ):
        """Инициализатор тела ответа ручки создания сообщения.
        
        :param message_id: id секретного сообщения, сохраненного в базе.
        :param error: сообщение об ошибке, возникшей в ходе обработки запроса.
        :param instance_id: id инстанса, представлен значением переменной окружения HOSTNAME контейнера.
        """        
        result = {
            "message_id": message_id,
            "error": error,
            "instance_id": instance_id
        }
        return super().__init__(result)

    @property
    def message_id(self):
        """Возвращает uuid полученного сообщения, с которым оно сохранилось в базе."""
        return self["message_id"]

    @message_id.setter
    def message_id(self, message_id):
        """Устанавливает uuid полученного сообщения, с которым оно сохранилось в базе."""
        self["message_id"] = message_id

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
