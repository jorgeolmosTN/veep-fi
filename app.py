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

/* Tight spacing between inputs */
div[data-testid="stTextInput"] {
    margin-bottom: 8px !important;
}

/* Remove password eye icon */
button[kind="secondary"] {
    display: none !important;
}
button[aria-label] {
    display: none !important;
}

/* Remove red focus outline and replace with dark grey */
div[data-baseweb="input"] > div {
    border: 1px solid #555 !important;
}

div[data-baseweb="input"] > div:focus-within {
    border: 1px solid #333 !important;
    box-shadow: none !important;
}

/* Remove red error glow */
input:focus {
    outline: none !important;
    box-shadow: none !important;
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
        with st.form("login_form", clear_on_submit=False):

            username = st.text_input(
                "",
                placeholder="User",
                label_visibility="collapsed"
            )

            password = st.text_input(
                "",
                type="password",
                placeholder="Password",
                label_visibility="collapsed"
            )

            submitted = st.form_submit_button("Login", use_container_width=True)

            if submitted:
                if username == "veep" and password == "fi2026":
                    st.session_state.authenticated = True
                    st.rerun()


# ---------------------------------------------------
# MAIN APP (MENU RESTORED)
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
        st.write("High-level architecture and scope summary.")

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
