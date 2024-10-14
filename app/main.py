from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
from . import models
from .database import engine
from .routers import vuelo, pasajero

from . import crud, models, schemas
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

# router = APIRouter()

app = FastAPI()

app.include_router(vuelo.router)
app.include_router(pasajero.router)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Aeropuerto
@app.post("/aeropuertos/", response_model=schemas.Aeropuerto)
def create_aeropuerto(aeropuerto: schemas.AeropuertoCreate, db: Session = Depends(get_db)):
    return crud.create_aeropuerto(db=db, aeropuerto=aeropuerto)

@app.get("/aeropuertos/", response_model=List[schemas.Aeropuerto])
def read_aeropuertos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    aeropuertos = crud.get_aeropuertos(db, skip=skip, limit=limit)
    return aeropuertos

@app.get("/aeropuertos/{aeropuerto_id}", response_model=schemas.Aeropuerto)
def read_aeropuerto(aeropuerto_id: int, db: Session = Depends(get_db)):
    db_aeropuerto = crud.get_aeropuerto(db, aeropuerto_id=aeropuerto_id)
    if db_aeropuerto is None:
        raise HTTPException(status_code=404, detail="Aeropuerto not found")
    return db_aeropuerto

@app.put("/aeropuertos/{aeropuerto_id}", response_model=schemas.Aeropuerto)
def update_aeropuerto(aeropuerto_id: int, aeropuerto: schemas.AeropuertoCreate, db: Session = Depends(get_db)):
    db_aeropuerto = crud.update_aeropuerto(db, aeropuerto_id=aeropuerto_id, aeropuerto=aeropuerto)
    if db_aeropuerto is None:
        raise HTTPException(status_code=404, detail="Aeropuerto not found")
    return db_aeropuerto

@app.delete("/aeropuertos/{aeropuerto_id}", response_model=schemas.Aeropuerto)
def delete_aeropuerto(aeropuerto_id: int, db: Session = Depends(get_db)):
    db_aeropuerto = crud.delete_aeropuerto(db, aeropuerto_id=aeropuerto_id)
    if db_aeropuerto is None:
        raise HTTPException(status_code=404, detail="Aeropuerto not found")
    return db_aeropuerto

# Terminal
@app.post("/terminales/", response_model=schemas.Terminal)
def create_terminal(terminal: schemas.TerminalCreate, db: Session = Depends(get_db)):
    return crud.create_terminal(db=db, terminal=terminal)

@app.get("/terminales/", response_model=List[schemas.Terminal])
def read_terminales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    terminales = crud.get_terminales(db, skip=skip, limit=limit)
    return terminales

@app.get("/terminales/{terminal_id}", response_model=schemas.Terminal)
def read_terminal(terminal_id: int, db: Session = Depends(get_db)):
    db_terminal = crud.get_terminal(db, terminal_id=terminal_id)
    if db_terminal is None:
        raise HTTPException(status_code=404, detail="Terminal not found")
    return db_terminal

@app.put("/terminales/{terminal_id}", response_model=schemas.Terminal)
def update_terminal(terminal_id: int, terminal: schemas.TerminalCreate, db: Session = Depends(get_db)):
    db_terminal = crud.update_terminal(db, terminal_id=terminal_id, terminal=terminal)
    if db_terminal is None:
        raise HTTPException(status_code=404, detail="Terminal not found")
    return db_terminal

@app.delete("/terminales/{terminal_id}", response_model=schemas.Terminal)
def delete_terminal(terminal_id: int, db: Session = Depends(get_db)):
    db_terminal = crud.delete_terminal(db, terminal_id=terminal_id)
    if db_terminal is None:
        raise HTTPException(status_code=404, detail="Terminal not found")
    return db_terminal

# Vuelo
@app.post("/vuelos/", response_model=schemas.Vuelo)
def create_vuelo(vuelo: schemas.VueloCreate, db: Session = Depends(get_db)):
    return crud.create_vuelo(db=db, vuelo=vuelo)

