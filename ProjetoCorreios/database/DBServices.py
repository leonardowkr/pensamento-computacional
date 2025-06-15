from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database.models import Usuario, Base

class DBservices():
    def __init__(self):
        
        # Conectar ao banco
        engine = create_engine('sqlite:///exemplo.db')
        Base.metadata.create_all(engine)    

        # Criar uma sessão
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def criar_usuario (self, nome = str, idade= int) -> Usuario:

        # Criar novo usuário
        novo_usuario = Usuario(nome=nome, idade=idade)

        # Adicionar à sessão
        self.session.add(novo_usuario)

        # Salvar no banco
        self.session.commit()
        return novo_usuario

    def buscar_todos_usuarios(self) -> list [Usuario]:
        try:
            usuarios = self.session.query(Usuario).all()
        except Exception as e:
            print(e)
            usuarios = []
        return usuarios

    def buscar_usuarios_por_nome(self, nome: str) -> list [Usuario]:
        try:
            usuarios = self.session.query(Usuario).filter_by(nome = nome).all()
        except Exception as e:
            print(e)
            usuarios = []
        return usuarios