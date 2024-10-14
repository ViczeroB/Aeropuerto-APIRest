from sqlalchemy.orm import Session
from .. import models, schemas

def get_aeropuerto(db: Session, aeropuerto_id: int):
    return db.query(models.Aeropuerto).filter(models.Aeropuerto.idAeropuerto == aeropuerto_id).first()

def get_aeropuertos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Aeropuerto).offset(skip).limit(limit).all()

def create_aeropuerto(db: Session, aeropuerto: schemas.AeropuertoCreate):
    db_aeropuerto = models.Aeropuerto(**aeropuerto.dict())
    db.add(db_aeropuerto)
    db.commit()
    db.refresh(db_aeropuerto)
    return db_aeropuerto

def update_aeropuerto(db: Session, aeropuerto_id: int, aeropuerto: schemas.AeropuertoCreate):
    db_aeropuerto = get_aeropuerto(db, aeropuerto_id)
    if db_aeropuerto:
        update_data = aeropuerto.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_aeropuerto, key, value)
        db.commit()
        db.refresh(db_aeropuerto)
    return db_aeropuerto

def delete_aeropuerto(db: Session, aeropuerto_id: int):
    db_aeropuerto = get_aeropuerto(db, aeropuerto_id)
    if db_aeropuerto:
        db.delete(db_aeropuerto)
        db.commit()
    return db_aeropuerto