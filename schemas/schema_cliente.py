"""
Este modulo define el esquema Cliente para la base de datos (c_cliente).
"""

from typing import Optional
from pydantic import BaseModel

class ClienteBase(BaseModel):
    '''clase base para el modelo Cliente'''
    cl_nombre: str
    cl_apellidoPaterno: str
    cl_apellidoMaterno: Optional[str] = None
    cl_direccion: Optional[str] = None
    cl_email: Optional[str] = None
    cl_telefono: Optional[str] = None
    cl_password: str

class ClienteCreate(ClienteBase):
    '''clase para crear un cliente'''
    pass

class ClienteUpdate(ClienteBase):
    '''clase para actualizar un cliente'''
    pass

class ClienteResponse(ClienteBase):
    '''clase para mostrar un cliente'''
    cl_id: int
    class Config:
        '''utilizar el orm para ejecutar funcionalidades'''
        orm_mode = True
