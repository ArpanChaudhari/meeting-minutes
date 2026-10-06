# AI Meeting Minutes Generator

An AI-powered web application that converts meeting audio recordings into professionally structured meeting minutes. Built with Streamlit, powered by Groq's ultra-fast inference engine.

## Features

- **Audio Transcription** — Converts audio to text using Groq's Whisper (whisper-large-v3-turbo)
- **AI Summarization** — Generates structured meeting minutes with multiple LLM options
- **Model Selection** — Choose between quality and speed with 3 available models
- **Download Support** — Export meeting minutes (.md) and transcript (.txt)
- **Dark Theme UI** — Premium glassmorphism design with smooth animations

## Tech Stack

| Technology | Purpose |
|------------|---------|
| [Streamlit](https://streamlit.io/) | Web framework |
| [Groq API](https://groq.com/) | AI inference (Whisper + LLMs) |
| Python | Backend logic |

## Project Structure

```
Mini Project3/
├── app.py              # Main entry point — orchestrates all modules
├── config.py           # Constants, model settings, and prompts
├── styles.py           # Custom CSS theme (dark glassmorphism)
├── services.py         # Groq API calls (transcribe + summarize)
├── ui_components.py    # Reusable Streamlit UI components
├── requirements.txt    # Python dependencies
├── .env                # API key 
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.9+
- Groq API key — get one free at [console.groq.com](https://console.groq.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ArpanChaudhari/meeting-minutes.git
   cd meeting-minutes
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/Mac
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**

   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY="your_groq_api_key_here"
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

   The app will open at `http://localhost:8501`

## How It Works

```
Upload Audio → Whisper Transcription → LLM Summarization → Download Minutes
```

1. Upload a meeting recording (MP3, WAV, M4A, WEBM, OGG, FLAC, MP4)
2. Groq's Whisper model transcribes the audio into text
3. A selected LLM analyzes the transcript and generates structured minutes
4. Download the formatted meeting minutes or raw transcript

## Available Models

| Model | Best For |
|-------|----------|
| OpenAI GPT-OSS 120B | Best quality output |
| Qwen 3.8 27B | Balanced speed and quality |
| OpenAI GPT-OSS 20B | Fastest response time |

## Output Format

The generated meeting minutes include:

- **Meeting Summary** — Overview with attendees, date, and purpose
- **Key Discussion Points** — Main topics with context
- **Key Takeaways** — Important conclusions and insights
- **Action Items** — Tasks with owners and deadlines

## Supported Audio Formats

MP3, WAV, M4A, WEBM, OGG, FLAC, MP4 (max 25 MB per Groq API limit)