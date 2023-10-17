from datetime import datetime
from services import flight_service


def test_create_new_flight():
    flight_date = datetime.now()
    new_flight = flight_service.create_new_flight(flight_date)

    assert new_flight.on == flight_date
    assert new_flight.id == 1
    assert len(new_flight.packages) == 0
