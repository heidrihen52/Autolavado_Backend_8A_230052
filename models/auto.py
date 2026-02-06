"""
Este modulo define el modelo Auto para la base de datos (c_auto).
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
    Clase que representa la tabla c_auto en la base de datos.
    """
    __tablename__ = "c_auto"

    au_id = Column(Integer, primary_key=True, index=True)
    au_modelo = Column(String(45), nullable=False)
    au_matricula = Column(String(45), nullable=False, unique=True)
    au_color = Column(String(45), nullable=True)
    au_Tipo = Column(String(45), nullable=True)
    cl_id = Column(Integer, ForeignKey("c_cliente.cl_id"))
