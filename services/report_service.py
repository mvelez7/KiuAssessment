import logging
from datetime import datetime
from typing import List, Final
from dataclasses import dataclass
from collections import defaultdict

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

    def log_details(self):
        """
        Log more details about the packages information (locations, owners, flights)
        """
        logging.info(f'A total of {len(self.packages)} packages were transported on {self.date}')
        flight_2_packages = defaultdict(list)
        for package in self.packages:
            flight_2_packages[package.flight].append(package)

        for flight, packages in flight_2_packages.items():
            logging.info(f"*{len(packages)} packages transported on {flight}")
            for package in packages:
                logging.info(f"**{package}")

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
    in case more details are needed (see PackageTransportReport.log_details method).
    """
    transported_packages: List[Package] = db.find_all_transported_packages_on(on)
    report = PackageTransportReport(on, transported_packages)
    logging.debug(f'Packages transport report: {report}')

    return report
