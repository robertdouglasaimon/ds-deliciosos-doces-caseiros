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
