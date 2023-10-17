import logging
from datetime import datetime, timedelta

from models.person import Person
from models.location import Location
from services import report_service, flight_service, package_service

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s][%(levelname)s]%(message)s')


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
client_1 = Person('Person1', is_client=True)
client_2 = Person('Person2', is_client=True)
client_3 = Person('Person3', is_client=True)
client_4 = Person('Person4', is_client=True)
client_5 = Person('Person5', is_client=True)
client_6 = Person('Person6', is_client=True)
client_7 = Person('Person7', is_client=True)
client_8 = Person('Person8', is_client=True)
client_9 = Person('Person9', is_client=True)

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

report_service.create_packages_transport_report_on_date(date_1)
report_service.create_packages_transport_report_on_date(date_2)
report_service.create_packages_transport_report_on_date(date_3)
