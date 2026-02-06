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
    Clase que representa la tabla c_rol en la base de datos.
    """
    __tablename__ = "c_rol"

    ro_id = Column(Integer, primary_key=True, index=True)
    ro_nombre = Column(String(45), nullable=False)