@app.get("/vuelos/", response_model=List[schemas.Vuelo])
def read_vuelos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vuelos = crud.get_vuelos(db, skip=skip, limit=limit)
    return vuelos

@app.get("/vuelos/{vuelo_id}", response_model=schemas.Vuelo)
def read_vuelo(vuelo_id: int, db: Session = Depends(get_db)):
    db_vuelo = crud.get_vuelo(db, vuelo_id=vuelo_id)
    if db_vuelo is None:
        raise HTTPException(status_code=404, detail="Vuelo not found")
    return db_vuelo

@app.put("/vuelos/{vuelo_id}", response_model=schemas.Vuelo)
def update_vuelo(vuelo_id: int, vuelo: schemas.VueloCreate, db: Session = Depends(get_db)):
    db_vuelo = crud.update_vuelo(db, vuelo_id=vuelo_id, vuelo=vuelo)
    if db_vuelo is None:
        raise HTTPException(status_code=404, detail="Vuelo not found")
    return db_vuelo

@app.delete("/vuelos/{vuelo_id}", response_model=schemas.Vuelo)
def delete_vuelo(vuelo_id: int, db: Session = Depends(get_db)):
    db_vuelo = crud.delete_vuelo(db, vuelo_id=vuelo_id)
    if db_vuelo is None:
        raise HTTPException(status_code=404, detail="Vuelo not found")
    return db_vuelo

# VehiculoAereo
@app.post("/vehiculos-aereos/", response_model=schemas.VehiculoAereo)
def create_vehiculo_aereo(vehiculo: schemas.VehiculoAereoCreate, db: Session = Depends(get_db)):
    return crud.create_vehiculo_aereo(db=db, vehiculo=vehiculo)

@app.get("/vehiculos-aereos/", response_model=List[schemas.VehiculoAereo])
def read_vehiculos_aereos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vehiculos = crud.get_vehiculos_aereos(db, skip=skip, limit=limit)
    return vehiculos

@app.get("/vehiculos-aereos/{vehiculo_id}", response_model=schemas.VehiculoAereo)
def read_vehiculo_aereo(vehiculo_id: int, db: Session = Depends(get_db)):
    db_vehiculo = crud.get_vehiculo_aereo(db, vehiculo_id=vehiculo_id)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehículo aéreo not found")
    return db_vehiculo

@app.put("/vehiculos-aereos/{vehiculo_id}", response_model=schemas.VehiculoAereo)
def update_vehiculo_aereo(vehiculo_id: int, vehiculo: schemas.VehiculoAereoCreate, db: Session = Depends(get_db)):
    db_vehiculo = crud.update_vehiculo_aereo(db, vehiculo_id=vehiculo_id, vehiculo=vehiculo)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehículo aéreo not found")
    return db_vehiculo

@app.delete("/vehiculos-aereos/{vehiculo_id}", response_model=schemas.VehiculoAereo)
def delete_vehiculo_aereo(vehiculo_id: int, db: Session = Depends(get_db)):
    db_vehiculo = crud.delete_vehiculo_aereo(db, vehiculo_id=vehiculo_id)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehículo aéreo not found")
    return db_vehiculo

# Avion
@app.post("/aviones/", response_model=schemas.Avion)
def create_avion(avion: schemas.AvionCreate, db: Session = Depends(get_db)):
    return crud.create_avion(db=db, avion=avion)

@app.get("/aviones/", response_model=List[schemas.Avion])
def read_aviones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    aviones = crud.get_aviones(db, skip=skip, limit=limit)
    return aviones

@app.get("/aviones/{avion_id}", response_model=schemas.Avion)
def read_avion(avion_id: int, db: Session = Depends(get_db)):
    db_avion = crud.get_avion(db, avion_id=avion_id)
    if db_avion is None:
        raise HTTPException(status_code=404, detail="Avión not found")
    return db_avion

@app.put("/aviones/{avion_id}", response_model=schemas.Avion)
def update_avion(avion_id: int, avion: schemas.AvionCreate, db: Session = Depends(get_db)):
    db_avion = crud.update_avion(db, avion_id=avion_id, avion=avion)
    if db_avion is None:
        raise HTTPException(status_code=404, detail="Avión not found")
    return db_avion

