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

class Estatus(enum.Enum):
    Programado = "Programado"
    Proceso = "En Proceso"
    Realizado = "Realizado"

class VehiculoServicio(Base):
    __tablename__ = "tbc_vehiculos_servicios_usuarios"

    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("tbb_vehiculos.id"))
    cajero_id = Column(Integer, ForeignKey("tbb_usuarios.id"))
    operador_id = Column(Integer, ForeignKey("tbb_usuarios.id"))
    servicio_id = Column(Integer, ForeignKey("tbc_servicios.id"))
    #usuario_id = Column(Integer, ForeignKey("tbb_usuarios.id"))
    fecha = Column(Date)
    hora = Column(Time)
    estatus = Column(Enum(Estatus),default=Estatus.Programado)
    estado = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
