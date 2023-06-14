from typing import Optional
from pydantic import BaseModel

class City(BaseModel):
    ID: Optional[int]
    Name: Optional[str]
    CountryCode: Optional[str]
    District: Optional[str]
    Population: Optional[int]

    class Config:
        orm_mode = True
