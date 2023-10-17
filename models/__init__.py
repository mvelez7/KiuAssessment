from typing import List
from datetime import datetime

from models.person import Person
from models.flight import Flight
from models.package import Package


class DummyDB:
    """
    Class to simulate a DB
    """

    def __init__(self):
        self.all_packages: List[Package] = []
        self.all_flights: List[Flight] = []

    def insert_flight(self, flight: Flight):
        self.all_flights.append(flight)
        flight.id = len(self.all_flights)

    def insert_package(self, package: Package):
        self.all_packages.append(package)
        package.id = len(self.all_packages)

    def find_all_transported_packages_on(self, on: datetime) -> List[Package]:
        return [package for package in self.all_packages if package.flight.on == on]

db = DummyDB()
