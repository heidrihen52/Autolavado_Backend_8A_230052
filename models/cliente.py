"""
Este modulo define el modelo Cliente para la base de datos (c_cliente).
"""
import sys
import os
# p
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=too-few-public-methods
# pylint: disable=wrong-import-position
from sqlalchemy import Column, Integer, String
from config.db import Base


class Cliente(Base):
    """
    Clase que representa la tabla c_cliente en la base de datos.
    """
    __tablename__ = "c_cliente"

    cl_id = Column(Integer, primary_key=True, index=True)
    cl_nombre = Column(String(60), nullable=False)
    cl_apellidoPaterno = Column(String(60), nullable=False)
    cl_apellidoMaterno = Column(String(60), nullable=True)
    cl_direccion = Column(String(255), nullable=True)
    cl_email = Column(String(55), nullable=True)
    cl_telefono = Column(String(15), nullable=True)
    cl_password = Column(String(750), nullable=False)
