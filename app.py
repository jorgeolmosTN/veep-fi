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
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# LOGIN SCREEN
# ---------------------------------------------------
def login_screen():

    # Vertical spacing
    st.markdown("<div style='height:30vh'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3,2,3])

    with col2:
        username = st.text_input("", placeholder="User")
        password = st.text_input("", type="password", placeholder="Password")

        if st.button("Enter", use_container_width=True):
            if username == "veep" and password == "fi2026":
                st.session_state.authenticated = True
                st.rerun()


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
