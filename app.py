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
# GLOBAL STYLE
# ---------------------------------------------------
st.markdown("""
<style>
header {visibility: hidden;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
.block-container {padding: 0 !important;}

.stApp {
    background-color: #dcdcdc;
}

/* Remove extra spacing between inputs */
div[data-testid="stTextInput"] {
    margin-bottom: 8px !important;
}

/* Remove password eye icon completely */
button[kind="secondary"] {
    display: none !important;
}
button[aria-label] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOGIN SCREEN
# ---------------------------------------------------
def login_screen():

    st.markdown("<div style='height:32vh'></div>", unsafe_allow_html=True)

    left, center, right = st.columns([3,2,3])

    with center:
        username = st.text_input("", placeholder="User", label_visibility="collapsed")
        password = st.text_input("", type="password", placeholder="Password", label_visibility="collapsed")

        if st.button("Login", use_container_width=True):
            if username == "veep" and password == "fi2026":
                st.session_state.authenticated = True
                st.rerun()

# ---------------------------------------------------
# MAIN APP
# ---------------------------------------------------
def main_app():
    st.title("FI Overview")

# ---------------------------------------------------
# ROUTER
# ---------------------------------------------------
if not st.session_state.authenticated:
    login_screen()
else:
    main_app()
