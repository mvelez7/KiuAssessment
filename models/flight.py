from typing import List
from datetime import datetime
from models.package import Package


class Flight:

    def __init__(self, on: datetime):
        self._on: datetime = on
        self.id: int = -1

    @property
    def on(self) -> datetime:
        return self._on

    def transport_package(self, package: Package):
        package.flight = self
