import streamlit as st
import base64

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
# LOAD IMAGE
# ---------------------------------------------------
def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64_image("assets/image_44a13a.png")


# ---------------------------------------------------
# LOGIN SCREEN
# ---------------------------------------------------
def login_screen():

    st.markdown(f"""
    <style>

    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    #MainMenu {{visibility: hidden;}}
    .block-container {{padding: 0 !important;}}

    /* Full screen background */
    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-position: center center;
        background-repeat: no-repeat;
        background-size: contain;   /* <<< FIXED */
        background-color: black;    /* fill empty space */
        height: 100vh;
    }}

    /* Bottom cinematic overlay */
    .overlay {{
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 35%;
        background: linear-gradient(to top, rgba(0,0,0,0.85), rgba(0,0,0,0));
        pointer-events: none;
    }}

    /* Bottom-right login container */
    .login-container {{
        position: fixed;
        bottom: 80px;
        right: 80px;
        width: 260px;
    }}

    /* Input styling */
    div[data-baseweb="input"] > div {{
        background: rgba(255,255,255,0.15) !important;
        border: none !important;
        border-radius: 6px !important;
        backdrop-filter: blur(6px);
    }}

    input {{
        color: white !important;
        font-size: 13px !important;
    }}

    input::placeholder {{
        color: rgba(255,255,255,0.7);
        letter-spacing: 2px;
        font-size: 11px;
    }}

    button[aria-label="Show password"] {{
        background: transparent !important;
        color: white !important;
    }}

    .stButton > button {{
        display: none;
    }}

    </style>
    """, unsafe_allow_html=True)

    # Overlay layer
    st.markdown('<div class="overlay"></div>', unsafe_allow_html=True)

    # Login inputs
    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    username = st.text_input("", placeholder="USER", key="username")
    password = st.text_input("", placeholder="PASS", type="password", key="password")

    if st.button("Login"):
        if username == "veep" and password == "fi2026":
            st.session_state.authenticated = True
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# ---------------------------------------------------
# MAIN APP
# ---------------------------------------------------
def main_app():
    st.write("Logged in successfully.")


# ---------------------------------------------------
# ROUTER
# ---------------------------------------------------
if not st.session_state.authenticated:
    login_screen()
else:
    main_app()
