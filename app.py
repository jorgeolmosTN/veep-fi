import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(layout="wide")

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ---------------------------------------------------
# GLOBAL RESET
# ---------------------------------------------------
st.markdown("""
<style>
header {visibility: hidden;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
.block-container {padding: 0 !important;}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# LOGIN SCREEN
# ---------------------------------------------------
def login_screen():

    st.markdown("""
    <style>

    /* Premium soft gradient background */
    .stApp {
        background: radial-gradient(circle at top left, #f2f2f2, #d9d9d9);
        height: 100vh;
    }

    /* Center container */
    .login-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    /* Glass card */
    .login-card {
        width: 320px;
        padding: 50px 40px;
        border-radius: 14px;
        background: rgba(255,255,255,0.55);
        backdrop-filter: blur(18px);
    }

    /* Remove default input styling */
    div[data-baseweb="input"] {
        margin-bottom: 28px;
    }

    div[data-baseweb="input"] > div {
        border: none !important;
        border-bottom: 1px solid #aaa !important;
        border-radius: 0 !important;
        background: transparent !important;
        transition: all 0.3s ease;
    }

    div[data-baseweb="input"] > div:focus-within {
        border-bottom: 1px solid black !important;
    }

    input {
        background: transparent !important;
        text-align: center;
        font-size: 14px !important;
        padding: 6px !important;
    }

    /* Hide password reveal icon background */
    button[aria-label="Show password"] {
        background: transparent !important;
    }

    /* Hide button completely (we'll still use it logically) */
    .stButton > button {
        display: none;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-wrapper"><div class="login-card">', unsafe_allow_html=True)

    username = st.text_input("", key="username")
    password = st.text_input("", type="password", key="password")

    # Hidden button for Enter trigger
    if st.button("Login"):
        if username == "veep" and password == "fi2026":
            st.session_state.authenticated = True
            st.rerun()

    st.markdown('</div></div>', unsafe_allow_html=True)


# ---------------------------------------------------
# MAIN APP
# ---------------------------------------------------
def main_app():

    tabs = st.tabs([
        "Overview",
        "EWA Request",
        "Eligibility",
        "Advance Creation",
        "Pinwheel",
        "Connective",
        "Q2",
        "Nudge",
        "Repayment – No Funds",
        "Repayment – Uncollectable",
        "Employer Missing",
        "Full Architecture"
    ])

    with tabs[0]:
        st.title("FI Overview")


# ---------------------------------------------------
# ROUTER
# ---------------------------------------------------
if not st.session_state.authenticated:
    login_screen()
else:
    main_app()
