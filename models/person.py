

class Person:
    def __init__(self, name: str, is_client: bool):
        self._name: str = name
        self._is_client: bool = is_client

    @property
    def is_client(self) -> bool:
        return self._is_client

    def __repr__(self) -> str:
        return f"Person#{self.name}@{'Client' if self.is_client else 'NonClient'}"

    def __str__(self) -> str:
        return self.__repr__()
