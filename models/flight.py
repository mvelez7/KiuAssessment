from typing import List
from datetime import datetime
from models.package import Package


class Flight:

    def __init__(self, on: datetime):
        self.packages: List[Package] = []
        self._on: datetime = on
        self.id: int = -1

    @property
    def on(self) -> datetime:
        return self._on

    def transport_package(self, package: Package):
        self.packages.append(package)
        package.flight = self
