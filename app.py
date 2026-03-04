import streamlit as st

st.set_page_config(layout="wide")

# Hide default Streamlit elements
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

nav_html = """
<style>
.navbar {
    overflow: hidden;
    background-color: #111;
    font-family: Arial, sans-serif;
}

.navbar a {
    float: left;
    font-size: 14px;
    color: white;
    text-align: center;
    padding: 14px 20px;
    text-decoration: none;
}

.dropdown {
    float: left;
    overflow: hidden;
}

.dropdown .dropbtn {
    font-size: 14px;
    border: none;
    outline: none;
    color: white;
    padding: 14px 20px;
    background-color: inherit;
    margin: 0;
    cursor: pointer;
}

.navbar a:hover, .dropdown:hover .dropbtn {
    background-color: #222;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #1c1c1c;
    min-width: 200px;
    z-index: 1;
}

.dropdown-content a {
    float: none;
    color: white;
    padding: 12px 16px;
    display: block;
    text-align: left;
}

.dropdown-content a:hover {
    background-color: #333;
}

.dropdown:hover .dropdown-content {
    display: block;
}
</style>

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
      <a href="?page=connective">Connective</a>
      <a href="?page=q2">Q2 Widget</a>
      <a href="?page=nudge">Nudge</a>
    </div>
  </div>

  <div class="dropdown">
    <button class="dropbtn">Edge Cases</button>
    <div class="dropdown-content">
      <a href="?page=repayment_no_funds">Repayment – No Funds</a>
      <a href="?page=repayment_uncollectable">Repayment – Uncollectable</a>
      <a href="?page=employer_missing">Employer Not Found</a>
    </div>
  </div>

  <a href="?page=architecture">Full Architecture</a>
</div>
"""
st.markdown(nav_html, unsafe_allow_html=True)

query_params = st.query_params
page = query_params.get("page", "overview")

if page == "overview":
    st.title("FI Overview")
elif page == "ewa":
    st.title("EWA Request Flow")
elif page == "pinwheel":
    st.title("Pinwheel Integration")
# etc...

