from sqlalchemy.orm import Session
from .. import models, schemas

def get_boleto(db: Session, boleto_id: int):
    return db.query(models.Boleto).filter(models.Boleto.idBoleto == boleto_id).first()

def get_boletos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Boleto).offset(skip).limit(limit).all()

def create_boleto(db: Session, boleto: schemas.BoletoCreate):
    db_boleto = models.Boleto(**boleto.dict())
    db.add(db_boleto)
    db.commit()
    db.refresh(db_boleto)
    return db_boleto

def update_boleto(db: Session, boleto_id: int, boleto: schemas.BoletoCreate):
    db_boleto = get_boleto(db, boleto_id)
    if db_boleto:
        update_data = boleto.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_boleto, key, value)
        db.commit()
        db.refresh(db_boleto)
    return db_boleto

def delete_boleto(db: Session, boleto_id: int):
    db_boleto = get_boleto(db, boleto_id)
    if db_boleto:
        db.delete(db_boleto)
        db.commit()
    return db_boleto