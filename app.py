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
# GLOBAL STYLE (REMOVE STREAMLIT UI)
# ---------------------------------------------------
st.markdown("""
<style>
header {visibility: hidden;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
.block-container {padding: 0rem !important;}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# LOGIN SCREEN
# ---------------------------------------------------
def login_screen():

    # Full background gradient
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #e4e4e4, #c9c9c9);
    }

    /* Center container vertically */
    .center-container {
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Input styling */
    div[data-baseweb="input"] {
        max-width: 260px;
        margin: auto;
    }

    div[data-baseweb="input"] > div {
        border-radius: 6px !important;
        border: 1px solid #999 !important;
        background-color: white !important;
    }

    input {
        text-align: center;
        font-size: 13px !important;
    }

    /* Button styling */
    .stButton > button {
        width: 260px;
        border-radius: 6px;
        background-color: black;
        color: white;
        border: none;
        padding: 8px;
        font-size: 13px;
    }

    .stButton > button:hover {
        background-color: #222;
    }

    </style>
    """, unsafe_allow_html=True)

    # Use columns to center content
    left, center, right = st.columns([3,2,3])

    with center:
        st.markdown("<div style='height:25vh'></div>", unsafe_allow_html=True)

        username = st.text_input("", key="username")
        password = st.text_input("", type="password", key="password")

        if st.button("Enter"):
            if username == "veep" and password == "fi2026":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)


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
