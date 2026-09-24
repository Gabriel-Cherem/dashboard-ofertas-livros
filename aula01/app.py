"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import libs
import dados


st.title("📚 Dashboard de Livros")
st.write("Se você está vendo esta página, o seu ambiente está pronto! 🎉")


livros = dados.ler_livros()

st.write(livros)
