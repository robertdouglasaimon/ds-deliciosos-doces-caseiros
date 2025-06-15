import streamlit as st
import sqlite3

# Configuração inicial da página
st.set_page_config(page_title="Login - Administrador", layout="centered")

# Função para conectar ao banco SQLite
def conectar():
    return sqlite3.connect("ds_banco.db")

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
        
        # Redirecionamento manual via link
        st.write("Clique no link abaixo para acessar o painel:")
        st.markdown("[Ir para o Painel](pages/painel_admin.py)", unsafe_allow_html=True)

    else:
        st.error("Usuário ou senha incorretos!")


