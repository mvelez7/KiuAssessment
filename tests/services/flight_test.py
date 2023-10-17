from datetime import datetime
from services import flight_service
from models.location import Location


def test_create_new_flight():
    flight_date = datetime.now()
    cordoba = Location('Cordoba')
    bsas = Location('Buenos Aires')
    new_flight = flight_service.create_new_flight(flight_date, cordoba, bsas)

    assert new_flight.on == flight_date
    assert new_flight.id == 1
    assert new_flight.origin is cordoba
    assert new_flight.destination is bsas

