from app.db.session import engine, Base
from app.db.models import Document, Booking

def init_db():
    Base.metadata.create_all(bind=engine)
