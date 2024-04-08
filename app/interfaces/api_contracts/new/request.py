from copy import deepcopy


class NewRequest(dict):
    """"""
    def __init__(
        self,
        message_text: str
    ):
        result = {
            "message_text": message_text
        }
        return super().__init__(result)

    @classmethod
    def init_from_dict(cls, data: dict):
        obj = deepcopy(data)
        return cls(**obj)

    @property
    def message_text(self):
        return self["message_text"]