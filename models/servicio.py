"""
Este modulo define el modelo Servicio para la base de datos (c_servicio).
"""
import sys
import os
# p
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=too-few-public-methods
# pylint: disable=wrong-import-position
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from config.db import Base


class Servicio(Base):
    """
    Clase que representa la tabla c_servicio en la base de datos.
    """
    __tablename__ = "c_servicio"

    se_id = Column(Integer, primary_key=True, index=True)
    se_nombre = Column(String(80), nullable=False)
    se_descripcion = Column(String(850), nullable=True)
    se_precio = Column(Float, nullable=False)
    se_estatus = Column(String(45), nullable=False)
    us_id = Column(Integer, ForeignKey("c_usuario.us_id"))
