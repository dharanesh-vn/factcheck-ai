import streamlit as st
import sys
import os

# ---------------------------------------------------------
# Local Model Integration
# ---------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, '..', 'src')
if src_path not in sys.path:
    sys.path.append(src_path)

try:
    from predict import predict_news
except ImportError:
    def predict_news(text): return "ERROR"

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="FactCheck AI",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    html, body, .stApp { background-color: #f8f9fc !important; }
    header, #MainMenu, footer { visibility: hidden; }
    .block-container { padding-top: 0 !important; padding-bottom: 2rem !important; }

    /* ── Navbar wrapper ── */
    .topbar {
        background: #ffffff;
        border-bottom: 1px solid #e5e7eb;
        height: 64px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 8px;
        margin-bottom: 36px;
    }
    .topbar-brand {
        font-size: 1.2rem;
        font-weight: 700;
        color: #6C48C5;
        letter-spacing: -0.02em;
    }

    /* ── Nav buttons: make them ghost/link-style ── */
    div[data-testid="column"] .stButton > button {
        background: transparent !important;
        color: #6b7280 !important;
        border: none !important;
        box-shadow: none !important;
        padding: 6px 14px !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        border-radius: 6px !important;
        margin-top: 0 !important;
        width: auto !important;
    }

    div[data-testid="column"] .stButton > button:hover {
        background: #f3f4f6 !important;
        color: #6C48C5 !important;
    }

    /* Active nav button */
    .active-tab .stButton > button {
        background: #f3f4f6 !important;
        color: #6C48C5 !important;
    }

    /* ── Typography ── */
    h2 {
        font-size: 2.25rem !important;
        font-weight: 800 !important;
        color: #1a1a1a !important;
        text-align: center;
        letter-spacing: -0.04em;
        margin-bottom: 4px !important;
    }
    .sub-text {
        text-align: center;
        color: #6b7280;
        font-size: 1rem;
        margin-bottom: 32px;
    }

    /* ── Card ── */
    .fc-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 36px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .fc-label {
        font-size: 0.875rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 10px;
        display: block;
    }

    /* ── Textarea ── */
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #1a1a1a !important;
        -webkit-text-fill-color: #1a1a1a !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 8px !important;
        padding: 14px !important;
        font-size: 1rem !important;
    }
    .stTextArea textarea::placeholder {
        color: #9ca3af !important;
        opacity: 1 !important;
    }

    /* ── Execute Button ONLY (full-width purple) ── */
    .exec-btn .stButton > button {
        background-color: #6C48C5 !important;
        color: #ffffff !important;
        width: auto !important;
        padding: 10px 28px !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        margin-top: 14px !important;
    }
    .exec-btn .stButton > button:hover {
        background-color: #5a3aad !important;
    }

    /* ── Result boxes ── */
    .result {
        margin-top: 28px;
        padding: 22px;
        border-radius: 10px;
        text-align: center;
    }
    .result-title { font-size: 1.2rem; font-weight: 700; margin-bottom: 4px; }
    .result-desc  { font-size: 0.875rem; }
    .res-real { background:#ecfdf5; border:1px solid #10b981; color:#064e3b; }
    .res-fake { background:#fef2f2; border:1px solid #ef4444; color:#7f1d1d; }

    /* ── Registry table ── */
    .reg-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 0;
        border-bottom: 1px solid #f3f4f6;
    }
    .reg-row:last-child { border-bottom: none; }
    .reg-k { font-size:0.72rem; color:#6b7280; text-transform:uppercase; font-weight:600; letter-spacing:0.05em; }
    .reg-v { font-size:0.95rem; font-weight:500; color:#1a1a1a; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Session State
# ---------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "AI"

# ---------------------------------------------------------
# Navbar  (HTML brand + st.button nav links)
# ---------------------------------------------------------
st.markdown('<div class="topbar"><span class="topbar-brand">FactCheck AI</span></div>', unsafe_allow_html=True)

# Place nav buttons in a row flush with the right
_, nav1_col, nav2_col = st.columns([6, 1, 1.2])

with nav1_col:
    a_class = "active-tab" if st.session_state.page == "AI" else ""
    st.markdown(f'<div class="{a_class}">', unsafe_allow_html=True)
    if st.button("AI", key="nav_ai"):
        st.session_state.page = "AI"
    st.markdown("</div>", unsafe_allow_html=True)

with nav2_col:
    i_class = "active-tab" if st.session_state.page == "About" else ""
    st.markdown(f'<div class="{i_class}">', unsafe_allow_html=True)
    if st.button("About", key="nav_about"):
        st.session_state.page = "About"
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# AI Page
# ---------------------------------------------------------
if st.session_state.page == "AI":
    st.markdown("<h2>Linguistic Analysis</h2>", unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Proprietary cloud engine for factual verification.</p>', unsafe_allow_html=True)

    st.markdown('<div class="fc-card"><span class="fc-label">Article Content</span>', unsafe_allow_html=True)
    user_text = st.text_area("_", placeholder="Input the text volume for verification...",
                              label_visibility="collapsed", height=200)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="exec-btn">', unsafe_allow_html=True)
    run = st.button("Execute Verification", key="exec")
    st.markdown("</div>", unsafe_allow_html=True)

    if run:
        if user_text.strip():
            with st.spinner("Analyzing..."):
                result = predict_news(user_text)
            if result == "REAL":
                st.markdown("""
                <div class="result res-real">
                    <div class="result-title">AUTHENTIC CONTENT</div>
                    <div class="result-desc">Linguistic patterns align with factual reporting standards.</div>
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="result res-fake">
                    <div class="result-title">FABRICATED CONTENT</div>
                    <div class="result-desc">Linguistic indicators suggest sensationalism or misinformation.</div>
                </div>""", unsafe_allow_html=True)
        else:
            st.warning("Please provide input text for analysis.")

# ---------------------------------------------------------
# About Page
# ---------------------------------------------------------
elif st.session_state.page == "About":
    st.markdown("<h2>Project Registry</h2>", unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Academic documentation and institutional details.</p>', unsafe_allow_html=True)

    rows = [
        ("Organization",    "Mobile and Cloud Application Lab"),
        ("Subject Code",    "22MDC65"),
        ("Research Lead",   "Dhanushya E (2303717673722009)"),
        ("Research Lead",   "Dharanesh VN (2303717673721010)"),
        ("Supervision",     "Dr. Savithri V, Dr. Chandia S, Dr. Kamatchi A"),
    ]

    st.markdown('<div class="fc-card">', unsafe_allow_html=True)
    for k, v in rows:
        st.markdown(f"""
        <div class="reg-row">
            <span class="reg-k">{k}</span>
            <span class="reg-v">{v}</span>
        </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)