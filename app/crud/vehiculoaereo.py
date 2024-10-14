from sqlalchemy.orm import Session
from .. import models, schemas

def get_vehiculo_aereo(db: Session, vehiculo_id: int):
    return db.query(models.VehiculoAereo).filter(models.VehiculoAereo.idVehiculoAereo == vehiculo_id).first()

def get_vehiculos_aereos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.VehiculoAereo).offset(skip).limit(limit).all()

def create_vehiculo_aereo(db: Session, vehiculo: schemas.VehiculoAereoCreate):
    db_vehiculo = models.VehiculoAereo(**vehiculo.dict())
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def update_vehiculo_aereo(db: Session, vehiculo_id: int, vehiculo: schemas.VehiculoAereoCreate):
    db_vehiculo = get_vehiculo_aereo(db, vehiculo_id)
    if db_vehiculo:
        update_data = vehiculo.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_vehiculo, key, value)
        db.commit()
        db.refresh(db_vehiculo)
    return db_vehiculo

def delete_vehiculo_aereo(db: Session, vehiculo_id: int):
    db_vehiculo = get_vehiculo_aereo(db, vehiculo_id)
    if db_vehiculo:
        db.delete(db_vehiculo)
        db.commit()
    return db_vehiculo