import streamlit as st
import streamlit.components.v1 as components


# ---------------------------------------------------
# INIT STATE
# ---------------------------------------------------
if "pinwheel_view" not in st.session_state:
    st.session_state.pinwheel_view = "flow1"


# ---------------------------------------------------
# NAVIGATION (FLOW SELECTOR)
# ---------------------------------------------------
def render_navigation():

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Flow 1 – Opt In Journey", use_container_width=True):
            st.session_state.pinwheel_view = "flow1"

    with col2:
        if st.button("Flow 2 – Future State", use_container_width=True):
            st.session_state.pinwheel_view = "flow2"

    with col3:
        if st.button("Edge Cases", use_container_width=True):
            st.session_state.pinwheel_view = "edge"


# ---------------------------------------------------
# EMBED DIAGRAM
# ---------------------------------------------------
def embed_lucid_chart(embed_url):
    components.iframe(
        embed_url,
        height=900,
        scrolling=True
    )


# ---------------------------------------------------
# MAIN RENDER
# ---------------------------------------------------
def render():

    st.title("Pinwheel Integration – Visual Flows")

    render_navigation()

    st.markdown("---")

    # 🔵 FLOW 1
    if st.session_state.pinwheel_view == "flow1":
        st.subheader("Flow 1 – Pinwheel Opt-In Journey")

        embed_lucid_chart(
            "PASTE_YOUR_EMBED_LINK_HERE"
        )

    # 🟢 FLOW 2
    elif st.session_state.pinwheel_view == "flow2":
        st.subheader("Flow 2 – Future / Alternative Flow")

        embed_lucid_chart(
            "PASTE_FLOW2_EMBED_LINK_HERE"
        )

    # 🟡 EDGE CASES
    elif st.session_state.pinwheel_view == "edge":
        st.subheader("Edge Cases & Error Handling")

        embed_lucid_chart(
            "PASTE_EDGE_CASE_EMBED_LINK_HERE"
        )
