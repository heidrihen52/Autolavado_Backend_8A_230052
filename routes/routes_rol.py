from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud.crud.rol, config.db, schemas.schema_rol, models.model_rol

router = APIRouter()


