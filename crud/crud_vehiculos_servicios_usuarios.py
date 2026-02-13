"""
Este modulo contiene las funciones CRUD para la tabla tbc_vehiculos_servicios_usuarios.
"""
import sys
import os
from sqlalchemy.orm import Session

# Add the parent directory to sys.path to allow imports from config and models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=wrong-import-position
import models.auto_servicio_usuario

def get_vehiculos_servicios_usuarios(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene lista de vehiculos_servicios_usuarios con paginacion.
    """
    return db.query(
        models.auto_servicio_usuario.VehiculoServicio
    ).offset(skip).limit(limit).all()
