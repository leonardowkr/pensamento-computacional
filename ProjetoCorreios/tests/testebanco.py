import sqlite3

conn = sqlite3.connect("teste.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE linhaTransporte (
               id INTEGER PRIMARY KEY,
               origem TEXT NOT NULL,
               destino TEXT NOT NULL,
               distancia    
               ) 

    ''')