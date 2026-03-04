import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="VEEP FI Flows",
    layout="wide",
)

# ---------------------------------------------------
# REMOVE STREAMLIT HEADER / FOOTER / PADDING
# ---------------------------------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    padding-left: 1.5rem;
    padding-right: 1.5rem;
}

header {visibility: hidden;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}

/* Remove extra top spacing */
div[data-testid="stVerticalBlock"] > div:first-child {
    margin-top: 0rem !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TOP NAVIGATION (CLOUD SAFE)
# ---------------------------------------------------
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

# ---------------------------------------------------
# TAB CONTENT
# ---------------------------------------------------
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
