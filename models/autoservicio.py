"""
Este modulo define el modelo Autoservicio para la base de datos (r_auto_servicio).
"""
import sys
import os
# p
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=too-few-public-methods
# pylint: disable=wrong-import-position
from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, Float, Time
from sqlalchemy.sql import func
from config.db import Base


class Autoservicio(Base):
    """
    Clase que representa la tabla r_auto_servicio en la base de datos.
    """
    __tablename__ = "r_auto_servicio"

    as_id = Column(Integer, primary_key=True, index=True)
    au_id = Column(Integer, ForeignKey("c_auto.au_id"))
    se_id = Column(Integer, ForeignKey("c_servicio.se_id"))
    us_id = Column(Integer, ForeignKey("c_usuario.us_id"))
    as_fecha = Column(DateTime, default=func.now())  # pylint: disable=not-callable
    as_pagado = Column(Boolean, default=False, nullable=False)
    as_monto = Column(Float, nullable=False)
    as_aprobado = Column(Boolean, default=False, nullable=False)
    as_hora = Column(Time, default=func.now())  # pylint: disable=not-callable
