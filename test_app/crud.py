from sqlalchemy.orm import Session
import models
import schemas

def get_city(db: Session, city_name: str):
    return db.query(models.City).filter(models.City.Name == city_name).first()

def get_all_city(db: Session):
    return db.query(models.City).all()
