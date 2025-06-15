import streamlit as st

# Teste básico para garantir que a página renderize
st.set_page_config(page_title="Painel Administrativo", layout="wide")
st.title("Painel Administrativo 🍬")

st.write("Se você está vendo esta mensagem, a página carregou corretamente! ✅")

aba = st.sidebar.radio("Selecione uma opção:", ["Cadastro", "Filtragem", "Categorias", "Relatórios"])
st.write(f"Aba selecionada: {aba}")
