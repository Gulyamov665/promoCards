# crud.py
from sqlalchemy.orm import Session
from sqlalchemy import update, insert, select
from models import schoolHouse
from schemas import SchoolHouseCreate


def fetch_all_schoolhouses(db: Session):
    return db.execute(select(schoolHouse)).fetchall()

def update_schoolHouse_count(db: Session, id: int, delta: int):
    stmt = update(schoolHouse).where(schoolHouse.c.id == id).values(count=schoolHouse.c.count + delta)
    db.execute(stmt)
    db.commit()
    return db.execute(schoolHouse.select().where(schoolHouse.c.id == id)).first()


def create_schoolhouse(db: Session, schoolhouse: SchoolHouseCreate):
    stmt = insert(schoolHouse).values(name=schoolhouse.name, count=schoolhouse.count)
    db.execute(stmt)
    db.commit()
    return db.execute(schoolHouse.select().order_by(schoolHouse.c.id.desc())).first()

