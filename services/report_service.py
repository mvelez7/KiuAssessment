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
    date: datetime
    total_packages: int

    @property
    def profits(self) -> int:
        return self.total_packages * PROFIT_PER_PACKAGE


def packages_report(on: datetime) -> PackageTransportReport:
    transported_packages: List[Package] = db.find_all_transported_packages_on(on)
    report = PackageTransportReport(on, len(transported_packages))

    logger.info(f"A total of {report.total_packages} packages were transported on {on} with a profit of ${report.profits}")
    return report
