"""
Este modulo define el modelo Auto para la base de datos (tbb_vehiculos).
"""
import sys
import os
# p
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=too-few-public-methods
# pylint: disable=wrong-import-position
from sqlalchemy import Column, Integer, String, ForeignKey
from config.db import Base


class Auto(Base):
    """
    Clase que representa la tabla tbb_vehiculos en la base de datos.
    """
    __tablename__ = "tbb_vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String(45), nullable=False)
    placa = Column(String(45), nullable=False, unique=True)
    serie = Column(String(45), nullable=True)
    color = Column(String(45), nullable=True)
    tipo = Column(String(45), nullable=True)
    anio = Column(Integer, nullable=True)
    estatus = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
    vehiculo_id = Column(Integer, ForeignKey("tbb_usuarios.id"))
