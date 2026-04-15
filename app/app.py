import streamlit as st
import requests
import os

# Page Configuration
st.set_page_config(page_title="FactCheck AI | Cloud Dashboard", layout="wide", initial_sidebar_state="collapsed")

# API Configuration
API_URL = "http://factcheck-prod.eba-shmkjjex.us-east-1.elasticbeanstalk.com/predict"

# Custom CSS for Professional Lavender Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Navbar */
    .stApp { background-color: #f5f0fb; }
    
    header[data-testid="stHeader"] { display: none !important; }

    .navbar {
        background-color: #6C48C5;
        padding: 16px 40px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2rem;
    }

    .brand {
        font-size: 24px;
        font-weight: 600;
        letter-spacing: -0.02em;
    }

    /* Main Container */
    .main-body {
        max-width: 800px;
        margin: 0 auto;
        padding: 0 20px;
    }

    .card {
        background: white;
        padding: 40px;
        border-radius: 14px;
        border: 1px solid #e2d8f5;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }

    /* Input Area */
    .stTextArea textarea {
        border: 1.5px solid #d5c8f0 !important;
        background-color: #faf8ff !important;
        border-radius: 10px !important;
        font-size: 16px !important;
    }

    /* Buttons */
    .stButton > button {
        background-color: #6C48C5 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 12px 28px !important;
        font-weight: 600 !important;
        border: none !important;
        width: 100% !important;
    }

    .nav-btn > button {
        width: auto !important;
        background: rgba(255,255,255,0.18) !important;
        border: 1.5px solid rgba(255,255,255,0.4) !important;
        font-size: 14px !important;
        padding: 4px 16px !important;
    }

    /* Results */
    .result-box {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-weight: 600;
        margin-top: 20px;
        font-size: 18px;
    }
    .real { background-color: #edf8f1; color: #1b6e3b; border: 1.5px solid #74c69d; }
    .fake { background-color: #fef0f0; color: #a42020; border: 1.5px solid #e86b6b; }
</style>
""", unsafe_allow_html=True)

# Session State for Navigation
if 'page' not in st.session_state:
    st.session_state.page = 'AI'

# Top Bar
st.markdown('<div class="navbar"><span class="brand">FactCheck AI</span></div>', unsafe_allow_html=True)

# Navigation Buttons at the top right (using Streamlit columns)
t_col1, t_col2 = st.columns([6, 1])
with t_col2:
    n_col1, n_col2 = st.columns(2)
    with n_col1:
        if st.button("AI", key="ai_nav"):
            st.session_state.page = 'AI'
    with n_col2:
        if st.button("About", key="about_nav"):
            st.session_state.page = 'About'

# Page Rendering
if st.session_state.page == 'AI':
    st.markdown("<div class='main-body'>", unsafe_allow_html=True)
    st.markdown("<h1>Linguistic Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#666;'>Cloud-based verified content verification</p>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        user_input = st.text_area("Input Content", label_visibility="collapsed", placeholder="Paste news content here for factual verification...", height=250)
        
        if st.button("Analyze Content", type="primary"):
            if user_input.strip():
                with st.spinner("Calling Cloud API..."):
                    try:
                        response = requests.post(API_URL, json={"text": user_input})
                        data = response.json()
                        
                        if data.get("prediction") == "REAL":
                            st.markdown('<div class="result-box real">Verification Successful — Content Appears Authentic</div>', unsafe_allow_html=True)
                        else:
                            st.markdown('<div class="result-box fake">Verification Failed — Content may be Fabricated</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error("Error connecting to the API. Ensure your Elastic Beanstalk service is running.")
            else:
                st.warning("Please provide content to analyze.")
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == 'About':
    st.markdown("<div class='main-body'>", unsafe_allow_html=True)
    st.markdown("<h1>Project Registry</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        details = [
            ("Student", "Dhanushya E"),
            ("Register No.", "2303717673722009"),
            ("Student", "Dharanesh VN"),
            ("Register No.", "2303717673721010"),
            ("Subject", "Mobile and Cloud Application Development Lab (22MDC65)"),
            ("Supervision", "Dr. Savithri V, Dr. Chandia S, Dr. Kamatchi A")
        ]
        
        for k, v in details:
            st.markdown(f"""
            <div style='padding: 15px 0; border-bottom: 1px solid #e2d8f5;'>
                <div style='font-size: 12px; color: #9a8ec2; text-transform: uppercase;'>{k}</div>
                <div style='font-size: 18px; font-weight: 500;'>{v}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)