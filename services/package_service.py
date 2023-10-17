import logging

from models import db
from models.flight import Flight
from models.person import Person
from models.package import Package

logger = logging.getLogger()


def create_new_package(owner: Person) -> Package:
    package = Package(owner)

    db.insert_package(package)
    return package


def transport_package(flight: Flight, package: Package):
    if not package.owner.is_client:
        raise Exception(f"Can't transport a non client {package}")
    flight.transport_package(package)