@app.delete("/aviones/{avion_id}", response_model=schemas.Avion)
def delete_avion(avion_id: int, db: Session = Depends(get_db)):
    db_avion = crud.delete_avion(db, avion_id=avion_id)
    if db_avion is None:
        raise HTTPException(status_code=404, detail="Avión not found")
    return db_avion

# Avioneta
@app.post("/avionetas/", response_model=schemas.Avioneta)
def create_avioneta(avioneta: schemas.AvionetaCreate, db: Session = Depends(get_db)):
    return crud.create_avioneta(db=db, avioneta=avioneta)

@app.get("/avionetas/", response_model=List[schemas.Avioneta])
def read_avionetas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    avionetas = crud.get_avionetas(db, skip=skip, limit=limit)
    return avionetas

@app.get("/avionetas/{avioneta_id}", response_model=schemas.Avioneta)
def read_avioneta(avioneta_id: int, db: Session = Depends(get_db)):
    db_avioneta = crud.get_avioneta(db, avioneta_id=avioneta_id)
    if db_avioneta is None:
        raise HTTPException(status_code=404, detail="Avioneta not found")
    return db_avioneta

@app.put("/avionetas/{avioneta_id}", response_model=schemas.Avioneta)
def update_avioneta(avioneta_id: int, avioneta: schemas.AvionetaCreate, db: Session = Depends(get_db)):
    db_avioneta = crud.update_avioneta(db, avioneta_id=avioneta_id, avioneta=avioneta)
    if db_avioneta is None:
        raise HTTPException(status_code=404, detail="Avioneta not found")
    return db_avioneta

@app.delete("/avionetas/{avioneta_id}", response_model=schemas.Avioneta)
def delete_avioneta(avioneta_id: int, db: Session = Depends(get_db)):
    db_avioneta = crud.delete_avioneta(db, avioneta_id=avioneta_id)
    if db_avioneta is None:
        raise HTTPException(status_code=404, detail="Avioneta not found")
    return db_avioneta

# Helicoptero
@app.post("/helicopteros/", response_model=schemas.Helicoptero)
def create_helicoptero(helicoptero: schemas.HelicopteroCreate, db: Session = Depends(get_db)):
    return crud.create_helicoptero(db=db, helicoptero=helicoptero)

@app.get("/helicopteros/", response_model=List[schemas.Helicoptero])
def read_helicopteros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    helicopteros = crud.get_helicopteros(db, skip=skip, limit=limit)
    return helicopteros

@app.get("/helicopteros/{helicoptero_id}", response_model=schemas.Helicoptero)
def read_helicoptero(helicoptero_id: int, db: Session = Depends(get_db)):
    db_helicoptero = crud.get_helicoptero(db, helicoptero_id=helicoptero_id)
    if db_helicoptero is None:
        raise HTTPException(status_code=404, detail="Helicóptero not found")
    return db_helicoptero

@app.put("/helicopteros/{helicoptero_id}", response_model=schemas.Helicoptero)
def update_helicoptero(helicoptero_id: int, helicoptero: schemas.HelicopteroCreate, db: Session = Depends(get_db)):
    db_helicoptero = crud.update_helicoptero(db, helicoptero_id=helicoptero_id, helicoptero=helicoptero)
    if db_helicoptero is None:
        raise HTTPException(status_code=404, detail="Helicóptero not found")
    return db_helicoptero

@app.delete("/helicopteros/{helicoptero_id}", response_model=schemas.Helicoptero)
def delete_helicoptero(helicoptero_id: int, db: Session = Depends(get_db)):
    db_helicoptero = crud.delete_helicoptero(db, helicoptero_id=helicoptero_id)
    if db_helicoptero is None:
        raise HTTPException(status_code=404, detail="Helicóptero not found")
    return db_helicoptero

# Tripulacion
@app.post("/tripulaciones/", response_model=schemas.Tripulacion)
def create_tripulacion(tripulacion: schemas.TripulacionCreate, db: Session = Depends(get_db)):
    return crud.create_tripulacion(db=db, tripulacion=tripulacion)

