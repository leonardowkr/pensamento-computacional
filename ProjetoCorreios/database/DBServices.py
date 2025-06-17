from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database.models import LinhaTransporte, Base

class DBservices():
    def __init__(self):
        
        # Conectar ao banco
        engine = create_engine('sqlite:///teste1.db')
        Base.metadata.create_all(engine)    

        # Criar uma sessão
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def criar_linha_transporte (self, origem = str, destino = str, 
                                distancia = float, peso = float, 
                                tarifa_km = float, tipo_transporte = str, custo = float) -> LinhaTransporte:

        # Criar novo usuário
        novo_usuario = LinhaTransporte(origem = origem, destino = destino, 
                                distancia = distancia, peso = peso, 
                                tarifa_km = tarifa_km, tipo_transporte = tipo_transporte, custo = custo)

        # Adicionar à sessão
        self.session.add(novo_usuario)

        # Salvar no banco
        self.session.commit()
        return novo_usuario

    def buscar_todas_linhas_transportes(self) -> list [LinhaTransporte]:
        try:
            usuarios = self.session.query(LinhaTransporte).all()
        except Exception as e:
            print(e)
            usuarios = []
        return usuarios

    def buscar_usuarios_por_origem(self, origem: str) -> list [LinhaTransporte]:
        try:
            usuarios = self.session.query(LinhaTransporte).filter_by(origem = origem).all()
        except Exception as e:
            print(e)
            usuarios = []
        return usuarios