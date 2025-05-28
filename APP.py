import streamlit as st

st.title("Say Hello App")
name = st.text_input("Masukkan nama Anda:")
if name:
    st.write(f"Halo, {name}!")
