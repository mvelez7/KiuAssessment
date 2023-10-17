

class Person:
    def __init__(self, name: str, is_client: bool):
        self.name: str = name
        self.is_client: bool = is_client

    def __repr__(self) -> str:
        return f"{self.name}"

    def __str__(self) -> str:
        return self.__repr__()
