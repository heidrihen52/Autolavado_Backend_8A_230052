"""
Este modulo define el esquema Auto para la base de datos (tbb_vehiculos).
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class AutoBase(BaseModel):
    '''clase base para el modelo Auto'''
    modelo: str
    placa: str
    serie: Optional[str] = None
    color: Optional[str] = None
    tipo: Optional[str] = None
    anio: Optional[int] = None
    estatus: Optional[bool] = None
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None
    vehiculo_id: int

class AutoCreate(AutoBase):
    '''clase para crear un auto'''
    pass

class AutoUpdate(AutoBase):
    '''clase para actualizar un auto'''
    pass

class AutoResponse(AutoBase):
    '''clase para mostrar un auto'''
    id: int
    class Config:
        '''utilizar el orm para ejecutar funcionalidades'''
        orm_mode = True
