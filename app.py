import streamlit as st
import pandas as pd

st.set_page_config(page_title="Taça das Cidades", layout="wide")

# O teu link
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0RCqjD-h0SJHNJLl-OC9TqzBDzec49tgiMyMxFeu4fmuz0fBuX8clatiqJWZ_jz9EYzjBJGd8HYaB/pub?output=csv"
META_PONTOS = 1000

# Removemos o código que escondia o menu para podermos ver os erros melhor agora

@st.cache_data(ttl=30)
def buscar_pontos():
    try:
        # Tenta ler o CSV
        df = pd.read_csv(SHEET_URL, header=None)
        
        # MOSTRA A TABELA NO ECRÃ DO STREAMLIT (Para depuração)
        st.write("🔍 **Como o Python está a ver a tua folha de cálculo:**", df)
        
        # Tenta extrair os pontos
        pontos_ninive = int(df.iloc[1, 1])
        pontos_juda = int(df.iloc[2, 1])
        return pontos_ninive, pontos_juda
        
    except Exception as e:
        # MOSTRA O ERRO EXATO A VERMELHO NO ECRÃ
        st.error(f"⚠️ Erro técnico ao ler os dados: {e}")
        return 0, 0 

ninive_pts, juda_pts = buscar_pontos()

pct_ninive = min((ninive_pts / META_PONTOS) * 100, 100)
pct_juda = min((juda_pts / META_PONTOS) * 100, 100)

st.markdown("<h1 style='text-align: center;'>🏆 Taça das Cidades</h1>", unsafe_allow_html=True)

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
