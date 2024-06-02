from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, create_tables
from schemas import CountUpdate, SchoolHouse, SchoolHouseCreate
from crud import update_schoolHouse_count, create_schoolhouse, fetch_all_schoolhouses
from typing import List

app = FastAPI()

create_tables()


def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


@app.post("/schoolhouse/update", response_model=SchoolHouse)
def update_schoolhouse_count(count_update: CountUpdate, db: Session = Depends(get_db)):
    updated = update_schoolHouse_count(db, count_update.id, count_update.delta)
    if not updated:
        raise HTTPException(status_code=404, detail="SchoolHouse not found")
    return updated



@app.post("/schoolhouse/", response_model=SchoolHouse)
def create_schoolhouse_record(schoolhouse: SchoolHouseCreate, db: Session = Depends(get_db)):
    return create_schoolhouse(db, schoolhouse)



@app.get('/schoolhouses/', response_model=List[SchoolHouse])
def get_all_schoolhouses(db: Session = Depends(get_db)):
    return fetch_all_schoolhouses(db)
