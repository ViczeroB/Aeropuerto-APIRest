from sqlalchemy.orm import Session
from .. import models, schemas

def get_sobrecargo(db: Session, sobrecargo_id: int):
    return db.query(models.Sobrecargo).filter(models.Sobrecargo.idSobrecargo == sobrecargo_id).first()

def get_sobrecargos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sobrecargo).offset(skip).limit(limit).all()

def create_sobrecargo(db: Session, sobrecargo: schemas.SobrecargoCreate):
    db_sobrecargo = models.Sobrecargo(**sobrecargo.dict())
    db.add(db_sobrecargo)
    db.commit()
    db.refresh(db_sobrecargo)
    return db_sobrecargo

def update_sobrecargo(db: Session, sobrecargo_id: int, sobrecargo: schemas.SobrecargoCreate):
    db_sobrecargo = get_sobrecargo(db, sobrecargo_id)
    if db_sobrecargo:
        update_data = sobrecargo.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_sobrecargo, key, value)
        db.commit()
        db.refresh(db_sobrecargo)
    return db_sobrecargo

def delete_sobrecargo(db: Session, sobrecargo_id: int):
    db_sobrecargo = get_sobrecargo(db, sobrecargo_id)
    if db_sobrecargo:
        db.delete(db_sobrecargo)
        db.commit()
    return db_sobrecargo