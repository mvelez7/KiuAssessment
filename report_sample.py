import logging
from datetime import datetime, timedelta

from models.person import Person
from services import report_service, flight_service, package_service


logging.basicConfig(level=logging.DEBUG)


flight_1_date = datetime.now() - timedelta(days=1)
flight_2_date = datetime.now() - timedelta(days=2)
flight_3_date = datetime.now() - timedelta(days=3)
flight_1 = flight_service.create_new_flight(flight_1_date)
flight_2 = flight_service.create_new_flight(flight_2_date)
flight_3 = flight_service.create_new_flight(flight_3_date)
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

report_1 = report_service.packages_report(flight_1.on)
report_2 = report_service.packages_report(flight_2.on)
report_3 = report_service.packages_report(flight_3.on)