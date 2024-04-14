from copy import deepcopy


class ReadRequest(dict):
    """Описывает структуру запроса к ручке чтения сообщения."""
    def __init__(
        self,
        message_id: str
    ):
        """Инициализатор тела запроса ручки чтения сообщения.

        :param message_id: uuid для нахождения секретного сообщения в базе.
        """
        result = {
            "message_id": message_id
        }
        return super().__init__(result)

    @classmethod
    def init_from_dict(cls, data: dict):
        """Инициализирует объект из пришедшего запроса."""
        obj = deepcopy(data)
        return cls(**obj)

    @property
    def message_id(self):
        """Возвращает id сообщения."""
        return self["message_id"]

    @message_id.setter
    def message_id(self, message_id):
        """Устанавливает id сообщения."""
        self["message_id"] = message_id

