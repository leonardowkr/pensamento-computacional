import sqlite3
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# conn = sqlite3.connect("teste.db")

# # Para fazer as operações no banco
# cursor = conn.cursor()

# #cursor.execute("CREATE TABLE linhaTransporte (id INTEGER PRIMARY KEY, origem TEXT NOT NULL, destino TEXT NOT NULL, distancia REAL)")

# #cursor.execute("INSERT INTO linhatransporte VALUES('1', 'SP', 'RS', '1500')")
# cursor.execute("SELECT * FROM linhatransporte")

# conn.commit()

# print(cursor.fetchall())

db = create_engine("sqlite:///linhatransporte.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

Base.metadata.create_all(bind=db)

class LinhaTransporte(Base):
    __tablename__ = "linhastransportes"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    origem = Column("origem", String)
    destino = Column("destino", String)
    distancia = Column("distancia", Float)
    peso_cubagem = Column("peso", Float)
    tarifa_km = Column("tarifa_km", Float)
    custo = Column("custo", Float)
    
