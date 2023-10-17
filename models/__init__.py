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
        """
        Method to simulate a database flight table record creation from a flight model + commit
        """
        self.all_flights.append(flight)
        flight.id = len(self.all_flights)

    def insert_package(self, package: Package):
        """
        Method to simulate a database package table record creation from a package model + commit
        """
        self.all_packages.append(package)
        package.id = len(self.all_packages)

    def find_all_transported_packages_on(self, on: datetime) -> List[Package]:
        """
        Method to find all the packages transported on an specific date
        """
        return [package for package in self.all_packages if package.flight.on == on]

db = DummyDB()
