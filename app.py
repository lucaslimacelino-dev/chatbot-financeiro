import streamlit as st
from chatbot import FinanceiroChatbot

st.set_page_config(page_title="Chatbot Financeiro", layout="centered")

# ✅ Mantém o bot entre execuções
if "bot" not in st.session_state:
    st.session_state.bot = FinanceiroChatbot()

bot = st.session_state.bot

st.title("💰 Gestor Financeiro")

# Tabs para separar entrada
tab1, tab2 = st.tabs(["Adicionar Gasto", "Adicionar Receita"])

with tab1:
    st.header("📉 Registrar Gasto")
    with st.form("form_gasto"):
        desc = st.text_input("Descrição do gasto", key="gasto_desc")
        valor = st.number_input("Valor (R$)", min_value=0.01, step=0.01, key="gasto_valor")
        cat = st.selectbox("Categoria", ["Alimentação", "Transporte", "Lazer", "Outros"], key="gasto_cat")
        if st.form_submit_button("Adicionar"):
            if desc.strip() == "":
                st.error("A descrição do gasto não pode estar vazia.")
            else:
                bot.adicionar_gasto(desc, valor, cat)
                st.success("Gasto registrado com sucesso!")

with tab2:
    st.header("📈 Registrar Receita")
    with st.form("form_receita"):
        desc = st.text_input("Descrição da receita", key="receita_desc")
        valor = st.number_input("Valor (R$)", min_value=0.01, step=0.01, key="receita_valor")
        cat = st.selectbox("Categoria", ["Salário", "Investimento", "Outros"], key="receita_cat")
        if st.form_submit_button("Adicionar"):
            if desc.strip() == "":
                st.error("A descrição da receita não pode estar vazia.")
            else:
                bot.adicionar_receita(desc, valor, cat)
                st.success("Receita registrada com sucesso!")

st.divider()

st.subheader("📊 Totais por Categoria")
for categoria, total in bot.total_por_categoria().items():
    st.write(f"- **{categoria}**: R$ {total:.2f}")

st.subheader("💵 Saldo Total")
st.metric("Saldo", f"R$ {bot.saldo_total():.2f}")

if st.checkbox("📄 Ver histórico"):
    st.subheader("🧾 Transações")
    for t in bot.listar_transacoes():
        st.write(f"- {t.descricao} | R$ {t.valor:.2f} | {t.categoria} | [{t.__class__.__name__}]")
