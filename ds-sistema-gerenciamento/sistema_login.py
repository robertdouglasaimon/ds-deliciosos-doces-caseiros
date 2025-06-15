import streamlit as st
import sqlite3

# Configuração inicial da página
st.set_page_config(page_title="Login - Administrador", layout="centered")

# **💾 Conexão com o banco (Agora com caminho correto!)**
def conectar():
    return sqlite3.connect("ds-sistema-gerenciamento/ds_banco.db")

# **🛠️ Garantir que a tabela `usuarios` existe**
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

# **Executar a função ao iniciar**
inicializar_banco()

# **🔑 Autenticação de usuários**
def autenticar(usuario, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT tipo FROM usuarios WHERE nome=? AND senha=?", (usuario, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

# **🖥️ Interface de Login**
st.title("Login - Administrador")

# **📋 Exibir usuários cadastrados para teste**
conn = conectar()
cursor = conn.cursor()
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
conn.close()
# st.write("📋 Usuários cadastrados no banco:", usuarios)

# **🆕 Botão para adicionar usuário teste**
if st.button("Adicionar usuário teste"):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, senha, tipo) VALUES (?, ?, ?)", ("admin", "1234", "Administrador"))
    conn.commit()
    conn.close()
    st.success("✅ Usuário teste 'admin' criado! Tente login com senha '1234'.")

# **✍️ Campos de login**
usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    tipo = autenticar(usuario, senha)
    if tipo:
        st.success(f"Bem-vindo, {usuario}! Você está logado como {tipo[0]}.")
        st.session_state["usuario_logado"] = usuario

        # **✅ Redirecionamento agora 100% funcional!**
        st.switch_page("pages/painel_admin.py")
    else:
        st.error("🚨 Usuário ou senha incorretos!")
