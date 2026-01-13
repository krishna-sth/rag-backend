from sqlalchemy import Column, Integer, String, Date, Time
from app.db.session import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    chunk_count = Column(Integer)

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    date = Column(Date)
    time = Column(Time)
