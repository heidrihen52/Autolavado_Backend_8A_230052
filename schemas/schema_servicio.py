"""
Este modulo define el esquema Servicio para la base de datos (tbc_servicios).
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class ServicioBase(BaseModel):
    '''clase base para el modelo Servicio'''
    se_nombre: str
    se_descripcion: Optional[str] = None
    se_precio: float
    se_duracion: Optional[int] = None
    se_estatus: str
    us_id: Optional[int] = None
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

class ServicioCreate(ServicioBase):
    '''clase para crear un servicio'''
    pass

class ServicioUpdate(ServicioBase):
    '''clase para actualizar un servicio'''
    pass

class ServicioResponse(ServicioBase):
    '''clase para mostrar un servicio'''
    se_id: int
    class Config:
        '''utilizar el orm para ejecutar funcionalidades'''
        orm_mode = True
