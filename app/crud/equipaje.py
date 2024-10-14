from sqlalchemy.orm import Session
from .. import models, schemas

def get_equipaje(db: Session, equipaje_id: int):
    return db.query(models.Equipaje).filter(models.Equipaje.idEquipaje == equipaje_id).first()

def get_equipajes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Equipaje).offset(skip).limit(limit).all()

def create_equipaje(db: Session, equipaje: schemas.EquipajeCreate):
    db_equipaje = models.Equipaje(**equipaje.dict())
    db.add(db_equipaje)
    db.commit()
    db.refresh(db_equipaje)
    return db_equipaje

def update_equipaje(db: Session, equipaje_id: int, equipaje: schemas.EquipajeCreate):
    db_equipaje = get_equipaje(db, equipaje_id)
    if db_equipaje:
        update_data = equipaje.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_equipaje, key, value)
        db.commit()
        db.refresh(db_equipaje)
    return db_equipaje

def delete_equipaje(db: Session, equipaje_id: int):
    db_equipaje = get_equipaje(db, equipaje_id)
    if db_equipaje:
        db.delete(db_equipaje)
        db.commit()
    return db_equipaje