@app.get("/tripulaciones/", response_model=List[schemas.Tripulacion])
def read_tripulaciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tripulaciones = crud.get_tripulaciones(db, skip=skip, limit=limit)
    return tripulaciones

@app.get("/tripulaciones/{tripulacion_id}", response_model=schemas.Tripulacion)
def read_tripulacion(tripulacion_id: int, db: Session = Depends(get_db)):
    db_tripulacion = crud.get_tripulacion(db, tripulacion_id=tripulacion_id)
    if db_tripulacion is None:
        raise HTTPException(status_code=404, detail="Tripulación not found")
    return db_tripulacion

@app.put("/tripulaciones/{tripulacion_id}", response_model=schemas.Tripulacion)
def update_tripulacion(tripulacion_id: int, tripulacion: schemas.TripulacionCreate, db: Session = Depends(get_db)):
    db_tripulacion = crud.update_tripulacion(db, tripulacion_id=tripulacion_id, tripulacion=tripulacion)
    if db_tripulacion is None:
        raise HTTPException(status_code=404, detail="Tripulación not found")
    return db_tripulacion

@app.delete("/tripulaciones/{tripulacion_id}", response_model=schemas.Tripulacion)
def delete_tripulacion(tripulacion_id: int, db: Session = Depends(get_db)):
    db_tripulacion = crud.delete_tripulacion(db, tripulacion_id=tripulacion_id)
    if db_tripulacion is None:
        raise HTTPException(status_code=404, detail="Tripulación not found")
    return db_tripulacion

# Piloto
@app.post("/pilotos/", response_model=schemas.Piloto)
def create_piloto(piloto: schemas.PilotoCreate, db: Session = Depends(get_db)):
    return crud.create_piloto(db=db, piloto=piloto)

@app.get("/pilotos/", response_model=List[schemas.Piloto])
def read_pilotos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pilotos = crud.get_pilotos(db, skip=skip, limit=limit)
    return pilotos

@app.get("/pilotos/{piloto_id}", response_model=schemas.Piloto)
def read_piloto(piloto_id: int, db: Session = Depends(get_db)):
    db_piloto = crud.get_piloto(db, piloto_id=piloto_id)
    if db_piloto is None:
        raise HTTPException(status_code=404, detail="Piloto not found")
    return db_piloto

@app.put("/pilotos/{piloto_id}", response_model=schemas.Piloto)
def update_piloto(piloto_id: int, piloto: schemas.PilotoCreate, db: Session = Depends(get_db)):
    db_piloto = crud.update_piloto(db, piloto_id=piloto_id, piloto=piloto)
    if db_piloto is None:
        raise HTTPException(status_code=404, detail="Piloto not found")
    return db_piloto

@app.delete("/pilotos/{piloto_id}", response_model=schemas.Piloto)
def delete_piloto(piloto_id: int, db: Session = Depends(get_db)):
    db_piloto = crud.delete_piloto(db, piloto_id=piloto_id)
    if db_piloto is None:
        raise HTTPException(status_code=404, detail="Piloto not found")
    return db_piloto

# Copiloto
@app.post("/copilotos/", response_model=schemas.Copiloto)
def create_copiloto(copiloto: schemas.CopilotoCreate, db: Session = Depends(get_db)):
    return crud.create_copiloto(db=db, copiloto=copiloto)

@app.get("/copilotos/", response_model=List[schemas.Copiloto])
def read_copilotos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    copilotos = crud.get_copilotos(db, skip=skip, limit=limit)
    return copilotos

@app.get("/copilotos/{copiloto_id}", response_model=schemas.Copiloto)
def read_copiloto(copiloto_id: int, db: Session = Depends(get_db)):
    db_copiloto = crud.get_copiloto(db, copiloto_id=copiloto_id)
    if db_copiloto is None:
        raise HTTPException(status_code=404, detail="Copiloto not found")
    return db_copiloto

