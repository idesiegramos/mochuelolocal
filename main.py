import streamlit as st
import os
import tiktoken
import openai
import tempfile
import whisper
import pytube
import re
import pinecone


from openai import OpenAI
from dotenv import load_dotenv
from tiktoken import encoding_for_model
from langchain_openai.chat_models import ChatOpenAI
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec



################################
# Secretos
################################

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
print("'Secretos' cargados correctamente")



################################
# Vídeo de prueba
################################

YOUTUBE_VIDEO_URL = "https://www.youtube.com/watch?v=dgZaIk3iFhc" # Clase MEP de IDESIE
# YOUTUBE_VIDEO_URL = "https://www.youtube.com/watch?v=ROax8vdhuEQ"



################################
# Modelo
################################

model_name = "gpt-3.5-turbo"

model = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model=model_name,
    temperature=0,
    max_tokens=1000,
    #top_p=1,
    #frequency_penalty=0,
    #presence_penalty=0.6
)
print(f"Modelo '{model_name}' cargado correctamente")



################################
# Transcripción con youtube-transcript-api
################################

def extract_video_id(url):
    # Intenta extraer el ID del video de la URL estándar y corta
    patterns = [
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([^&]+)',  # URL estándar
        r'(?:https?://)?youtu\.be/([^?]+)'                         # URL corta
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    raise ValueError("URL de video no válida")

# Reemplaza 'your_video_url' con la URL del video de YouTube
video_url = YOUTUBE_VIDEO_URL
YOUTUBE_VIDEO_ID = extract_video_id(video_url)
print(f"ID del vídeo de YouTube: {YOUTUBE_VIDEO_ID}")


def get_transcript(video_id):
    try:
        # Obtener la transcripción del video
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])

        # Concatenar las partes de la transcripción en un solo texto
        transcript_text = "\n".join([entry['text'] for entry in transcript])
        return transcript_text

    except Exception as e:
        return str(e)

video_id = YOUTUBE_VIDEO_ID
transcription_y = get_transcript(video_id)
with open("./transcripts/transcription_y.txt", "w", encoding="utf-8") as file:
            file.write(transcription_y)



################################
# Vector store
################################





###############################################################################
# Construimos la página web
###############################################################################
