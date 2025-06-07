from pydantic import BaseModel
from typing import Optional

class ArchivoOut(BaseModel):
    id: int
    filename: str
    tipo: str
    uploaded_at: str

    class Config:
        orm_mode = True

class ImportacionOut(BaseModel):
    id: int
    ordinal: Optional[int] = None
    fecha: Optional[str] = None
    documento: Optional[str] = None
    codigo_sa: Optional[str] = None
    pais_origen: Optional[str] = None
    importador: Optional[str] = None
    ruc: Optional[str] = None
    direccion_importador: Optional[str] = None
    localidad: Optional[str] = None
    proveedor: Optional[str] = None
    direccion_proveedor: Optional[str] = None
    ciudad: Optional[str] = None
    aduana: Optional[str] = None
    transporte: Optional[str] = None
    usd_cif: Optional[float] = None
    usd_unitario: Optional[float] = None
    kgs_brutos: Optional[float] = None
    cantidad: Optional[float] = None
    unidad_cantidad: Optional[str] = None
    volumen: Optional[float] = None
    unidad_volumen: Optional[str] = None
    descripcion: Optional[str] = None

    class Config:
        orm_mode = True

class ExportacionOut(BaseModel):
    id: int
    ordinal: Optional[int] = None
    fecha: Optional[str] = None
    documento: Optional[str] = None
    codigo_sa: Optional[str] = None
    pais_destino: Optional[str] = None
    exportador: Optional[str] = None
    ruc: Optional[str] = None
    direccion_exportador: Optional[str] = None
    localidad: Optional[str] = None
    comprador: Optional[str] = None
    direccion_comprador: Optional[str] = None
    ciudad: Optional[str] = None
    aduana: Optional[str] = None
    transporte: Optional[str] = None
    usd_fob: Optional[float] = None
    usd_unitario: Optional[float] = None
    kgs_brutos: Optional[float] = None
    cantidad: Optional[float] = None
    unidad_cantidad: Optional[str] = None
    volumen: Optional[float] = None
    unidad_volumen: Optional[str] = None
    descripcion: Optional[str] = None

    class Config:
        orm_mode = True
