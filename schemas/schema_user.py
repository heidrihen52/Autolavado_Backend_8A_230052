"""
Este modulo define el esquema User para la base de datos (tbb_usuarios).
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    '''clase base para el modelo User'''
    nombre: str
    apellidoPaterno: str
    apellidoMaterno: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    password: str
    rol_id: int
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

class UserCreate(UserBase):
    '''clase para crear un usuario'''
    pass

class UserUpdate(UserBase):
    '''clase para actualizar un usuario'''
    pass

class UserResponse(UserBase):
    '''clase para mostrar un usuario'''
    id: int
    class Config:
        '''utilizar el orm para ejecutar funcionalidades'''
        orm_mode = True
