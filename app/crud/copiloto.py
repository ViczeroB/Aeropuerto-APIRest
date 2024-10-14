from sqlalchemy.orm import Session
from .. import models, schemas

def get_copiloto(db: Session, copiloto_id: int):
    return db.query(models.Copiloto).filter(models.Copiloto.idCopiloto == copiloto_id).first()

def get_copilotos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Copiloto).offset(skip).limit(limit).all()

def create_copiloto(db: Session, copiloto: schemas.CopilotoCreate):
    db_copiloto = models.Copiloto(**copiloto.dict())
    db.add(db_copiloto)
    db.commit()
    db.refresh(db_copiloto)
    return db_copiloto

def update_copiloto(db: Session, copiloto_id: int, copiloto: schemas.CopilotoCreate):
    db_copiloto = get_copiloto(db, copiloto_id)
    if db_copiloto:
        update_data = copiloto.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_copiloto, key, value)
        db.commit()
        db.refresh(db_copiloto)
    return db_copiloto

def delete_copiloto(db: Session, copiloto_id: int):
    db_copiloto = get_copiloto(db, copiloto_id)
    if db_copiloto:
        db.delete(db_copiloto)
        db.commit()
    return db_copiloto