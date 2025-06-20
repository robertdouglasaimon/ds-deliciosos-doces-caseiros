# Sistema de Pedidos Internos (Streamlit)
# 📦 Sistema de Pedidos Internos – DS Doces Artesanais

Aplicação interna desenvolvida em **Python + Streamlit** para controle rápido e acessível de pedidos na produção da **DS Doces Artesanais**. Criado para facilitar o dia a dia, gerenciar solicitações e manter o fluxo de atendimento com organização.

## 🧪 Tecnologias Utilizadas
- Python 3.x
- Streamlit
- Pandas
- CSV (armazenamento simples local)
- (Opcional) SQLite ou integração com Google Sheets

## 🚀 Funcionalidades
- 📋 **Cadastro de pedidos** com nome, produto, forma de pagamento e observações
- 👁️ **Visualização de pedidos em tabela dinâmica**
- ✅ **Alteração de status** para "Pendente", "Em produção" ou "Entregue"
- 📦 Exportação dos dados (.csv) para relatórios e backup
- 🔐 Acesso offline sem servidor ou banco externo

## 🖥️ Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/ds-pedidos-streamlit.git
   cd ds-pedidos-streamlit
    ```

2. Crie um ambiente virtual:
   ```python -m venv venv
    source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```

3. Instale as dependências:
   ```
    pip install -r requirements.txt
   ```

4. Execute o sistema:
   ```
   streamlit run app.py
   ```

## 💡 Estrutura
```
    📁 ds-pedidos-streamlit
    ├── app.py               # Aplicação principal
    ├── pedidos.csv          # Base local com dados dos pedidos
    ├── requirements.txt     # Bibliotecas utilizadas
    └── assets/              # (opcional) Imagens, logos, etc.
```

## ✨ Observações
<p>
    <ul>
        <li>Este sistema roda localmente, sem necessidade de internet ou login.</li>
        <li>Ideal para uso interno com atualizações manuais.</li>
        <li>Pode ser hospedado no Streamlit Cloud para acesso remoto com link privado</li>
    </ul>
</p>


## 🔒 Acesso
Esse sistema é de uso **interno**, criado para facilitar o dia a dia da produção e não está conectado a banco de dados externo ou API de pedidos.

---

🛠️ *Desenvolvido com carinho para acompanhar o crescimento da marca que adoça vidas.*  
Programado por <a href="https://github.com/robertdouglasaimon">Robert</a> com sabor, paciência e Python 🍬🐍
