import logging
from datetime import datetime
from typing import List, Final
from dataclasses import dataclass

from models import db
from models.package import Package


PROFIT_PER_PACKAGE: Final[int] = 10


@dataclass
class PackageTransportReport:
    date: datetime.date
    packages: List[Package]

    def profits(self) -> int:
        return self.total_transported_packages() * PROFIT_PER_PACKAGE

    def total_transported_packages(self) -> int:
        return len(self.packages)

    def __repr__(self) -> str:
        return (f"A total of {self.total_transported_packages()} packages were transported "
                f"on {self.date} with a profit of ${self.profits()}")

    def __str__(self) -> str:
        return self.__repr__()


def create_packages_transport_report_on_date(on: datetime.date) -> PackageTransportReport:
    """
    Generates a simple package transport report of a specific date.

    It only logs the total of packages transported on the date, and the profits earned by the company.
    But all the information (clients, flight, locations) should be accessible in the PackageTransportReport object
    in case more details are needed.
    """
    transported_packages: List[Package] = db.find_all_transported_packages_on(on)
    report = PackageTransportReport(on, transported_packages)

    logging.info(f'Packages transport report: {report}')
    return report
