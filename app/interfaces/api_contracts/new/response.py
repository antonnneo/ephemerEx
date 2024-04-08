import os


class NewResponse(dict):
    """"""
    def __init__(
        self,
        message_id: str = None,
        error: str = None,
        instance_id: str = os.environ.get("HOSTNAME")
    ):
        result = {
            "message_id": message_id,
            "error": error,
            "instance_id": instance_id
        }
        return super().__init__(result)

    @property
    def message_id(self):
        return self["message_id"]

    @message_id.setter
    def message_id(self, message_id):
        self["message_id"] = message_id

    @property
    def error(self):
        return self["error"]
    
    @error.setter
    def error(self, error):
        self["error"] = error

    @property
    def instance_id(self):
        return self["instance_id"]
