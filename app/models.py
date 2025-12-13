from sqlalchemy import Column, Integer, String
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    telefono = Column(String, nullable=False)
    contrasena = Column(String, nullable=False)
    calle = Column(String)
    numero = Column(String)
    colonia = Column(String)
    ciudad = Column(String)
