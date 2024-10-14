from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Aeropuerto(Base):
    __tablename__ = "aeropuertos"

    idAeropuerto = Column(Integer, primary_key=True, index=True)
    nombreAeropuerto = Column(String, index=True)
    numPistas = Column(Integer)
    tipoAvion = Column(String)

    terminales = relationship("Terminal", back_populates="aeropuerto")

class Terminal(Base):
    __tablename__ = "terminales"

    idTerminal = Column(Integer, primary_key=True, index=True)
    capacidad = Column(Integer)
    disponible = Column(Boolean)
    idAeropuerto = Column(Integer, ForeignKey("aeropuertos.idAeropuerto"))

    aeropuerto = relationship("Aeropuerto", back_populates="terminales")
    vuelos = relationship("Vuelo", back_populates="terminal")

class Vuelo(Base):
    __tablename__ = "vuelos"

    idVuelo = Column(Integer, primary_key=True, index=True)
    origen = Column(String)
    destino = Column(String)
    duracion = Column(Float)
    horaSalida = Column(DateTime)
    horaLlegada = Column(DateTime)
    idTerminal = Column(Integer, ForeignKey("terminales.idTerminal"))
    idVehiculoAereo = Column(Integer, ForeignKey("vehiculos_aereos.idVehiculoAereo"))

    terminal = relationship("Terminal", back_populates="vuelos")
    vehiculoAereo = relationship("VehiculoAereo", back_populates="vuelos")
    tripulaciones = relationship("Tripulacion", back_populates="vuelo")
    boletos = relationship("Boleto", back_populates="vuelo")

class VehiculoAereo(Base):
    __tablename__ = "vehiculos_aereos"

    idVehiculoAereo = Column(Integer, primary_key=True, index=True)
    matricula = Column(String, index=True)
    serie = Column(String)
    capacidad = Column(Integer)
    color = Column(String)
    estado = Column(Boolean)
    antiguedad = Column(Integer)
    tiempoAire = Column(Float)
    llantas = Column(Integer)
    tanque = Column(Float)
    distancia = Column(Float)

    vuelos = relationship("Vuelo", back_populates="vehiculoAereo")

class Avion(VehiculoAereo):
    __tablename__ = "aviones"

    idAvion = Column(Integer, ForeignKey("vehiculos_aereos.idVehiculoAereo"), primary_key=True)
    aerolinea = Column(String)
    tipoMotor = Column(String)
    puertas = Column(Integer)
    tipoAvion = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "avion",
    }

class Avioneta(VehiculoAereo):
    __tablename__ = "avionetas"

    idAvioneta = Column(Integer, ForeignKey("vehiculos_aereos.idVehiculoAereo"), primary_key=True)
    numeroMotores = Column(Integer)
    tipoPista = Column(String)
    clasificacion = Column(String)
    tipoConcesion = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "avioneta",
    }

class Helicoptero(VehiculoAereo):
    __tablename__ = "helicopteros"

    idHelicoptero = Column(Integer, ForeignKey("vehiculos_aereos.idVehiculoAereo"), primary_key=True)
    numeroHelices = Column(Integer)
    tipoHelicoptero = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "helicoptero",
    }

class Tripulacion(Base):
    __tablename__ = "tripulaciones"

    idTripulacion = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    direccion = Column(String)
    apellido = Column(String)
    fecha_nac = Column(DateTime)
    discapacidad = Column(Boolean)
    antiguedad = Column(Integer)
    turno = Column(String)
    horasVuelo = Column(Float)
    genero = Column(String)
    idVuelo = Column(Integer, ForeignKey("vuelos.idVuelo"))

    vuelo = relationship("Vuelo", back_populates="tripulaciones")

class Piloto(Tripulacion):
    __tablename__ = "pilotos"

    idPiloto = Column(Integer, ForeignKey("tripulaciones.idTripulacion"), primary_key=True)
    rango = Column(String)
    licencia = Column(String)
    tipoAeronave = Column(String)
    saludMental = Column(Boolean)

    __mapper_args__ = {
        "polymorphic_identity": "piloto",
    }

class Copiloto(Tripulacion):
    __tablename__ = "copilotos"

    idCopiloto = Column(Integer, ForeignKey("tripulaciones.idTripulacion"), primary_key=True)
    rango = Column(String)
    tiempoRestantePiloto = Column(Float)

    __mapper_args__ = {
        "polymorphic_identity": "copiloto",
    }

class Sobrecargo(Tripulacion):
    __tablename__ = "sobrecargos"

    idSobrecargo = Column(Integer, ForeignKey("tripulaciones.idTripulacion"), primary_key=True)
    idiomas = Column(String)
    certificados = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "sobrecargo",
    }

class Pasajero(Base):
    __tablename__ = "pasajeros"

    idPasajero = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    direccion = Column(String)
    apellido = Column(String)
    fecha_nac = Column(DateTime)
    discapacidad = Column(Boolean)
    nacionalidad = Column(String)

    equipajes = relationship("Equipaje", back_populates="pasajero")
    boletos = relationship("Boleto", back_populates="pasajero")

class Equipaje(Base):
    __tablename__ = "equipajes"

    idEquipaje = Column(Integer, primary_key=True, index=True)
    peso = Column(Float)
    altura = Column(Float)
    tipo = Column(String)
    idPasajero = Column(Integer, ForeignKey("pasajeros.idPasajero"))

    pasajero = relationship("Pasajero", back_populates="equipajes")

class Boleto(Base):
    __tablename__ = "boletos"

    idBoleto = Column(Integer, primary_key=True, index=True)
    asiento = Column(String)
    costo = Column(Float)
    idPasajero = Column(Integer, ForeignKey("pasajeros.idPasajero"))
    idVuelo = Column(Integer, ForeignKey("vuelos.idVuelo"))

    pasajero = relationship("Pasajero", back_populates="boletos")
    vuelo = relationship("Vuelo", back_populates="boletos")