from copy import deepcopy


class NewRequest(dict):
    """Описывает структуру запроса к ручке создание сообщения."""
    def __init__(
        self,
        message_text: str
    ):
        """Инициализатор тела запроса ручки создания сообщения.

        :param message_text: текст секретного сообщения для сохранения в базе.
        """
        result = {
            "message_text": message_text
        }
        return super().__init__(result)

    @classmethod
    def init_from_dict(cls, data: dict):
        """Инициализирует объект из пришедшего запроса."""
        obj = deepcopy(data)
        return cls(**obj)

    @property
    def message_text(self):
        """Возвращает текст сообщения."""
        return self["message_text"]