@app.put("/copilotos/{copiloto_id}", response_model=schemas.Copiloto)
def update_copiloto(copiloto_id: int, copiloto: schemas.CopilotoCreate, db: Session = Depends(get_db)):
    db_copiloto = crud.update_copiloto(db, copiloto_id=copiloto_id, copiloto=copiloto)
    if db_copiloto is None:
        raise HTTPException(status_code=404, detail="Copiloto not found")
    return db_copiloto

@app.delete("/copilotos/{copiloto_id}", response_model=schemas.Copiloto)
def delete_copiloto(copiloto_id: int, db: Session = Depends(get_db)):
    db_copiloto = crud.delete_copiloto(db, copiloto_id=copiloto_id)
    if db_copiloto is None:
        raise HTTPException(status_code=404, detail="Copiloto not found")
    return db_copiloto

# Sobrecargo
@app.post("/sobrecargos/", response_model=schemas.Sobrecargo)
def create_sobrecargo(sobrecargo: schemas.SobrecargoCreate, db: Session = Depends(get_db)):
    return crud.create_sobrecargo(db=db, sobrecargo=sobrecargo)

@app.get("/sobrecargos/", response_model=List[schemas.Sobrecargo])
def read_sobrecargos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sobrecargos = crud.get_sobrecargos(db, skip=skip, limit=limit)
    return sobrecargos

@app.get("/sobrecargos/{sobrecargo_id}", response_model=schemas.Sobrecargo)
def read_sobrecargo(sobrecargo_id: int, db: Session = Depends(get_db)):
    db_sobrecargo = crud.get_sobrecargo(db, sobrecargo_id=sobrecargo_id)
    if db_sobrecargo is None:
        raise HTTPException(status_code=404, detail="Sobrecargo not found")
    return db_sobrecargo

@app.put("/sobrecargos/{sobrecargo_id}", response_model=schemas.Sobrecargo)
def update_sobrecargo(sobrecargo_id: int, sobrecargo: schemas.SobrecargoCreate, db: Session = Depends(get_db)):
    db_sobrecargo = crud.update_sobrecargo(db, sobrecargo_id=sobrecargo_id, sobrecargo=sobrecargo)
    if db_sobrecargo is None:
        raise HTTPException(status_code=404, detail="Sobrecargo not found")
    return db_sobrecargo

@app.delete("/sobrecargos/{sobrecargo_id}", response_model=schemas.Sobrecargo)
def delete_sobrecargo(sobrecargo_id: int, db: Session = Depends(get_db)):
    db_sobrecargo = crud.delete_sobrecargo(db, sobrecargo_id=sobrecargo_id)
    if db_sobrecargo is None:
        raise HTTPException(status_code=404, detail="Sobrecargo not found")
    return db_sobrecargo

# Pasajero
@app.post("/pasajeros/", response_model=schemas.Pasajero)
def create_pasajero(pasajero: schemas.PasajeroCreate, db: Session = Depends(get_db)):
    return crud.create_pasajero(db=db, pasajero=pasajero)

@app.get("/pasajeros/", response_model=List[schemas.Pasajero])
def read_pasajeros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pasajeros = crud.get_pasajeros(db, skip=skip, limit=limit)
    return pasajeros

@app.get("/pasajeros/{pasajero_id}", response_model=schemas.Pasajero)
def read_pasajero(pasajero_id: int, db: Session = Depends(get_db)):
    db_pasajero = crud.get_pasajero(db, pasajero_id=pasajero_id)
    if db_pasajero is None:
        raise HTTPException(status_code=404, detail="Pasajero not found")
    return db_pasajero

@app.put("/pasajeros/{pasajero_id}", response_model=schemas.Pasajero)
def update_pasajero(pasajero_id: int, pasajero: schemas.PasajeroCreate, db: Session = Depends(get_db)):
    db_pasajero = crud.update_pasajero(db, pasajero_id=pasajero_id, pasajero=pasajero)
    if db_pasajero is None:
        raise HTTPException(status_code=404, detail="Pasajero not found")
    return db_pasajero

