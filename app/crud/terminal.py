from sqlalchemy.orm import Session
from .. import models, schemas

def get_terminal(db: Session, terminal_id: int):
    return db.query(models.Terminal).filter(models.Terminal.idTerminal == terminal_id).first()

def get_terminales(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Terminal).offset(skip).limit(limit).all()

def create_terminal(db: Session, terminal: schemas.TerminalCreate):
    db_terminal = models.Terminal(**terminal.dict())
    db.add(db_terminal)
    db.commit()
    db.refresh(db_terminal)
    return db_terminal

def update_terminal(db: Session, terminal_id: int, terminal: schemas.TerminalCreate):
    db_terminal = get_terminal(db, terminal_id)
    if db_terminal:
        update_data = terminal.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_terminal, key, value)
        db.commit()
        db.refresh(db_terminal)
    return db_terminal

def delete_terminal(db: Session, terminal_id: int):
    db_terminal = get_terminal(db, terminal_id)
    if db_terminal:
        db.delete(db_terminal)
        db.commit()
    return db_terminal