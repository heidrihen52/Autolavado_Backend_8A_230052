"""
Este modulo contiene las funciones CRUD para la tabla tbb_usuarios.
"""
import sys
import os
from sqlalchemy.orm import Session

# Add the parent directory to sys.path to allow imports from config and models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=wrong-import-position
import models.user

def get_usuarios(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene lista de usuarios con paginacion.
    """
    return db.query(models.user.User).offset(skip).limit(limit).all()
