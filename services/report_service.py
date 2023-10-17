import logging
from datetime import datetime
from typing import List, Final
from dataclasses import dataclass

from models import db
from models.package import Package


logger = logging.getLogger()


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


def packages_report(on: datetime.date) -> PackageTransportReport:
    transported_packages: List[Package] = db.find_all_transported_packages_on(on)
    report = PackageTransportReport(on, transported_packages)

    logger.info(f'Packages transport report: {report}')
    return report
