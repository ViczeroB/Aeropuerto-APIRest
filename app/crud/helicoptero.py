from sqlalchemy.orm import Session
from .. import models, schemas

def get_helicoptero(db: Session, helicoptero_id: int):
    return db.query(models.Helicoptero).filter(models.Helicoptero.idHelicoptero == helicoptero_id).first()

def get_helicopteros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Helicoptero).offset(skip).limit(limit).all()

def create_helicoptero(db: Session, helicoptero: schemas.HelicopteroCreate):
    db_helicoptero = models.Helicoptero(**helicoptero.dict())
    db.add(db_helicoptero)
    db.commit()
    db.refresh(db_helicoptero)
    return db_helicoptero

def update_helicoptero(db: Session, helicoptero_id: int, helicoptero: schemas.HelicopteroCreate):
    db_helicoptero = get_helicoptero(db, helicoptero_id)
    if db_helicoptero:
        update_data = helicoptero.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_helicoptero, key, value)
        db.commit()
        db.refresh(db_helicoptero)
    return db_helicoptero

def delete_helicoptero(db: Session, helicoptero_id: int):
    db_helicoptero = get_helicoptero(db, helicoptero_id)
    if db_helicoptero:
        db.delete(db_helicoptero)
        db.commit()
    return db_helicoptero