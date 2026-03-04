import streamlit as st
from Sections import pinwheel

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

/* Grey background */
.stApp {
    background-color: #dcdcdc;
}

/* Top navigation bar */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #555;
    display: flex;
    align-items: center;
    padding-left: 40px;
    height: 55px;
    z-index: 9999;
}

/* Menu links */
.navbar a {
    color: white;
    text-decoration: none;
    margin-right: 40px;
    font-size: 14px;
    transition: all 0.2s ease;
}

/* Hover amplify */
.navbar a:hover {
    font-size: 16px;
}

/* Push content below navbar */
.page-content {
    margin-top: 70px;
    padding: 40px;
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
        with st.form("login_form"):
            username = st.text_input("", placeholder="User", label_visibility="collapsed")
            password = st.text_input("", type="password", placeholder="Password", label_visibility="collapsed")
            submitted = st.form_submit_button("Login", use_container_width=True)

            if submitted:
                if username == "veep" and password == "fi2026":
                    st.session_state.authenticated = True
                    st.rerun()


# ---------------------------------------------------
# NAVIGATION BAR
# ---------------------------------------------------
def render_navbar():

    st.markdown("""
    <div class="navbar">
        <a href="?page=overview">Overview</a>
        <a href="?page=pinwheel">Pinwheel</a>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------
# MAIN APP
# ---------------------------------------------------
def main_app():

    render_navbar()

    # routing
    page = st.query_params.get("page", "overview")

    st.markdown('<div class="page-content">', unsafe_allow_html=True)

    if page == "overview":
        st.title("FI Overview")

    elif page == "pinwheel":
        pinwheel.render()

    else:
        st.title("FI Overview")

    st.markdown('</div>', unsafe_allow_html=True)


# ---------------------------------------------------
# ROUTER
# ---------------------------------------------------
if not st.session_state.authenticated:
    login_screen()
else:
    main_app()
