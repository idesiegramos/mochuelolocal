import streamlit as st
st.logo(
    LOGO_URL_LARGE,
    link="https://streamlit.io/gallery",
    icon_image=LOGO_URL_SMALL,
)


st.image("OIP.jpg", caption="Open minded")

st.title("IDE-IA")
st.write(
    "Bienvenido a la Inteligencia Artificial de IDESIE"
    "Busca, investiga, documenta lo que necesites a través de nuestra IA."
)


st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
