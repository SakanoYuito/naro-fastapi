from sqlalchemy import Column, Integer, String
from database import Base

class City(Base):
    __tablename__ = "city"

    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    CountryCode = Column(String(3))
    District = Column(String)
    Population = Column(Integer)