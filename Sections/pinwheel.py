import streamlit as st


# ---------------------------------------------------
# INIT STATE
# ---------------------------------------------------
if "pinwheel_step" not in st.session_state:
    st.session_state.pinwheel_step = "question"

if "model_status" not in st.session_state:
    st.session_state.model_status = "Not Opted In"

if "model_tier" not in st.session_state:
    st.session_state.model_tier = "Standard"


# ---------------------------------------------------
# RENDER FUNCTION
# ---------------------------------------------------
def render():

    # ---------------------------
    # STEP 1: QUESTION STAGE
    # ---------------------------
    if st.session_state.pinwheel_step == "question":

        st.title("Connect Payroll with Pinwheel")

        st.write("Would you like to connect your payroll provider?")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Do Not Request", use_container_width=True):
                # Direct return to dashboard
                st.session_state.page = "overview"
                st.session_state.pinwheel_step = "question"
                st.rerun()

        with col2:
            if st.button("Request Pinwheel", use_container_width=True):
                st.session_state.pinwheel_step = "widget"
                st.rerun()

    # ---------------------------
    # STEP 2: PINWHEEL WIDGET
    # ---------------------------
    elif st.session_state.pinwheel_step == "widget":

        st.title("Pinwheel Widget")

        st.info("🔐 Pinwheel payroll connection flow would render here.")

        st.write("User can complete connection or exit anytime.")

        if st.button("Exit Anytime", use_container_width=True):
            st.session_state.pinwheel_step = "exit"
            st.rerun()

    # ---------------------------
    # STEP 3: EXIT ANYTIME LOGIC
    # ---------------------------
    elif st.session_state.pinwheel_step == "exit":

        st.title("Processing Model Update")

        # Simulate model update
        st.session_state.model_status = "Opted In"
        st.session_state.model_tier = "Lower Tier"

        st.success("Model updated successfully.")

        st.write("Model Status:", st.session_state.model_status)
        st.write("Model Tier:", st.session_state.model_tier)

        if st.button("Return to Dashboard", use_container_width=True):
            st.session_state.pinwheel_step = "question"
            st.session_state.page = "overview"
            st.rerun()
