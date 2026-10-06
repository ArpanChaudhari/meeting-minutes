import os
import tempfile
import streamlit as st

from styles import CUSTOM_CSS
from services import get_groq_client, transcribe_audio, generate_minutes
from ui_components import (
    render_model_selector,
    render_hero,
    render_upload_section,
    render_file_metrics,
    render_status,
    render_word_count,
    render_results,
    render_downloads,
    render_footer,
)


# Page Config 
st.set_page_config(
    page_title="AI Meeting Minutes Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Apply Custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Hero Banner 
render_hero()

# Model Selector
selected_model_id = render_model_selector()

# File Upload 
uploaded_file = render_upload_section()

# Processing Pipeline 
if uploaded_file is not None:
    render_file_metrics(uploaded_file)

    # Generate button
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        generate_btn = st.button(
            "🚀  Generate Meeting Minutes",
            use_container_width=True,
            type="primary",
        )

    if generate_btn:
        client = get_groq_client()

        # Save uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=f".{uploaded_file.name.split('.')[-1]}",
        ) as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name

        try:
            # Step 1: Transcribe Audio
            render_status("Step 1/2 — Transcribing audio with Whisper...", "processing")

            with st.spinner(""):
                transcription = transcribe_audio(client, tmp_path)

            render_status("Transcription complete", "success")

            # Show transcript in expander
            with st.expander("View Full Transcript", expanded=False):
                st.markdown(
                    f'<div class="transcript-box">{transcription}</div>',
                    unsafe_allow_html=True,
                )

            render_word_count(len(transcription.split()))

            # Step 2: Generate Minutes
            render_status(
                f"Step 2/2 — Generating meeting minutes with {selected_model_id}...",
                "processing",
            )

            with st.spinner(""):
                minutes = generate_minutes(client, transcription, selected_model_id)

            render_status("Meeting minutes generated", "success")

            # Display Results
            render_results(minutes)

            # Download Buttons
            render_downloads(minutes, transcription)

        except Exception as e:
            render_status(f"Error: {str(e)}", "error")
            st.error(f"Details: {str(e)}")

        finally:
            # Clean up temp file
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

# Footer
render_footer()
