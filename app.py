import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="VEEP FI Flows",
    layout="wide",
)

# ---------------------------------------------------
# REMOVE ALL STREAMLIT SPACING / UI
# ---------------------------------------------------
st.markdown("""
<style>

/* Remove default Streamlit padding */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
}

/* Remove header, footer, menu */
header {visibility: hidden;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}

/* Remove top spacing completely */
div[data-testid="stVerticalBlock"] > div:first-child {
    margin-top: 0rem !important;
}

/* NAVBAR */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #111;
    display: flex;
    align-items: center;
    font-family: Arial, sans-serif;
    z-index: 9999;
}

/* Main links */
.navbar a, .dropbtn {
    color: white;
    padding: 18px 24px;
    text-decoration: none;
    font-size: 14px;
    background: none;
    border: none;
    cursor: pointer;
}

/* Hover effect */
.navbar a:hover, .dropdown:hover .dropbtn {
    background-color: #222;
}

/* Dropdown container */
.dropdown {
    position: relative;
}

/* Dropdown content */
.dropdown-content {
    display: none;
    position: absolute;
    background-color: #1c1c1c;
    min-width: 240px;
    top: 54px;
}

/* Dropdown items */
.dropdown-content a {
    display: block;
    padding: 14px 18px;
    color: white;
}

/* Hover inside dropdown */
.dropdown-content a:hover {
    background-color: #333;
}

/* Show dropdown on hover */
.dropdown:hover .dropdown-content {
    display: block;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# NAVIGATION BAR
# ---------------------------------------------------
st.markdown("""
<div class="navbar">

    <a href="?page=overview">Overview</a>

    <div class="dropdown">
        <button class="dropbtn">Core Flows</button>
        <div class="dropdown-content">
            <a href="?page=ewa">EWA Request</a>
            <a href="?page=eligibility">Eligibility & Model</a>
            <a href="?page=advance">Advance Creation</a>
        </div>
    </div>

    <div class="dropdown">
        <button class="dropbtn">Integrations</button>
        <div class="dropdown-content">
            <a href="?page=pinwheel">Pinwheel</a>
            <a href="?page=connective">Connective (Kinective)</a>
            <a href="?page=q2">Q2 Widget</a>
            <a href="?page=nudge">Nudge</a>
        </div>
    </div>

    <div class="dropdown">
        <button class="dropbtn">Edge Cases</button>
        <div class="dropdown-content">
            <a href="?page=no_funds">Repayment – No Funds</a>
            <a href="?page=uncollectable">Repayment – Uncollectable</a>
            <a href="?page=employer_missing">Employer Not Found</a>
        </div>
    </div>

    <a href="?page=architecture">Full Architecture</a>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# PUSH CONTENT BELOW FIXED NAVBAR
# ---------------------------------------------------
st.markdown("<div style='margin-top:70px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------
# PAGE ROUTING
# ---------------------------------------------------
page = st.query_params.get("page", "overview")

if page == "overview":
    st.title("FI Overview")
    st.write("High-level Financial Institution architecture and flow summary.")

elif page == "ewa":
    st.title("EWA Request Flow")
    st.write("User → FE → BFF → Model → Advance Creation → Connective → Response")

elif page == "eligibility":
    st.title("Eligibility & Model")
    st.write("ModelShop eligibility evaluation and contract definition.")

elif page == "advance":
    st.title("Advance Creation")
    st.write("Advance lifecycle and ledger interaction.")

elif page == "pinwheel":
    st.title("Pinwheel Integration")
    st.write("Employer verification, income validation, destination account flow.")

elif page == "connective":
    st.title("Connective (Kinective)")
    st.write("Transaction ingestion and banking abstraction layer.")

elif page == "q2":
    st.title("Q2 Widget")
    st.write("Widget visibility rules and eligibility gating.")

elif page == "nudge":
    st.title("Nudge Integration")
    st.write("Token-based SSO and contextual financial education access.")

elif page == "no_funds":
    st.title("Repayment – No Funds")
    st.write("ACH return scenario and retry logic.")

elif page == "uncollectable":
    st.title("Repayment – Uncollectable")
    st.write("Max retry exceeded, write-off logic, eligibility impact.")

elif page == "employer_missing":
    st.title("Employer Not Found (Pinwheel)")
    st.write("Edge case handling and Phase 2 considerations.")

elif page == "architecture":
    st.title("Full FI Architecture")
    st.write("End-to-end architecture diagram including FE, BE, Model, Connective, Q2, Pinwheel.")

else:
    st.title("Page Not Found")
