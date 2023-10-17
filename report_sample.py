import logging
from datetime import datetime, timedelta

from models.person import Person
from models.location import Location
from services import report_service, flight_service, package_service

logging.basicConfig(level=logging.INFO, format='[%(asctime)s][%(levelname)s]%(message)s')


date_1 = datetime.now().date() - timedelta(days=3)
date_2 = datetime.now().date() - timedelta(days=2)
date_3 = datetime.now().date() - timedelta(days=1)
cordoba = Location('Cordoba')
bsas = Location('Buenos Aires')
tucuman = Location('Tucuman')
misiones = Location('Misiones')
flight_1 = flight_service.create_new_flight(date_1, cordoba, bsas)
flight_2 = flight_service.create_new_flight(date_2, bsas, misiones)
flight_3 = flight_service.create_new_flight(date_3, tucuman, cordoba)
flight_4 = flight_service.create_new_flight(date_2, tucuman, misiones)  # same date as flight1
client_1 = Person('Juan', is_client=True)
client_2 = Person('Mariana', is_client=True)
client_3 = Person('Matias', is_client=True)
client_4 = Person('Georgina', is_client=True)
client_5 = Person('Lucila', is_client=True)
client_6 = Person('Lucas', is_client=True)
client_7 = Person('Mateo', is_client=True)
client_8 = Person('Morena', is_client=True)
client_9 = Person('Fabrizio', is_client=True)

package_service.transport_package(flight_1, package_service.create_new_package(client_1))
package_service.transport_package(flight_1, package_service.create_new_package(client_2))
package_service.transport_package(flight_1, package_service.create_new_package(client_3))
package_service.transport_package(flight_2, package_service.create_new_package(client_4))
package_service.transport_package(flight_2, package_service.create_new_package(client_5))
package_service.transport_package(flight_3, package_service.create_new_package(client_6))
package_service.transport_package(flight_3, package_service.create_new_package(client_7))
package_service.transport_package(flight_3, package_service.create_new_package(client_8))
package_service.transport_package(flight_3, package_service.create_new_package(client_9))
package_service.transport_package(flight_4, package_service.create_new_package(client_9))
package_service.transport_package(flight_4, package_service.create_new_package(client_9))
package_service.transport_package(flight_4, package_service.create_new_package(client_8))
package_service.transport_package(flight_4, package_service.create_new_package(client_7))
package_service.transport_package(flight_4, package_service.create_new_package(client_5))

report_1 = report_service.create_packages_transport_report_on_date(date_1)
report_2 = report_service.create_packages_transport_report_on_date(date_2)
report_3 = report_service.create_packages_transport_report_on_date(date_3)

report_1.log_details()
report_2.log_details()
report_3.log_details()
