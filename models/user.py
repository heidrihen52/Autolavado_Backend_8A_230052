from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base


class User(Base):
    '''
    Esta clase permite generar el modelo para los usuarios
    '''
    __tablename__ = "tbb_usuario"
    Id=Column(Integer, primary_key=True, index=True)
    Rol_Id = Column(Integer, ForeignKey("tbc_roles.Id"))
    nombreUsuario = Column(String(15), nullable=False)
    password = Column(String(15), nullable=False)
    estatus = Column(Boolean, nullable=False)
    IdRol = Column(Integer, nullable=False)
    