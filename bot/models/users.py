from datetime import datetime

from sqlalchemy import Column, BigInteger, DateTime, String

from db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    created = Column(DateTime, default=datetime.utcnow)

    fullname = Column(String)
    username = Column(String)

