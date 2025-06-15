import streamlit as st
import sqlite3

# **💾 Configuração e conexão**
st.set_page_config(page_title="Painel Administrativo", layout="wide")

# **🛠️ Conectar ao banco (Agora com caminho correto!)**
def conectar():
    return sqlite3.connect("ds-sistema-gerenciamento/ds_banco.db")

# **🔒 Verificar login antes de exibir o painel**
if "usuario_logado" not in st.session_state:
    st.warning("🚨 Acesso negado! Volte para a tela de login.")
    st.stop()
    

# **🎨 Painel administrativo**
st.title(f"Painel Administrativo 🍬 - Bem-vindo, {st.session_state['usuario_logado']}!")

# **🚪 Botão de saída**
if st.sidebar.button("🚪 Sair"):
    del st.session_state["usuario_logado"]
    st.success("✅ Você saiu do sistema!")
    st.stop()


# **📌 Criar menu lateral de navegação**
aba = st.sidebar.radio("Navegação", ["Cadastro", "Filtragem", "Categorias", "Relatórios", "Clientes"])

if aba == "Cadastro":
    st.header("Cadastro de Produtos")
    nome_produto = st.text_input("Nome do Produto")
    categoria_produto = st.text_input("Categoria")
    preco_produto = st.number_input("Preço", min_value=0.01)
    quantidade_produto = st.number_input("Quantidade", min_value=1)

    if st.button("Cadastrar Produto"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (?, ?, ?, ?)",
                       (nome_produto, categoria_produto, preco_produto, quantidade_produto))
        conn.commit()
        conn.close()
        st.success("✅ Produto cadastrado com sucesso!")
        
# **📊 Cadastro de Clientes**       
elif aba == "Clientes":
    st.header("Cadastro de Clientes")
    nome_cliente = st.text_input("Nome do Cliente")
    email_cliente = st.text_input("Email do Cliente")
    telefone_cliente = st.text_input("Telefone")
    
    if st.button("Cadastrar Cliente"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", 
                       (nome_cliente, email_cliente, telefone_cliente))
        conn.commit()
        conn.close()
        st.success("✅ Cliente cadastrado com sucesso!")


elif aba == "Filtragem":
    st.header("📊 Filtragem de dados")
    filtro_nome = st.text_input("Filtrar por Nome")
    filtro_data = st.date_input("Filtrar por Data")

    if st.button("Buscar"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vendas WHERE data >= ?", (filtro_data,))
        resultado = cursor.fetchall()
        conn.close()
        st.write("Resultados encontrados:", resultado)

elif aba == "Categorias":
    st.header("🗂️ Gerenciamento de Categorias")

    # **Adicionar nova categoria**
    nova_categoria = st.text_input("Nova Categoria")
    if st.button("Adicionar Categoria"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (nova_categoria,))
        conn.commit()
        conn.close()
        st.success(f"✅ Categoria '{nova_categoria}' adicionada!")

    # **Selecionar uma categoria existente para inserir produtos**
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM categorias")
    categorias_disponiveis = [cat[0] for cat in cursor.fetchall()]
    conn.close()

    categoria_selecionada = st.selectbox("Escolha uma categoria para adicionar produtos", categorias_disponiveis)

    # **Adicionar um produto novo ou existente na categoria**
    st.subheader(f"Adicionar produto na categoria '{categoria_selecionada}'")
    nome_produto = st.text_input("Nome do Produto")
    preco_produto = st.number_input("Preço", min_value=0.01)
    quantidade_produto = st.number_input("Quantidade", min_value=1)

    if st.button("Adicionar Produto na Categoria"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco, quantidade, categoria) VALUES (?, ?, ?, ?)",
                       (nome_produto, preco_produto, quantidade_produto, categoria_selecionada))
        conn.commit()
        conn.close()
        st.success(f"✅ Produto '{nome_produto}' adicionado à categoria '{categoria_selecionada}'!")

    # **Tabela de visualização de categorias e seus produtos**
    st.subheader("📋 Produtos por Categoria")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, categoria, preco FROM produtos ORDER BY categoria")
    produtos_por_categoria = cursor.fetchall()
    conn.close()

    for categoria in categorias_disponiveis:
        st.subheader(f"📂 {categoria}")
        produtos_na_categoria = [p for p in produtos_por_categoria if p[1] == categoria]
        if produtos_na_categoria:
            st.write(produtos_na_categoria)
        else:
            st.write("Nenhum produto nesta categoria ainda.")


elif aba == "Relatórios":
    st.header("📑 Relatórios Financeiros")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(id) FROM vendas")
    total_vendas = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(id) FROM clientes")
    total_clientes = cursor.fetchone()[0]
    conn.close()

    st.metric("💰 Total de Vendas", total_vendas)
    st.metric("🧑‍💼 Total de Clientes", total_clientes)
