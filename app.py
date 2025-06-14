import streamlit as st
from computador import Computador

st.set_page_config(page_title="Simulador de Computador", layout="centered")
st.title("💻 Simulador de Computador")

st.write("Preencha os dados do computador abaixo:")

# Formulário para entrada de dados
with st.form("form_computador"):
    marca = st.text_input("Marca do computador", placeholder="Ex: Dell, HP, Lenovo")
    memoria_ram = st.number_input("Memória RAM (em GB)", min_value=2, max_value=128, step=2)
    armazenamento = st.number_input("Armazenamento (em GB)", min_value=128, max_value=2048, step=128)
    submitted = st.form_submit_button("Criar Computador")

if submitted:
    pc = Computador(marca, memoria_ram, armazenamento)
    st.success("✅ Computador criado com sucesso!")
    
    st.subheader("🔍 Informações do Computador:")
    st.write("Marca:", pc.get_marca())
    st.write("Memória RAM:", f"{pc.get_memoria_ram()} GB")
    st.write("Armazenamento:", f"{pc.get_armazenamento()} GB")
    st.write("Status:", "Ligado" if pc.is_ligado() else "Desligado")

    if st.button("🔌 Ligar Computador"):
        mensagem = pc.ligar_computador()
        st.info(mensagem)
        st.write("Status atual:", "Ligado" if pc.is_ligado() else "Desligado")
