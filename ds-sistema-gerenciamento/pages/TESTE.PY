import streamlit as st
import sqlite3

def conectar():
    return sqlite3.connect("ds-sistema-gerenciamento\ds_banco.db")

conn = conectar()
cursor = conn.cursor()
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
conn.close()

st.write("Usuários cadastrados no banco:", usuarios)
