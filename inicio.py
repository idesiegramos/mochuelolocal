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
    "Busca, investiga, documenta. Aquí, donde la tecnología de la Inteligencia Aritficial se une al aprendizaje avanzado, encontrarás todo lo que necesites. 
    A continuación te mostramos las principales utilidades:"
    "1.-Transcribe de manera automática y precisa los videos de tus clases del Máster BIM."
    "2.- Resume el contenido principal de las clases."
    "3.- Responde preguntas relacionadas con el vídeo de las clases."
    )


st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
