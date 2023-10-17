import logging

from models import db
from models.flight import Flight
from models.person import Person
from models.package import Package

logger = logging.getLogger()


def create_new_package(owner: Person) -> Package:
    """
    Creates a new package
    It uses a dummy database (db) to insert the flight and gets an id for it.
    """
    package = Package(owner)

    db.insert_package(package)
    return package


def transport_package(flight: Flight, package: Package):
    """
    Transport a package on a specific flight. If package's owner is not a client,
    the pacakge can't be transported, an exception will be raised.
    """
    if not package.owner.is_client:
        raise Exception(f"Can't transport a non client {package}")
    flight.transport_package(package)
