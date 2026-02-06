"""
Este modulo define el modelo User para la base de datos (c_usuario).
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
    Clase que representa la tabla c_usuario en la base de datos.
    """
    __tablename__ = "c_usuario"

    us_id = Column(Integer, primary_key=True, index=True)
    us_nombre = Column(String(60), nullable=False)
    us_apellidoPaterno = Column(String(60), nullable=False)
    us_apellidoMaterno = Column(String(60), nullable=True)
    us_usuario = Column(String(60), nullable=False)
    us_password = Column(String(256), nullable=False)
    ro_id = Column(Integer, ForeignKey("c_rol.ro_id"))
