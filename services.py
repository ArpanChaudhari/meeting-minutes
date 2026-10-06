import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# import constants from config.py
from config import AUDIO_MODEL, SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

# Load environment variables from .env file
load_dotenv()


# Initializing Groq Client
def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("GROQ_API_KEY not found in `.env` file. Please add it and restart.")
        st.stop()
    return Groq(api_key=api_key)


# Transcribing Audio
def transcribe_audio(client, audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=AUDIO_MODEL,
            file=audio_file,
            response_format="text",
        )
    return transcription


# Generating Minutes
def generate_minutes(client, transcription, model_id):
    user_prompt = USER_PROMPT_TEMPLATE.format(transcription=transcription)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]
    chat_completion = client.chat.completions.create(
        model=model_id,
        messages=messages,
        temperature=0.3,
        max_tokens=4096,
    )
    return chat_completion.choices[0].message.content
