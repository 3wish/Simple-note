from sqlalchemy.orm import sessionmaker
from app.database.db import engine


def get_session():
    Session = sessionmaker(engine)
    session: Session = Session()
    try:
        yield session
    finally:
        session.close()
