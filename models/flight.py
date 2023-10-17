from datetime import datetime
from models.package import Package
from models.location import Location


class Flight:

    def __init__(self, on: datetime, origin: Location, destination: Location):
        self._on: datetime = on
        self.id: int = -1
        self.origin: Location = origin
        self.destination: Location = destination

    @property
    def on(self) -> datetime:
        return self._on

    def transport_package(self, package: Package):
        """
        Transport a package on this flight
        """
        package.flight = self

    def __repr__(self) -> str:
        return f"Flight#{self.id}@{self.origin} -> {self.destination}"

    def __str__(self) -> str:
        return self.__repr__()
