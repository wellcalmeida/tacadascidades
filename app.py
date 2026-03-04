import streamlit as st
import pandas as pd

# Configuração da página para ocupar a tela toda
st.set_page_config(page_title="Taça das Cidades", layout="wide")

# ==========================================
# CONFIGURAÇÕES - EDITE AQUI
# ==========================================
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0RCqjD-h0SJHNJLl-OC9TqzBDzec49tgiMyMxFeu4fmuz0fBuX8clatiqJWZ_jz9EYzjBJGd8HYaB/pub?output=csv"
META_PONTOS = 1000  # Quantos pontos enchem a régua até o topo?

# Oculta o menu padrão do Streamlit para parecer um site finalizado
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=30)
def buscar_pontos():
    try:
        df = pd.read_csv(SHEET_URL, header=None)
        # Atenção: ajustado para linha 2 e 3, coluna B (índices 1 e 1)
        pontos_ninive = int(df.iloc[1, 1])
        pontos_juda = int(df.iloc[2, 1])
        return pontos_ninive, pontos_juda
    except Exception as e:
        return 0, 0 

ninive_pts, juda_pts = buscar_pontos()

pct_ninive = min((ninive_pts / META_PONTOS) * 100, 100)
pct_juda = min((juda_pts / META_PONTOS) * 100, 100)

st.markdown("<h1 style='text-align: center;'>🏆 Taça das Cidades</h1>", unsafe_allow_html=True)

# HTML sem indentação para evitar o bug de bloco de código no Streamlit
html_code = f"""
<div style="display: flex; justify-content: space-around; align-items: flex-end; height: 500px; padding: 20px; font-family: sans-serif; text-align: center;">
<div>
<div style="font-size: 50px; margin-bottom: 10px;">🐋</div>
<div style="width: 100px; height: 350px; border: 4px solid #333; border-radius: 20px; position:
