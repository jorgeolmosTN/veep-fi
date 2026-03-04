import streamlit as st
from Sections import pinwheel

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(layout="wide")

# ---------------------------------------------------
# SESSION STATE INIT
# ---------------------------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "page" not in st.session_state:
    st.session_state.page = "overview"


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

/* Menu buttons */
.nav-btn {
    color: white;
    background: none;
    border: none;
    margin-right: 40px;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.nav-btn:hover {
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
                    st.session_state.page = "overview"
                    st.rerun()


# ---------------------------------------------------
# NAVIGATION BAR (NO QUERY PARAMS)
# ---------------------------------------------------
def render_navbar():

    st.markdown("""
    <div class="navbar">
        <form method="post">
            <button class="nav-btn" name="nav" value="overview">Overview</button>
            <button class="nav-btn" name="nav" value="pinwheel">Pinwheel</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

    # Capture navigation
    if "nav" in st.session_state:
        st.session_state.page = st.session_state.nav


# ---------------------------------------------------
# MAIN APP
# ---------------------------------------------------
def main_app():

    render_navbar()

    st.markdown('<div class="page-content">', unsafe_allow_html=True)

    if st.session_state.page == "overview":
        st.title("FI Overview")

    elif st.session_state.page == "pinwheel":
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
