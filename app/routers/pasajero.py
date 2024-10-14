from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/pasajeros/", response_model=schemas.Pasajero)
def create_pasajero(pasajero: schemas.PasajeroCreate, db: Session = Depends(get_db)):
    return crud.create_pasajero(db=db, pasajero=pasajero)

@router.get("/pasajeros/", response_model=List[schemas.Pasajero])
def read_pasajeros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pasajeros = crud.get_pasajeros(db, skip=skip, limit=limit)
    return pasajeros