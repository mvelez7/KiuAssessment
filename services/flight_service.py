from models import db
from datetime import datetime
from models.flight import Flight


def create_new_flight(on: datetime.date) -> Flight:
    flight = Flight(on)

    db.insert_flight(flight)
    return flight
