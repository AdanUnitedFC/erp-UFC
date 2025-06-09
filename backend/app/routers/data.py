from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/data", tags=["Data"])

@router.get("/importaciones", response_model=List[schemas.ImportacionOut])
def list_importaciones(db: Session = Depends(get_db)):
    return db.query(models.Importacion).all()

@router.get("/exportaciones", response_model=List[schemas.ExportacionOut])
def list_exportaciones(db: Session = Depends(get_db)):
    return db.query(models.Exportacion).all()
