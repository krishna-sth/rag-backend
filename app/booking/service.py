from app.db.session import SessionLocal
from app.db.models import Booking

def save_booking(data: dict):
    db = SessionLocal()
    booking = Booking(
        name=data["name"],
        email=data["email"],
        date=data["date"],
        time=data["time"]
    )
    db.add(booking)
    db.commit()
    db.close()
