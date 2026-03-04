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
        pinwheel.render()
