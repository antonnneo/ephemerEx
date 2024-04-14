import os

class HealthResponse(dict):
    """Отдает hostname текущего контейнера."""
    def __init__(
        self,
        instance_id: str = os.environ.get("HOSTNAME")
    ):
        """Инициализатор тела ответа.
        
        :param instance_id: id инстанса, представлен значением переменной окружения HOSTNAME контейнера.
        """
        result = {
            "instance_id": instance_id
        }
        return super().__init__(result)

    @property
    def instance_id(self):
        """Возвращает id инстанса."""
        return self["instance_id"]
