from __future__ import annotations

from models.person import Person
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.flight import Flight


class Package:
    def __init__(self, owner: Person):
        self._owner: Person = owner
        self._flight: Optional[Flight] = None
        self.id: int = -1

    @property
    def owner(self) -> Person:
        return self._owner

    @property
    def flight(self) -> Flight:
        return self._flight

    @flight.setter
    def flight(self, flight: Flight):
        self._flight = flight
