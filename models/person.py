

class Person:
    def __init__(self, name: str, is_client: bool):
        self._name: str = name
        self._is_client: bool = is_client

    @property
    def is_client(self) -> bool:
        return self._is_client