@app.delete("/pasajeros/{pasajero_id}", response_model=schemas.Pasajero)
def delete_pasajero(pasajero_id: int, db: Session = Depends(get_db)):
    db_pasajero = crud.delete_pasajero(db, pasajero_id=pasajero_id)
    if db_pasajero is None:
        raise HTTPException(status_code=404, detail="Pasajero not found")
    return db_pasajero

# Equipaje
@app.post("/equipajes/", response_model=schemas.Equipaje)
def create_equipaje(equipaje: schemas.EquipajeCreate, db: Session = Depends(get_db)):
    return crud.create_equipaje(db=db, equipaje=equipaje)

@app.get("/equipajes/", response_model=List[schemas.Equipaje])
def read_equipajes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    equipajes = crud.get_equipajes(db, skip=skip, limit=limit)
    return equipajes

@app.get("/equipajes/{equipaje_id}", response_model=schemas.Equipaje)
def read_equipaje(equipaje_id: int, db: Session = Depends(get_db)):
    db_equipaje = crud.get_equipaje(db, equipaje_id=equipaje_id)
    if db_equipaje is None:
        raise HTTPException(status_code=404, detail="Equipaje not found")
    return db_equipaje

@app.put("/equipajes/{equipaje_id}", response_model=schemas.Equipaje)
def update_equipaje(equipaje_id: int, equipaje: schemas.EquipajeCreate, db: Session = Depends(get_db)):
    db_equipaje = crud.update_equipaje(db, equipaje_id=equipaje_id, equipaje=equipaje)
    if db_equipaje is None:
        raise HTTPException(status_code=404, detail="Equipaje not found")
    return db_equipaje

@app.delete("/equipajes/{equipaje_id}", response_model=schemas.Equipaje)
def delete_equipaje(equipaje_id: int, db: Session = Depends(get_db)):
    db_equipaje = crud.delete_equipaje(db, equipaje_id=equipaje_id)
    if db_equipaje is None:
        raise HTTPException(status_code=404, detail="Equipaje not found")
    return db_equipaje

# Boleto
@app.post("/boletos/", response_model=schemas.Boleto)
def create_boleto(boleto: schemas.BoletoCreate, db: Session = Depends(get_db)):
    return crud.create_boleto(db=db, boleto=boleto)

@app.get("/boletos/", response_model=List[schemas.Boleto])
def read_boletos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    boletos = crud.get_boletos(db, skip=skip, limit=limit)
    return boletos

@app.get("/boletos/{boleto_id}", response_model=schemas.Boleto)
def read_boleto(boleto_id: int, db: Session = Depends(get_db)):
    db_boleto = crud.get_boleto(db, boleto_id=boleto_id)
    if db_boleto is None:
        raise HTTPException(status_code=404, detail="Boleto not found")
    return db_boleto

@app.put("/boletos/{boleto_id}", response_model=schemas.Boleto)
def update_boleto(boleto_id: int, boleto: schemas.BoletoCreate, db: Session = Depends(get_db)):
    db_boleto = crud.update_boleto(db, boleto_id=boleto_id, boleto=boleto)
    if db_boleto is None:
        raise HTTPException(status_code=404, detail="Boleto not found")
    return db_boleto

@app.delete("/boletos/{boleto_id}", response_model=schemas.Boleto)
def delete_boleto(boleto_id: int, db: Session = Depends(get_db)):
    db_boleto = crud.delete_boleto(db, boleto_id=boleto_id)
    if db_boleto is None:
        raise HTTPException(status_code=404, detail="Boleto not found")
    return db_boleto

#pasajeros por vuelo
# @router.get("/vuelos/{vuelo_id}/pasajeros", response_model=List[schemas.Pasajero])
# def read_pasajeros_by_vuelo(vuelo_id: int, db: Session = Depends(get_db)):
#     pasajeros = crud.get_pasajeros_by_vuelo(db, vuelo_id=vuelo_id)
#     if not pasajeros:
#         raise HTTPException(status_code=404, detail="No se encontraron pasajeros para este vuelo")
#     return pasajeros