"""
    Sistema de Cadastro de Usuários
    IENH - 2025/1
    Aluno/autor: Leonardo Nunes Wecker

    Arquivo que contém as classes que representam os modelos do banco de dados.

    Classes: Classe que representa a tabela 'usuarios' no banco de dados
        Usuario: Classe que representa a tabela 'usuarios' no banco de daddos
    """

"""
    
"""

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# Base para nossos modelos
Base = declarative_base()
class LinhaTransporte(Base):
    """
        Classe que representa a tabela 'usuarios' no banco de dados.
        Atributos: 
            id (int): ID da linha de transporte (chave primária)
            origem (str): Dá onde está saindo (tamanho máximo de 50 caractéres)
            destino (str): Para onde vai (tamanho máximo de 50 caractéres)
            distancia (float): Distancia entre origem e destino
            peso (float): Peso da mercadoria transportada
            tarifa por km (float): tarifa cobrada por km rodado
            tipo transporte (str): tipo de transporte utilizado
    """

    __tablename__ = 'linhatransportes'
    id = Column(Integer, primary_key=True)
    origem = Column(String(50), nullable=False)
    destino = Column(String(50), nullable=False)
    distancia = Column(Float, nullable=False)
    peso = Column(Float, nullable=False)
    tarifa_km = Column(Float, nullable=False)
    tipo_transporte = Column(String(30), nullable=False)
    custo = Column(Float, nullable=False)

def __repr__(self):
    return f"<LinhaTransporte(origem='{self.origem}', destino={self.destino}, distancia={self.distancia}, peso={self.peso}, tarifa_km={self.tarifa_km}, tipo_transporte={self.tipo_transporte})>"