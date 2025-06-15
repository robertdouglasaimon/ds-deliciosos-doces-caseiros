import streamlit as st
import sqlite3

# Configuração inicial da página
st.set_page_config(page_title="Login - Administrador", layout="centered")

# Função para conectar ao banco SQLite
def conectar():
    return sqlite3.connect("ds_banco.db")

# Função para garantir que a tabela `usuarios` existe no banco
def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Executar a função ao iniciar o sistema
inicializar_banco()

# Função de autenticação no SQLite
def autenticar(usuario, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT tipo FROM usuarios WHERE nome=? AND senha=?", (usuario, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

# Interface de Login
st.title("Login - Administrador")

usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    tipo = autenticar(usuario, senha)
    if tipo:
        st.success(f"Bem-vindo, {usuario}! Você está logado como {tipo[0]}.")
        st.session_state["usuario_logado"] = usuario

        # Redirecionamento correto para o painel
        st.switch_page("painel_admin")
    else:
        st.error("Usuário ou senha incorretos!")
