from copy import deepcopy


class ReadRequest(dict):
    """"""
    def __init__(
        self,
        message_id: str
    ):
        result = {
            "message_id": message_id
        }
        return super().__init__(result)

    @classmethod
    def init_from_dict(cls, data: dict):
        obj = deepcopy(data)
        return cls(**obj)

    @property
    def message_id(self):
        return self["message_id"]

    @message_id.setter
    def message_id(self, message_id):
        self["message_id"] = message_id

