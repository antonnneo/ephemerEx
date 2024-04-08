import os

class ReadResponse(dict):
    """"""
    def __init__(
        self,
        message_text: str = None,
        error: str = None,
        instance_id: str = os.environ.get("HOSTNAME")
    ):
        result = {
            "message_text": message_text,
            "error": error,
            "instance_id": instance_id
        }
        return super().__init__(result)

    @property
    def message_text(self):
        return self["message_text"]

    @message_text.setter
    def message_text(self, message_text):
        self["message_text"] = message_text

    @property
    def error(self):
        return self["error"]
    
    @error.setter
    def error(self, error):
        self["error"] = error

    @property
    def instance_id(self):
        return self["instance_id"]
