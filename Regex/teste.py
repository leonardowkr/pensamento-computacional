import re

def validar_email(email):
    # Regex para validar o formato do email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    emails = ['usuario@exemplo.com', 'nomesobrenome@empresa.com.br', 'invalido@exemplo', 'usuario@.com', 'usuario@exemplo.c', 'usuario@exemplo..com', 'semaaroba.com']
    
    for email in emails:
        print(f"{email} {'Válido' if validar_email(email) else 'Inválido'}")