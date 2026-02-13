"""
Este modulo define el esquema VehiculoServicio para la base de datos (tbc_vehiculos_servicios_usuarios).
"""

from typing import Optional
from datetime import datetime, date, time
from enum import Enum
from pydantic import BaseModel

class Estatus(str, Enum):
    '''Enum para el estatus del servicio'''
    Programado = "Programado"
    Proceso = "En Proceso"
    Realizado = "Realizado"

class VehiculoServicioBase(BaseModel):
    '''clase base para el modelo VehiculoServicio'''
    vehiculo_id: int
    cajero_id: int
    operador_id: int
    servicio_id: int
    fecha: Optional[date] = None
    hora: Optional[time] = None
    estatus: Estatus = Estatus.Programado
    estado: Optional[bool] = None
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

class VehiculoServicioCreate(VehiculoServicioBase):
    '''clase para crear un vehiculo_servicio'''
    pass

class VehiculoServicioUpdate(VehiculoServicioBase):
    '''clase para actualizar un vehiculo_servicio'''
    pass

class VehiculoServicioResponse(VehiculoServicioBase):
    '''clase para mostrar un vehiculo_servicio'''
    id: int
    class Config:
        '''utilizar el orm para ejecutar funcionalidades'''
        orm_mode = True
