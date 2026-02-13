"""
Este modulo define el modelo Rol para la base de datos (c_rol).
"""
import sys
import os
# p
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=too-few-public-methods
# pylint: disable=wrong-import-position
from sqlalchemy import Column, Integer, String
from config.db import Base


class Rol(Base):
    """
    Clase que representa la tabla tbc_roles en la base de datos.
    """
    __tablename__ = "tbc_roles"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(45), nullable=False)
    estado = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
