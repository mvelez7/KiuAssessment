from models import db
from datetime import datetime
from models.flight import Flight
from models.location import Location


def create_new_flight(on: datetime.date, origin: Location, desination: Location) -> Flight:
    """
    Creates a new flight for a date
    It uses a dummy database (db) to insert the flight and gets an id for it.
    """
    flight = Flight(on, origin, desination)

    db.insert_flight(flight)
    return flight
