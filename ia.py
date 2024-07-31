
# PESTAÑAS
pages = {
    "Inteligencia IDESIE": [
        st.Page("inicio.py", title="Inicio"),
        st.Page("ia.py", title="Accede a nuestra IA"),
        st.Page("repositorio.py", title="Repositorio de clases"),
        st.Page("acerca_de.py", title="Acerca de"),
    ],
}

pg = st.navigation(pages)
pg.run()

# Título y descripción

st.title("IA de IDESIE Business&Tech School")
st.write(
    "Esta Inteligencia Artificial te ayudará a con el contenido de las clases impartidas en IDESIE. "
    "Para usar esta aplicación, solo debes escribir en el chat la información que quieres obtener, como por ejemplo un resumen con los puntos importantes de la clase o resolver otro tipo de dudas relacionadas con el contenido del vídeo. "
    "Te será de ayuda."
)
import streamlit as st

option = st.selectbox(
    "Asignatura",
    ("Fundamentos BIM", "REVIT ARQ", "REVIT MEP", "Management Skills"),
)

st.write("You selected:", option)

st.video(f"{YOUTUBE_VIDEO_URL}")
st.write(YOUTUBE_VIDEO_URL)

with st.expander("Transcripción (primeros 1000 caracteres)"):
     st.write(transcription_y[:1000])

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = OPENAI_API_KEY
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("What is up?"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

