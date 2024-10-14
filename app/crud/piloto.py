from sqlalchemy.orm import Session
from .. import models, schemas

def get_piloto(db: Session, piloto_id: int):
    return db.query(models.Piloto).filter(models.Piloto.idPiloto == piloto_id).first()

def get_pilotos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Piloto).offset(skip).limit(limit).all()

def create_piloto(db: Session, piloto: schemas.PilotoCreate):
    db_piloto = models.Piloto(**piloto.dict())
    db.add(db_piloto)
    db.commit()
    db.refresh(db_piloto)
    return db_piloto

def update_piloto(db: Session, piloto_id: int, piloto: schemas.PilotoCreate):
    db_piloto = get_piloto(db, piloto_id)
    if db_piloto:
        update_data = piloto.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_piloto, key, value)
        db.commit()
        db.refresh(db_piloto)
    return db_piloto

def delete_piloto(db: Session, piloto_id: int):
    db_piloto = get_piloto(db, piloto_id)
    if db_piloto:
        db.delete(db_piloto)
        db.commit()
    return db_piloto