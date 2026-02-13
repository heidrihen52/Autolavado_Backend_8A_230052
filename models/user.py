"""
Este modulo define el modelo User para la base de datos (tbb_usuarios).
"""
import sys
import os
# p
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=too-few-public-methods
# pylint: disable=wrong-import-position
from sqlalchemy import Column, Integer, String, ForeignKey
from config.db import Base


class User(Base):
    """
    Clase que representa la tabla tbb_usuarios en la base de datos.
    """
    __tablename__ = "tbb_usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(60), nullable=False)
    apellidoPaterno = Column(String(60), nullable=False)
    apellidoMaterno = Column(String(60), nullable=True)
    direccion = Column(String(256), nullable=True)
    telefono = Column(String(45), nullable=True)
    correo = Column(String(45), nullable=True)
    password = Column(String(256), nullable=False)
    rol_id = Column(Integer, ForeignKey("tbc_roles.id"))
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
