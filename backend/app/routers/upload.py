from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
import pandas as pd
from sqlalchemy.orm import Session
import os
from datetime import datetime
import re
from pathlib import Path

from app import models
from app.database import get_db

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

IMPORTACION_COLUMNS = [
    "Ordinal", "Fecha", "Documento", "Código SA", "País de Origen",
    "Importador", "RUC", "Dirección", "Localidad", "Proveedor",
    "Dirección.1", "Ciudad", "Aduana", "Transporte", "U$S CIF",
    "U$S Unitario", "Kgs. Brutos", "Cantidad", "Unidad", "Volúmen",
    "Unidad.1", "Descripción",
]

EXPORTACION_COLUMNS = [
    "Ordinal", "Fecha", "Documento", "Código SA", "País de Destino",
    "Exportador", "RUC", "Dirección", "Localidad", "Comprador",
    "Dirección.1", "Ciudad", "Aduana", "Transporte", "U$S FOB",
    "U$S Unitario", "Kgs. Brutos", "Cantidad", "Unidad", "Volúmen",
    "Unidad.1", "Descripción",
]


async def _save_file(upload: UploadFile) -> tuple[str, str]:
    # Sanitize original filename to avoid characters not supported on Windows
    original = Path(upload.filename).name
    safe_name = re.sub(r'[\\/*?:"<>|]', "_", original)
    filename = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{safe_name}"
    filepath = os.path.join(UPLOAD_DIR, filename)
    contents = await upload.read()
    with open(filepath, "wb") as f:
        f.write(contents)
    return filepath, filename


def _validate_columns(df: pd.DataFrame, columns: list):
    if not all(col in df.columns for col in columns):
        raise HTTPException(status_code=400, detail="Invalid columns in Excel file")


def _insert_importacion(df: pd.DataFrame, archivo_id: int, db: Session):
    for _, row in df.iterrows():
        item = models.Importacion(
            archivo_id=archivo_id,
            ordinal=row.get("Ordinal"),
            fecha=str(row.get("Fecha")),
            documento=row.get("Documento"),
            codigo_sa=row.get("Código SA"),
            pais_origen=row.get("País de Origen"),
            importador=row.get("Importador"),
            ruc=row.get("RUC"),
            direccion_importador=row.get("Dirección"),
            localidad=row.get("Localidad"),
            proveedor=row.get("Proveedor"),
            direccion_proveedor=row.get("Dirección.1"),
            ciudad=row.get("Ciudad"),
            aduana=row.get("Aduana"),
            transporte=row.get("Transporte"),
            usd_cif=row.get("U$S CIF"),
            usd_unitario=row.get("U$S Unitario"),
            kgs_brutos=row.get("Kgs. Brutos"),
            cantidad=row.get("Cantidad"),
            unidad_cantidad=row.get("Unidad"),
            volumen=row.get("Volúmen"),
            unidad_volumen=row.get("Unidad.1"),
            descripcion=row.get("Descripción"),
        )
        db.add(item)
    db.commit()


def _insert_exportacion(df: pd.DataFrame, archivo_id: int, db: Session):
    for _, row in df.iterrows():
        item = models.Exportacion(
            archivo_id=archivo_id,
            ordinal=row.get("Ordinal"),
            fecha=str(row.get("Fecha")),
            documento=row.get("Documento"),
            codigo_sa=row.get("Código SA"),
            pais_destino=row.get("País de Destino"),
            exportador=row.get("Exportador"),
            ruc=row.get("RUC"),
            direccion_exportador=row.get("Dirección"),
            localidad=row.get("Localidad"),
            comprador=row.get("Comprador"),
            direccion_comprador=row.get("Dirección.1"),
            ciudad=row.get("Ciudad"),
            aduana=row.get("Aduana"),
            transporte=row.get("Transporte"),
            usd_fob=row.get("U$S FOB"),
            usd_unitario=row.get("U$S Unitario"),
            kgs_brutos=row.get("Kgs. Brutos"),
            cantidad=row.get("Cantidad"),
            unidad_cantidad=row.get("Unidad"),
            volumen=row.get("Volúmen"),
            unidad_volumen=row.get("Unidad.1"),
            descripcion=row.get("Descripción"),
        )
        db.add(item)
    db.commit()


@router.post("/importacion")
async def upload_importacion(file: UploadFile = File(...), db: Session = Depends(get_db)):
    filepath, fname = await _save_file(file)
    df = pd.read_excel(filepath, engine="openpyxl")
    _validate_columns(df, IMPORTACION_COLUMNS)
    archivo = models.Archivo(filename=fname, tipo="importacion", path=filepath)
    db.add(archivo)
    db.commit()
    db.refresh(archivo)
    _insert_importacion(df, archivo.id, db)
    return {"rows": len(df)}


@router.post("/exportacion")
async def upload_exportacion(file: UploadFile = File(...), db: Session = Depends(get_db)):
    filepath, fname = await _save_file(file)
    df = pd.read_excel(filepath, engine="openpyxl")
    _validate_columns(df, EXPORTACION_COLUMNS)
    archivo = models.Archivo(filename=fname, tipo="exportacion", path=filepath)
    db.add(archivo)
    db.commit()
    db.refresh(archivo)
    _insert_exportacion(df, archivo.id, db)
    return {"rows": len(df)}

