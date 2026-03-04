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

div[data-testid="stTextInput"] {
    margin-bottom: 8px !important;
}

button[kind="secondary"] {
    display: none !important;
}
button[aria-label] {
    display: none !important;
}

div[data-baseweb="input"] > div {
    border: 1px solid #555 !important;
}

div[data-baseweb="input"] > div:focus-within {
    border: 1px solid #333 !important;
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

            username = st.text_input("", placeholder="User", label_visibility="collapsed")
            password = st.text_input("", type="password", placeholder="Password", label_visibility="collapsed")

            submitted = st.form_submit_button("Login", use_container_width=True)

            if submitted:
                if username == "veep" and password == "fi2026":
                    st.session_state.authenticated = True
                    st.rerun()


# ---------------------------------------------------
# PINWHEEL DIAGRAM FUNCTION
# ---------------------------------------------------
def render_pinwheel_diagram():

    st.subheader("Pinwheel Integration Flow")

    mermaid_code = """
    flowchart LR

        User --> FE["Veep FE"]
        FE --> PW_Widget["Pinwheel Widget"]
        PW_Widget --> PW_API["Pinwheel API"]

        PW_API --> BE["Veep Backend"]

        BE --> Enrich["Member Enrichment"]
        Enrich --> Dest["Create Destination Account"]

        Dest --> Model["ModelShop Eligibility Refresh"]
        Model --> FE

        PW_API -->|Employer Not Found| Edge["Edge Case Handling (Phase 2)"]
    """

    st.markdown(
        f"""
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <div class="mermaid">
        {mermaid_code}
        </div>
        <script>
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("### Flow Explanation")

    st.markdown("""
    **1. User initiates account linking in FE**  
    → Pinwheel widget loads.

    **2. Pinwheel verifies employer & income**  
    → Returns structured payroll data.

    **3. Backend receives Pinwheel payload**  
    → Member enrichment logic executes.

    **4. Destination account created**  
    → Account stored for EWA disbursement.

    **5. Eligibility refresh triggered in ModelShop**  
    → Updated offer availability.

    **6. Edge Case: Employer Not Found**  
    → Phase 2 decision logic required.
    """)


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

    with tabs[4]:
        render_pinwheel_diagram()


# ---------------------------------------------------
# ROUTER
# ---------------------------------------------------
if not st.session_state.authenticated:
    login_screen()
else:
    main_app()
