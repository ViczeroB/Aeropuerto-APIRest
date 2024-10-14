from sqlalchemy.orm import Session
from .. import models, schemas

def get_tripulacion(db: Session, tripulacion_id: int):
    return db.query(models.Tripulacion).filter(models.Tripulacion.idTripulacion == tripulacion_id).first()

def get_tripulaciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tripulacion).offset(skip).limit(limit).all()

def create_tripulacion(db: Session, tripulacion: schemas.TripulacionCreate):
    db_tripulacion = models.Tripulacion(**tripulacion.dict())
    db.add(db_tripulacion)
    db.commit()
    db.refresh(db_tripulacion)
    return db_tripulacion

def update_tripulacion(db: Session, tripulacion_id: int, tripulacion: schemas.TripulacionCreate):
    db_tripulacion = get_tripulacion(db, tripulacion_id)
    if db_tripulacion:
        update_data = tripulacion.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_tripulacion, key, value)
        db.commit()
        db.refresh(db_tripulacion)
    return db_tripulacion

def delete_tripulacion(db: Session, tripulacion_id: int):
    db_tripulacion = get_tripulacion(db, tripulacion_id)
    if db_tripulacion:
        db.delete(db_tripulacion)
        db.commit()
    return db_tripulacion