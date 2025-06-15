import sqlite3

# **💾 Função para conectar ao banco**
def conectar():
    return sqlite3.connect("ds-sistema-gerenciamento/ds_banco.db")

# **🔧 Função para atualizar a tabela clientes**
def atualizar_banco():
    conn = conectar()
    cursor = conn.cursor()

    # **Verificar se as colunas já existem antes de adicionar**
    cursor.execute("PRAGMA table_info(clientes)")
    colunas = [col[1] for col in cursor.fetchall()]

    if "email" not in colunas:
        cursor.execute("ALTER TABLE clientes ADD COLUMN email TEXT")

    if "endereco" not in colunas:
        cursor.execute("ALTER TABLE clientes ADD COLUMN endereco TEXT")

    conn.commit()
    conn.close()

# **Executar a atualização no banco**
atualizar_banco()
