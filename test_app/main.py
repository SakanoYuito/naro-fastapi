from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import crud
import models
import schemas
from database import SessionLocal, engine
import uvicorn

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

@app.get("/cities/{city_name}", response_model=schemas.City)
def get_city(city_name: str, db: Session = Depends(get_db)):
    db_city = crud.get_city(db, city_name=city_name)
    if db_city is None:
        raise HTTPException(status_code=404, detail=f"No such city : {city_name}")
    return db_city

@app.get("/allCity", response_model=List[schemas.City])
def get_all_city(db: Session = Depends(get_db)):
    db_cities = crud.get_all_city(db)
    # if city_name is None:
    #     raise HTTPException(status_code=404, detail=f"No such city : {city_name}")
    return db_cities

if __name__ == '__main__':
    uvicorn.run(app=app)