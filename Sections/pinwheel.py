import streamlit as st

st.set_page_config(layout="wide")

# ---------------------------------------------------
# INIT STATE
# ---------------------------------------------------
if "pinwheel_view" not in st.session_state:
    st.session_state.pinwheel_view = "flow1"


# ---------------------------------------------------
# NAVIGATION
# ---------------------------------------------------
st.title("Pinwheel Integration – Visual Flows")

col1, col2 = st.columns(2)

with col1:
    if st.button("Flow 1 – Opt In Journey", use_container_width=True):
        st.session_state.pinwheel_view = "flow1"

with col2:
    if st.button("Future / Edge Cases", use_container_width=True):
        st.session_state.pinwheel_view = "future"

st.markdown("---")


# ---------------------------------------------------
# RENDER FLOWS
# ---------------------------------------------------
if st.session_state.pinwheel_view == "flow1":

    st.subheader("Flow 1 – Pinwheel Opt-In Journey")

    st.image(
        "https://lucid.app/publicSegments/view/c49e1371-91bf-4804-8725-ef9f29bf5614/image.png",
        use_container_width=True
    )

elif st.session_state.pinwheel_view == "future":

    st.subheader("Future / Alternative Flow")

    st.info("Upload or publish the second flow PNG and paste the URL here.")
