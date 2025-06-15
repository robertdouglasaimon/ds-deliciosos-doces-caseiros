import sqlite3

# **💾 Conectar ao banco**
def conectar():
    return sqlite3.connect("ds-sistema-gerenciamento/ds_banco.db")

# **🛠️ Função para inserir dados manualmente**
def inserir_dados():
    conn = conectar()
    cursor = conn.cursor()

    # **Correção: Passando os valores como argumentos separados**
    cursor.execute("""
        INSERT INTO usuarios (nome, senha, tipo)
        VALUES (?, ?, ?)
    """, ("geovana", "geovana147", "teste"))  

    conn.commit()
    conn.close()

# **🚀 Executar a inserção**
inserir_dados()







#----------INSERINDO TABELA VENDAS CADASTRADAS NO BANCO----------#
# import sqlite3

# # **💾 Conectar ao banco**
# def conectar():
#     return sqlite3.connect("ds-sistema-gerenciamento/ds_banco.db")

# # **🛠️ Criar a tabela `vendas_cadastradas`**
# def criar_tabela_vendas_cadastradas():
#     conn = conectar()
#     cursor = conn.cursor()
    
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS vendas_cadastradas (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             usuario TEXT NOT NULL,
#             cliente_id INTEGER NOT NULL,
#             produto_id INTEGER NOT NULL,
#             categoria TEXT NOT NULL,
#             valor_total REAL NOT NULL,
#             data DATE NOT NULL,
#             FOREIGN KEY (cliente_id) REFERENCES clientes(id),
#             FOREIGN KEY (produto_id) REFERENCES produtos(id),
#             FOREIGN KEY (categoria) REFERENCES categorias(nome)
#         )
#     """)
    
#     conn.commit()
#     conn.close()

# # **🛠️ Função para inserir uma venda manualmente**
# def inserir_venda():
#     conn = conectar()
#     cursor = conn.cursor()

#     cursor.execute("""
#         INSERT INTO vendas_cadastradas (usuario, cliente_id, produto_id, categoria, valor_total, data)
#         VALUES (?, ?, ?, ?, ?, ?)
#     """, ("admin", 1, 2, "Doces", 50.00, "2025-06-15"))

#     conn.commit()
#     conn.close()

# # **🚀 Executar criação da tabela e inserção de exemplo**
# criar_tabela_vendas_cadastradas()
# inserir_venda()
