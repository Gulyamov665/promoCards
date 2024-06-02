# schemas.py
from pydantic import BaseModel


class CountUpdate(BaseModel):
    id: int
    delta: int


class SchoolHouse(BaseModel):
    id: int
    count: int
    name: str

    class Config:
        orm_mode = True



class SchoolHouseCreate(BaseModel):
    name: str
    count: int
