"""
Este modulo define el esquema Autoservicio para la base de datos (r_auto_servicio).
"""

from typing import Optional
from datetime import datetime, time
from pydantic import BaseModel

class AutoservicioBase(BaseModel):
    '''clase base para el modelo Autoservicio'''
    au_id: int
    se_id: int
    us_id: int
    as_fecha: Optional[datetime] = None
    as_pagado: bool = False
    as_monto: float
    as_aprobado: bool = False
    as_hora: Optional[time] = None

class AutoservicioCreate(AutoservicioBase):
    '''clase para crear un autoservicio'''
    pass

class AutoservicioUpdate(AutoservicioBase):
    '''clase para actualizar un autoservicio'''
    pass

class AutoservicioResponse(AutoservicioBase):
    '''clase para mostrar un autoservicio'''
    as_id: int
    class Config:
        '''utilizar el orm para ejecutar funcionalidades'''
        orm_mode = True
