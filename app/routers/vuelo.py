from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/vuelos/", response_model=schemas.Vuelo)
def create_vuelo(vuelo: schemas.VueloCreate, db: Session = Depends(get_db)):
    return crud.create_vuelo(db=db, vuelo=vuelo)

@router.get("/vuelos/", response_model=List[schemas.Vuelo])
def read_vuelos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vuelos = crud.get_vuelos(db, skip=skip, limit=limit)
    return vuelos

@router.get("/vuelos/{vuelo_id}", response_model=schemas.Vuelo)
def read_vuelo(vuelo_id: int, db: Session = Depends(get_db)):
    db_vuelo = crud.get_vuelo(db, vuelo_id=vuelo_id)
    if db_vuelo is None:
        raise HTTPException(status_code=404, detail="Vuelo not found")
    return db_vuelo

@router.put("/vuelos/{vuelo_id}", response_model=schemas.Vuelo)
def update_vuelo(vuelo_id: int, vuelo: schemas.VueloCreate, db: Session = Depends(get_db)):
    db_vuelo = crud.update_vuelo(db, vuelo_id=vuelo_id, vuelo=vuelo)
    if db_vuelo is None:
        raise HTTPException(status_code=404, detail="Vuelo not found")
    return db_vuelo

@router.delete("/vuelos/{vuelo_id}", response_model=schemas.Vuelo)
def delete_vuelo(vuelo_id: int, db: Session = Depends(get_db)):
    db_vuelo = crud.delete_vuelo(db, vuelo_id=vuelo_id)
    if db_vuelo is None:
        raise HTTPException(status_code=404, detail="Vuelo not found")
    return db_vuelo

@router.get("/vuelos/{vuelo_id}/pasajeros", response_model=List[schemas.Pasajero])
def read_pasajeros_by_vuelo(vuelo_id: int, db: Session = Depends(get_db)):
    pasajeros = crud.get_pasajeros_by_vuelo(db, vuelo_id=vuelo_id)
    if not pasajeros:
        raise HTTPException(status_code=404, detail="No se encontraron pasajeros para este vuelo")
    return pasajeros

# Puedes agregar más endpoints relacionados con vuelos aquí, por ejemplo:
# - Obtener todos los vuelos de un día específico
# - Obtener vuelos por origen o destino
# - Obtener detalles del vehículo aéreo asociado a un vuelo
# - etc.