from sqlalchemy.orm import Session
from .. import models, schemas
from typing import List

def get_vuelo(db: Session, vuelo_id: int):
    return db.query(models.Vuelo).filter(models.Vuelo.idVuelo == vuelo_id).first()

def get_vuelos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vuelo).offset(skip).limit(limit).all()

def create_vuelo(db: Session, vuelo: schemas.VueloCreate):
    db_vuelo = models.Vuelo(**vuelo.dict())
    db.add(db_vuelo)
    db.commit()
    db.refresh(db_vuelo)
    return db_vuelo

def update_vuelo(db: Session, vuelo_id: int, vuelo: schemas.VueloCreate):
    db_vuelo = get_vuelo(db, vuelo_id)
    if db_vuelo:
        update_data = vuelo.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_vuelo, key, value)
        db.commit()
        db.refresh(db_vuelo)
    return db_vuelo

def delete_vuelo(db: Session, vuelo_id: int):
    db_vuelo = get_vuelo(db, vuelo_id)
    if db_vuelo:
        db.delete(db_vuelo)
        db.commit()
    return db_vuelo

def get_pasajeros_by_vuelo(db: Session, vuelo_id: int) -> List[models.Pasajero]:
    return db.query(models.Pasajero).join(models.Boleto).filter(models.Boleto.idVuelo == vuelo_id).all()