import streamlit as st
import sys
import os

# Set up paths
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '../src')
sys.path.append(src_dir)

from predict import predict_news

# Page Configuration
st.set_page_config(page_title="FactCheck AI", layout="wide", initial_sidebar_state="collapsed")

# Session State for Navigation
if 'page' not in st.session_state:
    st.session_state.page = 'AI'

# Custom CSS provided by User with Final Visibility Fixes
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        font-size: 16px;
    }

    /* Kill the default white gap at top */
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 2rem !important;
        max-width: 100% !important;
    }
    header[data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stToolbar"] { display: none !important; }

    .stApp { background-color: #f5f0fb; }

    /* ── Navbar ── */
    .navbar-wrap {
        background: #6C48C5;
        padding: 0 32px;
        height: 60px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }
    .brand-title {
        color: #ffffff;
        font-size: 24px;
        font-weight: 600;
        letter-spacing: -0.02em;
        line-height: 60px;
    }

    /* Target the nav buttons specifically */
    div[data-testid="stHorizontalBlock"] .stButton > button {
        background-color: rgba(255,255,255,0.18) !important;
        color: #ffffff !important;
        border: 1.5px solid rgba(255,255,255,0.55) !important;
        border-radius: 6px !important;
        padding: 4px 14px !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        height: 32px !important;
        min-height: 32px !important;
        line-height: 1 !important;
        margin-top: 14px; /* Align with brand title vertically */
    }
    div[data-testid="stHorizontalBlock"] .stButton > button:hover {
        background-color: rgba(255,255,255,0.32) !important;
        border-color: #ffffff !important;
    }

    /* Analyze button (primary) */
    .stButton > button[kind="primary"] {
        background-color: #6C48C5 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 11px 30px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        height: auto !important;
        min-height: 44px !important;
        margin-top: 14px !important;
    }
    .stButton > button[kind="primary"]:hover {
        background-color: #5a3aad !important;
    }

    /* ── Hero ── */
    .hero-section {
        background: linear-gradient(135deg, #6C48C5 0%, #8B5FD8 55%, #C68FE6 100%);
        padding: 40px 40px 32px;
    }
    .hero-section h1 {
        font-size: 32px !important;
        font-weight: 600 !important;
        letter-spacing: -0.03em !important;
        color: #fff !important;
        margin: 0 0 6px 0 !important;
    }
    .hero-subtitle {
        font-size: 15px;
        opacity: 0.82;
        color: #fff;
        margin-bottom: 22px;
    }
    .stats-row { display: flex; gap: 12px; flex-wrap: wrap; }
    .stat-pill {
        background: rgba(255,255,255,0.15);
        border: 1px solid rgba(255,255,255,0.25);
        border-radius: 8px;
        padding: 9px 18px;
        color: #fff;
        font-size: 13px;
        font-weight: 500;
    }
    .stat-pill b {
        display: block;
        font-size: 19px;
        font-weight: 600;
        color: #fff;
    }

    /* ── Page body ── */
    .page-body {
        max-width: 860px;
        margin: 28px auto;
        padding: 0 24px;
    }

    /* ── Card ── */
    .card {
        background: #ffffff;
        border-radius: 14px;
        border: 1px solid #e2d8f5;
        padding: 28px 30px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .card-label {
        font-size: 11px;
        font-weight: 600;
        color: #6C48C5;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        margin-bottom: 12px;
    }

    /* ── Textarea ── */
    .stTextArea textarea {
        border: 1.5px solid #d5c8f0 !important;
        background-color: #faf8ff !important;
        border-radius: 10px !important;
        font-size: 15px !important;
        padding: 14px 16px !important;
        min-height: 210px !important;
        color: #1F2937 !important;
        line-height: 1.6 !important;
    }
    .stTextArea textarea:focus {
        border-color: #6C48C5 !important;
        box-shadow: 0 0 0 3px rgba(108,72,197,0.1) !important;
    }

    /* ── Results ── */
    .result-real {
        background: #edf8f1;
        border: 1.5px solid #74c69d;
        border-radius: 10px;
        padding: 18px 20px;
        color: #1b6e3b;
        font-size: 15px;
        font-weight: 600;
        margin-top: 16px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .result-fake {
        background: #fef0f0;
        border: 1.5px solid #e86b6b;
        border-radius: 10px;
        padding: 18px 20px;
        color: #a42020;
        font-size: 15px;
        font-weight: 600;
        margin-top: 16px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* ── Info card ── */
    .info-card {
        background: #f0ebfc;
        border-radius: 14px;
        border-left: 4px solid #6C48C5;
        padding: 24px 26px;
    }
    .info-card h3 {
        font-size: 16px !important;
        font-weight: 600 !important;
        color: #3d2a8a !important;
        margin: 0 0 10px 0 !important;
    }
    .info-card p {
        font-size: 15px !important;
        color: #4a3880 !important;
        line-height: 1.7 !important;
        margin: 0 0 8px 0 !important;
    }
    .info-card p:last-child { margin-bottom: 0 !important; }
    .badge-inline {
        background: #6C48C5;
        color: #fff;
        border-radius: 4px;
        padding: 2px 8px;
        font-size: 13px;
        font-weight: 500;
    }

    /* ── About ── */
    .about-card {
        background: #fff;
        border-radius: 14px;
        border: 1px solid #e2d8f5;
        overflow: hidden;
    }
    .about-group {
        padding: 22px 30px;
        border-bottom: 1px solid #ede6f8;
    }
    .about-group:last-child { border-bottom: none; }
    .about-group-label {
        font-size: 11px;
        font-weight: 600;
        color: #9880cc;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 12px;
    }
    .about-entry {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
        padding: 5px 0;
    }
    .about-name {
        font-size: 16px;
        color: #1F2937;
        font-weight: 500;
    }
    .about-reg {
        font-size: 13px;
        color: #6C48C5;
        font-weight: 500;
        background: #f0ebfc;
        border-radius: 5px;
        padding: 3px 10px;
        font-family: 'SF Mono', 'Courier New', monospace;
        white-space: nowrap;
    }
    .about-value {
        font-size: 16px;
        color: #1F2937;
        font-weight: 500;
    }
    .about-code {
        font-size: 13px;
        color: #6C48C5;
        font-weight: 600;
        background: #f0ebfc;
        border-radius: 5px;
        padding: 3px 10px;
    }
    .about-staff-name {
        font-size: 15px;
        color: #374151;
        font-weight: 400;
        padding: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

# ── Navbar ─────────────────────────────────────────────────────────────
# Hack to make the navbar full-width and colorful
st.markdown('<div style="background-color:#6C48C5; width:100%; height:60px; position:absolute; top:0; left:0; z-index:0;"></div>', unsafe_allow_html=True)

nav_left, nav_right = st.columns([6, 1.5])
with nav_left:
    st.markdown('<span class="brand-title">FactCheck AI</span>', unsafe_allow_html=True)

with nav_right:
    btn_a, btn_b = st.columns(2)
    with btn_a:
        if st.button("AI", key="nav_btn_ai"):
            st.session_state.page = 'AI'
            st.rerun()
    with btn_b:
        if st.button("About", key="nav_btn_about"):
            st.session_state.page = 'About'
            st.rerun()

# ── AI Page ────────────────────────────────────────────────────────────
if st.session_state.page == 'AI':

    st.markdown("""
    <div class="hero-section">
        <h1>Linguistic Analysis</h1>
        <p class="hero-subtitle">Validate news content using cloud-native inference</p>
        <div class="stats-row">
            <div class="stat-pill"><b>44,800</b>Articles Trained</div>
            <div class="stat-pill"><b>99.5%</b>Accuracy</div>
            <div class="stat-pill"><b>PAC</b>Classifier</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='page-body'>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-label'>Analysis Input</div>", unsafe_allow_html=True)

    user_input = st.text_area(
        "Input Content",
        label_visibility="collapsed",
        placeholder="Paste news content here for factual verification…"
    )

    if st.button("Analyze Content", key="main_btn", type="primary"):
        if user_input.strip():
            with st.spinner("Accessing cloud node…"):
                result = predict_news(user_input)
                if result == "REAL":
                    st.markdown(
                        '<div class="result-real">'
                        '<svg width="18" height="18" viewBox="0 0 18 18" fill="none">'
                        '<circle cx="9" cy="9" r="9" fill="#2d9e5f"/>'
                        '<path d="M5 9.5l2.8 2.8 5-5.5" stroke="#fff" stroke-width="1.8" '
                        'stroke-linecap="round" stroke-linejoin="round"/>'
                        '</svg>'
                        'Verification Successful — Content appears authentic'
                        '</div>',
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        '<div class="result-fake">'
                        '<svg width="18" height="18" viewBox="0 0 18 18" fill="none">'
                        '<circle cx="9" cy="9" r="9" fill="#d44141"/>'
                        '<path d="M6 6l6 6M12 6l-6 6" stroke="#fff" stroke-width="1.8" '
                        'stroke-linecap="round"/>'
                        '</svg>'
                        'Verification Failed — Content may be fabricated'
                        '</div>',
                        unsafe_allow_html=True
                    )
        else:
            st.warning("Please provide valid content to analyze.")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <h3>How FactCheck AI Works</h3>
        <p>This engine utilizes a <span class="badge-inline">Passive Aggressive Classifier</span>
        trained on a high-fidelity dataset of <span class="badge-inline">44,800 news articles</span>.</p>
        <p>By analyzing linguistic patterns — lexical density, word choice, and tonal consistency —
        the system distinguishes verified factual reporting from sensationalist misinformation with
        <span class="badge-inline">99.5% precision</span>.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ── About Page ─────────────────────────────────────────────────────────
elif st.session_state.page == 'About':

    st.markdown("""
    <div class="hero-section" style="padding-bottom: 28px;">
        <h1>Project Registry</h1>
        <p class="hero-subtitle">Official coursework documentation and supervision</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='page-body'>", unsafe_allow_html=True)
    st.markdown("<div class='about-card'>", unsafe_allow_html=True)

    st.markdown("""
    <div class="about-group">
        <div class="about-group-label">Students</div>
        <div class="about-entry">
            <span class="about-name">Dhanushya E</span>
            <span class="about-reg">2303717673722009</span>
        </div>
        <div class="about-entry">
            <span class="about-name">Dharanesh VN</span>
            <span class="about-reg">2303717673721010</span>
        </div>
    </div>

    <div class="about-group">
        <div class="about-group-label">Subject</div>
        <div class="about-entry">
            <span class="about-value">Mobile and Cloud Application Development Lab</span>
            <span class="about-code">22MDC65</span>
        </div>
    </div>

    <div class="about-group">
        <div class="about-group-label">Staff In-Charge</div>
        <div class="about-staff-name">Dr. Savithri V</div>
        <div class="about-staff-name">Dr. Chandia S</div>
        <div class="about-staff-name">Dr. Kamatchi A</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)