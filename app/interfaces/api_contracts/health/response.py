import os

class HealthResponse(dict):
    def __init__(
        self,
        instance_id: str = os.environ.get("HOSTNAME")
    ):
        result = {
            "instance_id": instance_id
        }
        return super().__init__(result)

    @property
    def instance_id(self):
        return self["instance_id"]
