# All configuration constants in one place

# Audio transcription model (Groq's Whisper)
AUDIO_MODEL = "whisper-large-v3-turbo"

# Available LLM models for summarization
LLM_MODELS = {
    "OpenAI GPT-OSS 120B (Best Quality)": "openai/gpt-oss-120b",
    "Qwen 3.8 27B (Fast)": "qwen/qwen3.8-27b",
    "OpenAI GPT-OSS 20B (Fastest)": "openai/gpt-oss-20b",
}

# Default model selection
DEFAULT_LLM = "OpenAI GPT-OSS 120B (Best Quality)"

# System prompt — tells the LLM how to behave
SYSTEM_PROMPT = """
You are an expert meeting minutes generator. You produce professional, well-structured 
minutes of meetings from transcripts. Your output must be in clean markdown format 
(without code blocks) and include the following sections:

1. **Meeting Summary** — A concise overview including attendees (if identifiable), 
   location, date, and purpose of the meeting.
2. **Key Discussion Points** — The main topics discussed, with enough detail to 
   understand the context.
3. **Key Takeaways** — The most important conclusions or insights from the meeting.
4. **Action Items** — Specific tasks with owners (if identifiable) and deadlines 
   (if mentioned).

Be thorough but concise. Use professional language.
"""

# User prompt template — {transcription} is replaced with the actual transcript
USER_PROMPT_TEMPLATE = """
Below is a transcript of a meeting. Please generate comprehensive meeting minutes 
in markdown format (without code blocks), including:
- A summary with attendees, location and date (if identifiable from the transcript)
- Key discussion points
- Key takeaways
- Action items with owners (if identifiable)

Transcript:
{transcription}
"""
