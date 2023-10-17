from datetime import datetime

import pytest

from models.flight import Flight
from models.person import Person
from models.package import Package
from services import package_service


def test_transport_client_new_package(mocker):
    flight = Flight(datetime.now(), origin=mocker.MagicMock(), destination=mocker.MagicMock())
    package_owner = Person('Matias', is_client=True)
    matias_package: Package = Package(package_owner)
    package_service.transport_package(flight, matias_package)

    assert matias_package.flight is flight


def test_transport_non_client_package(mocker):
    flight = Flight(datetime.now(), origin=mocker.MagicMock(), destination=mocker.MagicMock())
    package_owner = Person('Nicolas', is_client=False)
    non_client_package: Package = Package(package_owner)

    with pytest.raises(Exception):
        package_service.transport_package(flight, non_client_package)


def test_transport_multiple_client_packages(mocker):
    flight = Flight(datetime.now(), origin=mocker.MagicMock(), destination=mocker.MagicMock())
    package_owner1 = Person('Matias', is_client=True)
    package_owner2 = Person('Nicolas', is_client=True)
    package_owner3 = Person('Velez', is_client=True)

    package1 = Package(package_owner1)
    package2 = Package(package_owner2)
    package3 = Package(package_owner3)
    package_service.transport_package(flight, package1)
    package_service.transport_package(flight, package2)
    package_service.transport_package(flight, package3)

    assert package1.flight is flight
    assert package2.flight is flight
    assert package3.flight is flight
