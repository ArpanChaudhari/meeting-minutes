# Reusable UI/HTML helper functions
import streamlit as st
from config import AUDIO_MODEL, LLM_MODELS, DEFAULT_LLM


# Model Selector
def render_model_selector():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        selected_model_name = st.selectbox(
            "Summarization Model",
            options=list(LLM_MODELS.keys()),
            index=list(LLM_MODELS.keys()).index(DEFAULT_LLM),
            key="model_selector",
        )
    return LLM_MODELS[selected_model_name]


# Hero Section
def render_hero():
    st.markdown(
        """
    <div class="hero-container">
        <div class="hero-icon">🎙️</div>
        <div class="hero-title">AI Meeting Minutes Generator</div>
        <div class="hero-subtitle">
            Upload your meeting recording and get beautifully structured meeting minutes 
            in seconds — powered by Groq's lightning-fast AI.
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Pipeline visualization
    st.markdown(
        """
    <div class="pipeline-bar">
        <div class="pipe-step s1">Upload Audio</div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step s2">Transcribe</div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-step s3">Generate Minutes</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# Upload Section
def render_upload_section():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            """
        <div class="glass-card">
            <div class="card-header">
                <span class="card-header-icon">📁</span>
                <span class="card-header-text">Upload Meeting Recording</span>
            </div>
            <div class="card-desc">
                Drop your audio file below. Supports MP3, WAV, M4A, WEBM, OGG, FLAC, and MP4 formats.
                Maximum file size: 25 MB (Groq API limit).
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        uploaded_file = st.file_uploader(
            "Upload Audio File",
            type=["mp3", "wav", "m4a", "webm", "ogg", "flac", "mp4"],
            label_visibility="collapsed",
            key="audio_uploader",
        )

    return uploaded_file


# File Info Metrics
def render_file_metrics(uploaded_file):
    file_size_mb = uploaded_file.size / (1024 * 1024)
    st.markdown(
        f"""
    <div class="metrics-row" style="justify-content: center;">
        <div class="metric-card">
            <div class="metric-label">{uploaded_file.name}</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">{file_size_mb:.1f} MB</div>
            <div class="metric-label">File Size</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">{uploaded_file.type.split('/')[-1].upper()}</div>
            <div class="metric-label">Format</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# Status Badges
def render_status(text, status_type="processing"):
    st.markdown(
        f"""
    <div style="text-align:center; margin: 1rem 0;">
        <span class="status-badge status-{status_type}">{text}</span>
    </div>
    """,
        unsafe_allow_html=True,
    )


# Word Count Metric
def render_word_count(word_count):
    st.markdown(
        f"""
    <div class="metrics-row" style="justify-content: center;">
        <div class="metric-card">
            <div class="metric-value">{word_count:,}</div>
            <div class="metric-label">Words Transcribed</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# Results Section
def render_results(minutes):
    st.markdown(
        """
    <div class="results-header">
        <div class="results-title">Your Meeting Minutes</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="glass-card" style="border-color: rgba(52, 211, 153, 0.3);">
    """,
        unsafe_allow_html=True,
    )
    st.markdown(minutes)
    st.markdown("</div>", unsafe_allow_html=True)


# Download Buttons
def render_downloads(minutes, transcription):
    st.divider()
    col_d1, col_d2, col_d3 = st.columns([1, 2, 1])
    with col_d2:
        st.download_button(
            label="Download Meeting Minutes (.md)",
            data=minutes,
            file_name="meeting_minutes.md",
            mime="text/markdown",
            use_container_width=True,
            type="primary",
        )
        st.download_button(
            label="Download Transcript (.txt)",
            data=transcription,
            file_name="transcript.txt",
            mime="text/plain",
            use_container_width=True,
        )


# Footer
def render_footer():
    st.markdown(
        """
    <div class="footer">
        Powered by <a href="https://groq.com" target="_blank">Groq</a> · 
        Whisper + Groq LLMs · Built with 
        <a href="https://streamlit.io" target="_blank">Streamlit</a>
    </div>
    """,
        unsafe_allow_html=True,
    )
