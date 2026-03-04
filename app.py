import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="VEEP FI",
    layout="wide",
)

# ---------------------------------------------------
# SESSION STATE INIT
# ---------------------------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ---------------------------------------------------
# LOGIN FUNCTION
# ---------------------------------------------------
def login_screen():

    st.markdown("""
    <style>

    /* Remove Streamlit UI */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    .block-container {padding: 0 !important;}

    /* Full page gradient */
    .login-bg {
        height: 100vh;
        background: linear-gradient(135deg, #e6e6e6, #cfcfcf);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Login box */
    .login-box {
        background: rgba(255,255,255,0.6);
        padding: 60px 50px;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        width: 320px;
        text-align: center;
    }

    /* Input styling */
    div[data-baseweb="input"] > div {
        border-radius: 8px !important;
        border: 1px solid #aaa !important;
        background-color: white !important;
    }

    input {
        text-align: center;
        font-size: 14px !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        background-color: black;
        color: white;
        border: none;
        padding: 10px;
        font-size: 14px;
    }

    .stButton > button:hover {
        background-color: #333;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-bg">', unsafe_allow_html=True)
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    username = st.text_input("", key="username")
    password = st.text_input("", type="password", key="password")

    if st.button("Enter"):
        if username == "veep" and password == "fi2026":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------
# MAIN APP (AFTER LOGIN)
# ---------------------------------------------------
def main_app():

    st.markdown("""
    <style>
    .block-container {
        padding-top: 0rem !important;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

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

    with tabs[1]:
        st.title("EWA Request Flow")

    with tabs[2]:
        st.title("Eligibility & Model")

    with tabs[3]:
        st.title("Advance Creation")

    with tabs[4]:
        st.title("Pinwheel Integration")

    with tabs[5]:
        st.title("Connective (Kinective)")

    with tabs[6]:
        st.title("Q2 Widget")

    with tabs[7]:
        st.title("Nudge Integration")

    with tabs[8]:
        st.title("Repayment – No Funds")

    with tabs[9]:
        st.title("Repayment – Uncollectable")

    with tabs[10]:
        st.title("Employer Not Found")

    with tabs[11]:
        st.title("Full FI Architecture")


# ---------------------------------------------------
# ROUTER
# ---------------------------------------------------
if not st.session_state.authenticated:
    login_screen()
else:
    main_app()
