'''
Esta clase permitegenerar el modelo para los tipos de rol
'''
from sqlalchemy import column, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base


class Rol(Base):
    '''
    Esta clase permite generar el modelo para los tipos de rol
    '''
    __tablename__ = "tbc_rol"
    IdRol = column(Integer, primary_key=True, index=True)
    nombreRol = column(String(15), nullable=False)
    estatus = column(Boolea)

    
    
