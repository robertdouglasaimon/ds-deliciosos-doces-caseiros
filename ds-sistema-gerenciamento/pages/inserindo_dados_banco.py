import sqlite3

# Inserindado dados no banco manualmente #

def conectar():
    return sqlite3.connect("ds_banco.db")

def iserir_dados():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios (
        nome, 
        senha, 
        tipo
        ) 
        VALUES 
        ('robertdouglasaimon', 'Douglas362500414@@@@', 'admin'),
        ('ds_diego', 'DsDiego2025', 'admin');
    """)



