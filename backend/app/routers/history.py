from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import os

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/history", tags=["History"])

@router.get("/", response_model=List[schemas.ArchivoOut])
def list_history(db: Session = Depends(get_db)):
    return db.query(models.Archivo).all()

@router.delete("/{archivo_id}")
def delete_archivo(archivo_id: int, db: Session = Depends(get_db)):
    archivo = db.query(models.Archivo).get(archivo_id)
    if not archivo:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    if os.path.exists(archivo.path):
        os.remove(archivo.path)
    db.delete(archivo)
    db.commit()
    return {"ok": True}
