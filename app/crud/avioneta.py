from sqlalchemy.orm import Session
from .. import models, schemas

def get_avioneta(db: Session, avioneta_id: int):
    return db.query(models.Avioneta).filter(models.Avioneta.idAvioneta == avioneta_id).first()

def get_avionetas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Avioneta).offset(skip).limit(limit).all()

def create_avioneta(db: Session, avioneta: schemas.AvionetaCreate):
    db_avioneta = models.Avioneta(**avioneta.dict())
    db.add(db_avioneta)
    db.commit()
    db.refresh(db_avioneta)
    return db_avioneta

def update_avioneta(db: Session, avioneta_id: int, avioneta: schemas.AvionetaCreate):
    db_avioneta = get_avioneta(db, avioneta_id)
    if db_avioneta:
        update_data = avioneta.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_avioneta, key, value)
        db.commit()
        db.refresh(db_avioneta)
    return db_avioneta

def delete_avioneta(db: Session, avioneta_id: int):
    db_avioneta = get_avioneta(db, avioneta_id)
    if db_avioneta:
        db.delete(db_avioneta)
        db.commit()
    return db_avioneta