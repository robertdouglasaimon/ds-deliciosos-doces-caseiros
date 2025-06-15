import streamlit as st
import sqlite3

# **💾 Configuração e conexão**
st.set_page_config(page_title="Painel Administrativo", layout="wide")

# **🛠️ Conectar ao banco**
def conectar():
    return sqlite3.connect("ds-sistema-gerenciamento/ds_banco.db")

# **📌 Garantir que todas as tabelas do banco existem**
def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereco TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL,
            categoria TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS financeiro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor REAL NOT NULL,
            tipo TEXT NOT NULL,
            descricao TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

# **💡 Executar a função ao iniciar o sistema**
inicializar_banco()

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
aba = st.sidebar.radio("Navegação", ["Cadastro", "Produtos", "Filtragem", "Categorias", "Relatórios", "Clientes"])

# **📌 Cadastro de Produtos**
if aba == "Cadastro":
    st.header("Cadastro de Produtos")
    nome_produto = st.text_input("Nome do Produto")
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM categorias")
    categorias_disponiveis = [cat[0] for cat in cursor.fetchall()]
    conn.close()
    
    categoria_produto = st.selectbox("Categoria", categorias_disponiveis)
    preco_produto = st.number_input("Preço", min_value=0.01)
    quantidade_produto = st.number_input("Quantidade", min_value=1)

    if st.button("Cadastrar Produto"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco, quantidade, categoria) VALUES (?, ?, ?, ?)",
                       (nome_produto, preco_produto, quantidade_produto, categoria_produto))
        conn.commit()
        conn.close()
        st.success("✅ Produto cadastrado com sucesso!")

# **📌 Exibir e excluir produtos**
elif aba == "Produtos":
    st.header("📦 Produtos Cadastrados")
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, categoria, preco, quantidade FROM produtos")
    produtos = cursor.fetchall()
    conn.close()

    if produtos:
        st.write(produtos)
        produto_excluir = st.selectbox("Selecione um produto para excluir", [f"{p[1]} ({p[2]})" for p in produtos])
        
        if st.button("Excluir Produto"):
            produto_id = [p[0] for p in produtos if f"{p[1]} ({p[2]})" == produto_excluir][0]
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
            conn.commit()
            conn.close()
            st.success("🚨 Produto removido com sucesso!")
    else:
        st.write("Nenhum produto cadastrado.")

# **📌 Filtragem de Dados**
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

# **📌 Gerenciamento de Categorias**
elif aba == "Categorias":
    st.header("🗂️ Gerenciamento de Categorias")

    nova_categoria = st.text_input("Nova Categoria")
    if st.button("Adicionar Categoria"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (nova_categoria,))
        conn.commit()
        conn.close()
        st.success(f"✅ Categoria '{nova_categoria}' adicionada!")

    st.subheader("📋 Categorias Existentes")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM categorias")
    categorias_existentes = [cat[0] for cat in cursor.fetchall()]
    conn.close()

    st.write(categorias_existentes)

# **📌 Relatórios Financeiros**
elif aba == "Relatórios":
    st.header("📑 Relatórios Financeiros")

    valor_financeiro = st.number_input("Valor da receita/despesa", min_value=0.01)
    tipo_financeiro = st.selectbox("Tipo", ["Receita", "Despesa"])
    descricao_financeiro = st.text_area("Descrição da Receita/Despesa")

    if st.button("Adicionar Valor"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO financeiro (valor, tipo, descricao) VALUES (?, ?, ?)",
                       (valor_financeiro, tipo_financeiro, descricao_financeiro))
        conn.commit()
        conn.close()
        st.success("✅ Valor financeiro registrado!")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT valor, tipo, descricao FROM financeiro")
    relatorio_financeiro = cursor.fetchall()
    conn.close()

    st.subheader("📋 Histórico Financeiro")
    st.write(relatorio_financeiro)

# **📌 Cadastro e exclusão de Clientes**
elif aba == "Clientes":
    st.header("📋 Cadastro de Clientes")
    nome_cliente = st.text_input("Nome do Cliente")
    email_cliente = st.text_input("Email do Cliente")
    telefone_cliente = st.text_input("Telefone")
    endereco_cliente = st.text_area("Endereço Completo")

    if st.button("Cadastrar Cliente"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)", 
                       (nome_cliente, email_cliente, telefone_cliente, endereco_cliente))
        conn.commit()
        conn.close()
        st.success("✅ Cliente cadastrado!")

    st.subheader("📋 Lista de Clientes")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, email, telefone, endereco FROM clientes")
    clientes = cursor.fetchall()
    conn.close()

    st.write(clientes)
