import streamlit as st
import pandas as pd

# Configuração da página para ocupar a tela toda
st.set_page_config(page_title="Taça das Cidades", layout="wide")

# ==========================================
# CONFIGURAÇÕES - EDITE AQUI
# ==========================================
SHEET_URL = "COLE_AQUI_O_SEU_LINK_CSV_DO_SHEETS"
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
<div style="width: 100px; height: 350px; border: 4px solid #333; border-radius: 20px; position: relative; background: #fff; overflow: hidden; margin: 0 auto;">
<div style="position: absolute; bottom: 0; width: 100%; height: {pct_ninive}%; background: linear-gradient(to top, #002147, #0077be); transition: height 1s ease-in-out;"></div>
</div>
<div style="margin-top: 15px; font-weight: bold; font-size: 1.5em; color: white;">Nínive: {ninive_pts}</div>
<div style="color: #0077be; font-size: 1.2em; margin-top: 5px;">🌊 🐟 🐠</div>
</div>
<div>
<div style="font-size: 50px; margin-bottom: 10px;">🦁</div>
<div style="width: 100px; height: 350px; border: 4px solid #333; border-radius: 20px; position: relative; background: #fff; overflow: hidden; margin: 0 auto;">
<div style="position: absolute; bottom: 0; width: 100%; height: {pct_juda}%; background: linear-gradient(to top, #8b4513, #ff8c00, #ffd700); transition: height 1s ease-in-out;"></div>
</div>
<div style="margin-top: 15px; font-weight: bold; font-size: 1.5em; color: white;">Judá: {juda_pts}</div>
<div style="color: #ff8c00; font-size: 1.2em; margin-top: 5px;">🌿 🌵 🐆</div>
</div>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)
