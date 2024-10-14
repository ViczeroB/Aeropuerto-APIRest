from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Aeropuerto
class AeropuertoBase(BaseModel):
    nombreAeropuerto: str
    numPistas: int
    tipoAvion: str

class AeropuertoCreate(AeropuertoBase):
    pass

class Aeropuerto(AeropuertoBase):
    idAeropuerto: int

    class Config:
        from_attributes = True

# Terminal
class TerminalBase(BaseModel):
    capacidad: int
    disponible: bool
    idAeropuerto: int

class TerminalCreate(TerminalBase):
    pass

class Terminal(TerminalBase):
    idTerminal: int

    class Config:
        from_attributes = True

# Vuelo
class VueloBase(BaseModel):
    origen: str
    destino: str
    duracion: float
    horaSalida: datetime
    horaLlegada: datetime
    idTerminal: int
    idVehiculoAereo: int

class VueloCreate(VueloBase):
    pass

class Vuelo(VueloBase):
    idVuelo: int

    class Config:
        from_attributes = True

# VehiculoAereo
class VehiculoAereoBase(BaseModel):
    matricula: str
    serie: str
    capacidad: int
    color: str
    estado: bool
    antiguedad: int
    tiempoAire: float
    llantas: int
    tanque: float
    distancia: float

class VehiculoAereoCreate(VehiculoAereoBase):
    pass

class VehiculoAereo(VehiculoAereoBase):
    idVehiculoAereo: int

    class Config:
        from_attributes = True

# Avion
class AvionBase(VehiculoAereoBase):
    aerolinea: str
    tipoMotor: str
    puertas: int
    tipoAvion: str

class AvionCreate(AvionBase):
    pass

class Avion(AvionBase):
    idAvion: int

    class Config:
        from_attributes = True

# Avioneta
class AvionetaBase(VehiculoAereoBase):
    numeroMotores: int
    tipoPista: str
    clasificacion: str
    tipoConcesion: str

class AvionetaCreate(AvionetaBase):
    pass

class Avioneta(AvionetaBase):
    idAvioneta: int

    class Config:
        from_attributes = True

# Helicoptero
class HelicopteroBase(VehiculoAereoBase):
    numeroHelices: int
    tipoHelicoptero: str

class HelicopteroCreate(HelicopteroBase):
    pass

class Helicoptero(HelicopteroBase):
    idHelicoptero: int

    class Config:
        from_attributes = True

# Tripulacion
class TripulacionBase(BaseModel):
    nombre: str
    direccion: str
    apellido: str
    fecha_nac: datetime
    discapacidad: bool
    antiguedad: int
    turno: str
    horasVuelo: float
    genero: str
    idVuelo: int

class TripulacionCreate(TripulacionBase):
    pass

class Tripulacion(TripulacionBase):
    idTripulacion: int

    class Config:
        from_attributes = True

# Piloto
class PilotoBase(TripulacionBase):
    rango: str
    licencia: str
    tipoAeronave: str
    saludMental: bool

class PilotoCreate(PilotoBase):
    pass

class Piloto(PilotoBase):
    idPiloto: int

    class Config:
        from_attributes = True

# Copiloto
class CopilotoBase(TripulacionBase):
    rango: str
    tiempoRestantePiloto: float

class CopilotoCreate(CopilotoBase):
    pass

class Copiloto(CopilotoBase):
    idCopiloto: int

    class Config:
        from_attributes = True

# Sobrecargo
class SobrecargoBase(TripulacionBase):
    idiomas: str
    certificados: str

class SobrecargoCreate(SobrecargoBase):
    pass

class Sobrecargo(SobrecargoBase):
    idSobrecargo: int

    class Config:
        from_attributes = True

# Pasajero
class PasajeroBase(BaseModel):
    nombre: str
    direccion: str
    apellido: str
    fecha_nac: datetime
    discapacidad: bool
    nacionalidad: str

class PasajeroCreate(PasajeroBase):
    pass

class Pasajero(PasajeroBase):
    idPasajero: int

    class Config:
        from_attributes = True

# Equipaje
class EquipajeBase(BaseModel):
    peso: float
    altura: float
    tipo: str
    idPasajero: int

class EquipajeCreate(EquipajeBase):
    pass

class Equipaje(EquipajeBase):
    idEquipaje: int

    class Config:
        from_attributes = True

# Boleto
class BoletoBase(BaseModel):
    asiento: str
    costo: float
    idPasajero: int
    idVuelo: int

class BoletoCreate(BoletoBase):
    pass

class Boleto(BoletoBase):
    idBoleto: int

    class Config:
        from_attributes = True