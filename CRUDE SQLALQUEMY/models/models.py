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


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base para nossos modelos
Base = declarative_base()
class Usuario(Base):
    """
        Classe que representa a tabela 'usuarios' no banco de dados.
        Atributos: 
            id (int): ID do usuário (chave primária)
            nome (str): Nome do usuário (tamanho máximo de 50 caractéres)
            idade (int): Idade do usuário
    """


    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer)
def __repr__(self):
    return f"<Usuario(nome='{self.nome}', idade={self.idade})>"