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
aba = st.sidebar.radio("Navegação", ["Cadastro", "Vendas Cadastradas", "Produtos", "Filtragem", "Categorias", "Relatórios", "Clientes"])

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

# **📌 Registro de Vendas**
elif aba == "Vendas Cadastradas":
    st.header("📦 Registrar uma Nova Venda")

    conn = conectar()
    cursor = conn.cursor()
    
    # **Puxar clientes cadastrados**
    cursor.execute("SELECT id, nome FROM clientes")
    clientes_disponiveis = {c[1]: c[0] for c in cursor.fetchall()}
    
    # **Puxar produtos cadastrados**
    cursor.execute("SELECT id, nome FROM produtos")
    produtos_disponiveis = {p[1]: p[0] for p in cursor.fetchall()}
    
    # **Puxar categorias cadastradas**
    cursor.execute("SELECT nome FROM categorias")
    categorias_disponiveis = [cat[0] for cat in cursor.fetchall()]
    
    conn.close()

    # **Selecionar cliente (ou cadastrar novo)**
    cliente_venda_nome = st.selectbox("Selecione o Cliente", ["Cadastrar Novo Cliente"] + list(clientes_disponiveis.keys()), key="cliente_select")
    if cliente_venda_nome == "Cadastrar Novo Cliente":
        cliente_venda_nome = st.text_input("Digite o Nome do Cliente", key="cliente_nome_input")
        cliente_venda_id = None
    else:
        cliente_venda_id = clientes_disponiveis[cliente_venda_nome]

    # **Selecionar produto e categoria**
    produto_venda_nome = st.selectbox("Selecione o Produto", list(produtos_disponiveis.keys()), key="produto_select")
    produto_venda_id = produtos_disponiveis[produto_venda_nome]
    categoria_venda = st.selectbox("Selecione a Categoria", categorias_disponiveis, key="categoria_select")

    # **Inserir valor da compra**
    valor_venda = st.number_input("Valor Total da Compra", min_value=0.01, key="valor_venda")
    
    # **Inserir data da venda**
    data_venda = st.date_input("📆 Data da Venda", key="data_venda")

    if st.button("Registrar Venda", key="registrar_venda"):
        conn = conectar()
        cursor = conn.cursor()

        # **Se for um novo cliente, cadastrá-lo antes de registrar a venda**
        if cliente_venda_id is None:
            cursor.execute("INSERT INTO clientes (nome) VALUES (?)", (cliente_venda_nome,))
            cliente_venda_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO vendas_cadastradas (usuario, cliente_id, produto_id, categoria, valor_total, data)
            VALUES (?, ?, ?, ?, ?, ?)
        """, ("admin", cliente_venda_id, produto_venda_id, categoria_venda, valor_venda, data_venda))

        conn.commit()
        conn.close()
        st.success("✅ Venda registrada com sucesso!")

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
        
        if produto_excluir and st.button("Excluir Produto"):
            produto_id = [p[0] for p in produtos if f"{p[1]} ({p[2]})" == produto_excluir][0]
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
            conn.commit()
            conn.close()
            st.success("🚨 Produto removido com sucesso!")
            st.experimental_rerun()
    else:
        st.write("Nenhum produto cadastrado.")

# **📌 Cadastro e Acompanhamento de Clientes**
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

    # **Quadro de Clientes Cadastrados**
    st.subheader("📋 Clientes Cadastrados")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, telefone, endereco FROM clientes")
    clientes = cursor.fetchall()
    conn.close()

    if clientes:
        st.write(clientes)
        cliente_excluir = st.selectbox("Selecione um cliente para excluir", [f"{c[1]} - {c[2]}" for c in clientes])
        
        if cliente_excluir and st.button("Excluir Cliente"):
            cliente_id = [c[0] for c in clientes if f"{c[1]} - {c[2]}" == cliente_excluir][0]
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
            conn.commit()
            conn.close()
            st.success("🚨 Cliente removido com sucesso!")
            st.experimental_rerun()
    else:
        st.write("Nenhum cliente cadastrado.")

# **📌 Correção na aba Categorias**
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
    categorias_disponiveis = [cat[0] for cat in cursor.fetchall()]
    conn.close()

    st.write(categorias_disponiveis)

    categoria_excluir = st.selectbox("Selecione uma categoria para excluir", categorias_disponiveis)
    if categoria_excluir and st.button("Excluir Categoria"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categorias WHERE nome = ?", (categoria_excluir,))
        conn.commit()
        conn.close()
        st.success("🚨 Categoria removida com sucesso!")
   
# **📌 Correção na aba Relatórios**
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

    st.header("📊 Filtragem de Dados")

    filtro_produto = st.text_input("🔍 Filtrar por ID do Produto", key="filtro_produto")
    filtro_cliente = st.text_input("🔍 Filtrar por ID do Cliente", key="filtro_cliente")
    filtro_data = st.date_input("📆 Filtrar por Data", key="filtro_data")

    if st.button("Buscar"):
        conn = conectar()
        cursor = conn.cursor()

        # **Verificar se a tabela existe**
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='vendas'")
        tabela_existe = cursor.fetchone()
        if not tabela_existe:
            st.error("🚨 A tabela 'vendas' não existe no banco de dados.")
            conn.close()
            st.stop()

        # **Corrigir formato da data para SQLite**
        filtro_data_str = filtro_data.strftime("%Y-%m-%d") if filtro_data else None

        query = "SELECT * FROM vendas WHERE 1=1"
        params = []

        if filtro_produto:
            query += " AND produto_id = ?"
            params.append(filtro_produto)

        if filtro_cliente:
            query += " AND cliente_id = ?"
            params.append(filtro_cliente)

        if filtro_data_str:
            query += " AND data >= ?"
            params.append(filtro_data_str)

        cursor.execute(query, params)
        resultado = cursor.fetchall()
        conn.close()

        if resultado:
            st.write("📋 Resultados encontrados:", resultado)
        else:
            st.warning("🚨 Nenhum resultado encontrado!")

    # **Tabela Geral**
    st.subheader("📋 Todas as Vendas Registradas")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vendas")
    vendas_gerais = cursor.fetchall()
    conn.close()
    
    st.write(vendas_gerais)

# **📌 Correção na aba Filtragem**
elif aba == "Filtragem":
    st.header("🔎 Filtragem de Dados")

    filtro_nome = st.text_input("🔍 Nome do Cliente ou Produto", key="filtro_nome")
    filtro_cliente_id = st.text_input("🆔 ID do Cliente", key="filtro_cliente_id")
    filtro_produto_id = st.text_input("🆔 ID do Produto", key="filtro_produto_id")
    filtro_data_inicio = st.date_input("📆 Data Inicial", key="filtro_data_inicio")
    filtro_data_fim = st.date_input("📆 Data Final", key="filtro_data_fim")

    if st.button("Buscar", key="buscar_dados"):
        conn = conectar()
        cursor = conn.cursor()

        # **Criar consulta SQL dinâmica**
        query = """
            SELECT vc.id, c.nome AS cliente, p.nome AS produto, vc.categoria, vc.valor_total, vc.data
            FROM vendas_cadastradas vc
            JOIN clientes c ON vc.cliente_id = c.id
            JOIN produtos p ON vc.produto_id = p.id
            WHERE 1=1
        """
        params = []

        if filtro_nome:
            query += " AND (c.nome LIKE ? OR p.nome LIKE ?)"
            params.extend([f"%{filtro_nome}%", f"%{filtro_nome}%"])

        if filtro_cliente_id:
            query += " AND vc.cliente_id = ?"
            params.append(filtro_cliente_id)

        if filtro_produto_id:
            query += " AND vc.produto_id = ?"
            params.append(filtro_produto_id)

        if filtro_data_inicio and filtro_data_fim:
            query += " AND vc.data BETWEEN ? AND ?"
            params.extend([filtro_data_inicio.strftime("%Y-%m-%d"), filtro_data_fim.strftime("%Y-%m-%d")])

        cursor.execute(query, params)
        resultado = cursor.fetchall()
        conn.close()

        if resultado:
            st.subheader("📋 Resultados da Busca")
            st.write(resultado)
        else:
            st.warning("🚨 Nenhum resultado encontrado!")

    # **Tabela Geral com todas as vendas**
    st.subheader("📋 Todas as Vendas Registradas")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT vc.id, c.nome AS cliente, p.nome AS produto, vc.categoria, vc.valor_total, vc.data
        FROM vendas_cadastradas vc
        JOIN clientes c ON vc.cliente_id = c.id
        JOIN produtos p ON vc.produto_id = p.id
    """)
    vendas_gerais = cursor.fetchall()
    conn.close()

    st.write(vendas_gerais)
