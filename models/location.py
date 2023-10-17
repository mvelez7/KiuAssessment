

class Location:

    def __init__(self, name: str):
        self.name: str = name

    def __repr__(self) -> str:
        return f"Location#{self.name}"

    def __str__(self) -> str:
        return self.__repr__()
