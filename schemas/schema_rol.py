"""
Este modulo define el esquema Rol para la base de datos (c_rol).
"""

from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):
    '''clase base para el modelo Rol'''
    nombre:str
    estado:bool
    fecha_registro:datetime
    fecha_actualizacion:datetime

class RolCreate(RolBase):
    '''clase para crear un rol'''
    pass

class RolUpdate(RolBase):
    '''clase para actualizar un rol'''
    pass

class RolResponse(RolBase):
    '''clase para mostrar un rol'''
    id:int
    class Config:
        '''utilizar el orm para ejecutar funcionalidades'''
        orm_mode=True

    
    