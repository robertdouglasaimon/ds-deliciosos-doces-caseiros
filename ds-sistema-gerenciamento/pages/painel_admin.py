import streamlit as st
import sqlite3

# **💾 Configuração e conexão**
st.set_page_config(page_title="Painel Administrativo", layout="wide")

# **🛠️ Conectar ao banco**
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

# **📌 Cadastro de Produtos**
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

# **📌 Cadastro de Clientes com Endereço**
elif aba == "Clientes":
    st.header("Cadastro de Clientes")
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
        st.success("✅ Cliente cadastrado com sucesso!")

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

    # **Adicionar nova categoria**
    nova_categoria = st.text_input("Nova Categoria")
    if st.button("Adicionar Categoria"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (nova_categoria,))
        conn.commit()
        conn.close()
        st.success(f"✅ Categoria '{nova_categoria}' adicionada!")

    # **Selecionar uma categoria existente para excluir**
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM categorias")
    categorias_disponiveis = [cat[0] for cat in cursor.fetchall()]
    conn.close()

    categoria_excluir = st.selectbox("Escolha uma categoria para excluir", categorias_disponiveis)
    if st.button("Excluir Categoria"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categorias WHERE nome = ?", (categoria_excluir,))
        conn.commit()
        conn.close()
        st.success(f"🚨 Categoria '{categoria_excluir}' removida!")

    # **Tabela de visualização de categorias e produtos**
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

# **📌 Relatórios Financeiros com entrada e exclusão de valores**
elif aba == "Relatórios":
    st.header("📑 Relatórios Financeiros")

    # **Inserir valor financeiro**
    valor_financeiro = st.number_input("Valor da receita/despesa", min_value=0.01)
    tipo_financeiro = st.selectbox("Tipo", ["Receita", "Despesa"])
    if st.button("Adicionar Valor"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO financeiro (valor, tipo) VALUES (?, ?)", (valor_financeiro, tipo_financeiro))
        conn.commit()
        conn.close()
        st.success("✅ Valor financeiro registrado!")

    # **Excluir um valor financeiro**
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, valor, tipo FROM financeiro")
    valores_financeiros = cursor.fetchall()
    conn.close()

    if valores_financeiros:
        valor_excluir = st.selectbox("Escolha um valor para excluir", [f"{v[1]} ({v[2]})" for v in valores_financeiros])
        if st.button("Excluir Valor"):
            valor_id = [v[0] for v in valores_financeiros if f"{v[1]} ({v[2]})" == valor_excluir][0]
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM financeiro WHERE id = ?", (valor_id,))
            conn.commit()
            conn.close()
            st.success("🚨 Valor financeiro removido!")

    # **Mostrar métricas financeiras**
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(valor) FROM financeiro WHERE tipo='Receita'")
    receita_total = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(valor) FROM financeiro WHERE tipo='Despesa'")
    despesa_total = cursor.fetchone()[0] or 0
    conn.close()

    st.metric("💰 Total de Receitas", receita_total)
    st.metric("📉 Total de Despesas", despesa_total)
