import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="VEEP FI Flows",
    layout="wide",
)

# ---------------------------------------------------
# REMOVE ALL STREAMLIT UI / SPACING
# ---------------------------------------------------
st.markdown(
    """
    <style>
    .block-container {
        padding: 0rem !important;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}

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

    .navbar a, .dropbtn {
        color: white;
        padding: 18px 24px;
        text-decoration: none;
        font-size: 14px;
        background: none;
        border: none;
        cursor: pointer;
    }

    .navbar a:hover, .dropdown:hover .dropbtn {
        background-color: #222;
    }

    .dropdown {
        position: relative;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #1c1c1c;
        min-width: 240px;
        top: 54px;
    }

    .dropdown-content a {
        display: block;
        padding: 14px 18px;
        color: white;
    }

    .dropdown-content a:hover {
        background-color: #333;
    }

    .dropdown:hover .dropdown-content {
        display: block;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# NAVBAR HTML
# ---------------------------------------------------
st.markdown(
    """
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
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# PUSH CONTENT BELOW NAVBAR
# ---------------------------------------------------
st.markdown("<div style='margin-top:70px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------
# ROUTING
# ---------------------------------------------------
page = st.query_params.get("page", "overview")

if page == "overview":
    st.title("FI Overview")
    st.write("High-level architecture and flow summary.")

elif page == "ewa":
    st.title("EWA Request Flow")

elif page == "eligibility":
    st.title("Eligibility & Model")

elif page == "advance":
    st.title("Advance Creation")

elif page == "pinwheel":
    st.title("Pinwheel Integration")

elif page == "connective":
    st.title("Connective (Kinective)")

elif page == "q2":
    st.title("Q2 Widget")

elif page == "nudge":
    st.title("Nudge Integration")

elif page == "no_funds":
    st.title("Repayment – No Funds")

elif page == "uncollectable":
    st.title("Repayment – Uncollectable")

elif page == "employer_missing":
    st.title("Employer Not Found")

elif page == "architecture":
    st.title("Full FI Architecture")
