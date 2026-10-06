# All custom CSS for the Streamlit app

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ── Global ── */
    .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* ── Remove Streamlit default top padding ── */
    .block-container {
        padding-top: 1rem !important;
    }
    .stMainBlockContainer {
        padding-top: 1rem !important;
    }

    /* ── Hero Section ── */
    .hero-container {
        text-align: center;
        padding: 0.5rem 1rem 0.5rem;
        margin-bottom: 0.5rem;
    }
    .hero-icon {
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
        display: inline-block;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.3rem;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #9ca3af;
        font-weight: 400;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }

    /* ── Pipeline Steps ── */
    .pipeline-bar {
        display: flex;
        justify-content: center;
        gap: 0.5rem;
        margin: 0.5rem auto;
        max-width: 700px;
        flex-wrap: wrap;
    }
    .pipe-step {
        display: flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.45rem 1rem;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.3px;
    }
    .pipe-step.s1 { background: rgba(102, 126, 234, 0.15); color: #667eea; border: 1px solid rgba(102, 126, 234, 0.3); }
    .pipe-step.s2 { background: rgba(118, 75, 162, 0.15); color: #a78bfa; border: 1px solid rgba(118, 75, 162, 0.3); }
    .pipe-step.s3 { background: rgba(240, 147, 251, 0.15); color: #f093fb; border: 1px solid rgba(240, 147, 251, 0.3); }
    .pipe-arrow { color: #4b5563; font-size: 1.1rem; }

    /* ── Card Styling ── */
    .glass-card {
        background: linear-gradient(135deg, rgba(30, 32, 48, 0.85), rgba(20, 22, 36, 0.95));
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 16px;
        padding: 0.5rem;
        margin-bottom: 1.2rem;
        backdrop-filter: blur(20px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
        border-color: rgba(102, 126, 234, 0.4);
        box-shadow: 0 8px 40px rgba(102, 126, 234, 0.1);
    }
    .card-header {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 1rem;
    }
    .card-header-icon {
        font-size: 1.4rem;
    }
    .card-header-text {
        font-size: 1.15rem;
        font-weight: 700;
        color: #e5e7eb;
    }
    .card-desc {
        font-size: 0.85rem;
        color: #9ca3af;
        margin-bottom: 1rem;
        line-height: 1.5;
    }

    /* ── Status Badges ── */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.5rem 1.2rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.3rem 0;
    }
    .status-success {
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    .status-processing {
        background: rgba(102, 126, 234, 0.15);
        color: #818cf8;
        border: 1px solid rgba(102, 126, 234, 0.3);
        animation: pulse-glow 2s ease-in-out infinite;
    }
    @keyframes pulse-glow {
        0%, 100% { box-shadow: 0 0 5px rgba(102, 126, 234, 0.2); }
        50% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.4); }
    }
    .status-error {
        background: rgba(239, 68, 68, 0.15);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }

    /* ── Results Section ── */
    .results-header {
        text-align: center;
        margin: 2rem 0 1rem;
    }
    .results-title {
        font-size: 1.6rem;
        font-weight: 700;
        background: linear-gradient(135deg, #34d399, #667eea);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }


    /* ── Transcript Expander ── */
    .transcript-box {
        background: rgba(15, 17, 28, 0.6);
        border: 1px solid rgba(102, 126, 234, 0.15);
        border-radius: 12px;
        padding: 1.2rem;
        font-size: 0.88rem;
        color: #d1d5db;
        line-height: 1.7;
        max-height: 350px;
        overflow-y: auto;
    }

    /* ── Metric Cards ── */
    .metrics-row {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
        flex-wrap: wrap;
    }
    .metric-card {
        flex: 1;
        min-width: 140px;
        background: rgba(30, 32, 48, 0.7);
        border: 1px solid rgba(102, 126, 234, 0.15);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .metric-label {
        font-size: 0.75rem;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 0.3rem;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem;
        color: #4b5563;
        font-size: 0.78rem;
        border-top: 1px solid rgba(102, 126, 234, 0.1);
        margin-top: 3rem;
    }
    .footer a { color: #667eea; text-decoration: none; }

    /* ── Hide default streamlit elements ── */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ── File uploader styling ── */
    [data-testid="stFileUploader"] {
        border: 2px dashed rgba(102, 126, 234, 0.3);
        border-radius: 16px;
        padding: 1rem;
        transition: border-color 0.3s;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: rgba(102, 126, 234, 0.6);
    }
</style>
"""
