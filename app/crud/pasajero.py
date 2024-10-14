from sqlalchemy.orm import Session
from .. import models, schemas

def get_pasajero(db: Session, pasajero_id: int):
    return db.query(models.Pasajero).filter(models.Pasajero.idPasajero == pasajero_id).first()

def get_pasajeros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pasajero).offset(skip).limit(limit).all()

def create_pasajero(db: Session, pasajero: schemas.PasajeroCreate):
    db_pasajero = models.Pasajero(**pasajero.dict())
    db.add(db_pasajero)
    db.commit()
    db.refresh(db_pasajero)
    return db_pasajero

def update_pasajero(db: Session, pasajero_id: int, pasajero: schemas.PasajeroCreate):
    db_pasajero = get_pasajero(db, pasajero_id)
    if db_pasajero:
        update_data = pasajero.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_pasajero, key, value)
        db.commit()
        db.refresh(db_pasajero)
    return db_pasajero

def delete_pasajero(db: Session, pasajero_id: int):
    db_pasajero = get_pasajero(db, pasajero_id)
    if db_pasajero:
        db.delete(db_pasajero)
        db.commit()
    return db_pasajero