from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base

class Archivo(Base):
    __tablename__ = "archivos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    filename = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    path = Column(String, nullable=False)

    importaciones = relationship("Importacion", back_populates="archivo", cascade="all, delete-orphan")
    exportaciones = relationship("Exportacion", back_populates="archivo", cascade="all, delete-orphan")


class Importacion(Base):
    __tablename__ = "importaciones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    archivo_id = Column(Integer, ForeignKey("archivos.id"))
    ordinal = Column(Integer)
    fecha = Column(String)
    documento = Column(String)
    codigo_sa = Column(String)
    pais_origen = Column(String)
    importador = Column(String)
    ruc = Column(String)
    direccion_importador = Column(String)
    localidad = Column(String)
    proveedor = Column(String)
    direccion_proveedor = Column(String)
    ciudad = Column(String)
    aduana = Column(String)
    transporte = Column(String)
    usd_cif = Column(Float)
    usd_unitario = Column(Float)
    kgs_brutos = Column(Float)
    cantidad = Column(Float)
    unidad_cantidad = Column(String)
    volumen = Column(Float)
    unidad_volumen = Column(String)
    descripcion = Column(String)

    archivo = relationship("Archivo", back_populates="importaciones")

class Exportacion(Base):
    __tablename__ = "exportaciones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    archivo_id = Column(Integer, ForeignKey("archivos.id"))
    ordinal = Column(Integer)
    fecha = Column(String)
    documento = Column(String)
    codigo_sa = Column(String)
    pais_destino = Column(String)
    exportador = Column(String)
    ruc = Column(String)
    direccion_exportador = Column(String)
    localidad = Column(String)
    comprador = Column(String)
    direccion_comprador = Column(String)
    ciudad = Column(String)
    aduana = Column(String)
    transporte = Column(String)
    usd_fob = Column(Float)
    usd_unitario = Column(Float)
    kgs_brutos = Column(Float)
    cantidad = Column(Float)
    unidad_cantidad = Column(String)
    volumen = Column(Float)
    unidad_volumen = Column(String)
    descripcion = Column(String)

    archivo = relationship("Archivo", back_populates="exportaciones")
