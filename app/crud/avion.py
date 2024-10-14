from sqlalchemy.orm import Session
from .. import models, schemas

def get_avion(db: Session, avion_id: int):
    return db.query(models.Avion).filter(models.Avion.idAvion == avion_id).first()

def get_aviones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Avion).offset(skip).limit(limit).all()

def create_avion(db: Session, avion: schemas.AvionCreate):
    db_avion = models.Avion(**avion.dict())
    db.add(db_avion)
    db.commit()
    db.refresh(db_avion)
    return db_avion

def update_avion(db: Session, avion_id: int, avion: schemas.AvionCreate):
    db_avion = get_avion(db, avion_id)
    if db_avion:
        update_data = avion.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_avion, key, value)
        db.commit()
        db.refresh(db_avion)
    return db_avion

def delete_avion(db: Session, avion_id: int):
    db_avion = get_avion(db, avion_id)
    if db_avion:
        db.delete(db_avion)
        db.commit()
    return db_avion