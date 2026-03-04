import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------
# RENDER FUNCTION (REQUIRED BY app.py)
# ---------------------------------------------------
def render():

    st.set_page_config(layout="wide")

    # =================================================
    # PAGE TITLE
    # =================================================
    st.title("Pinwheel Integration")

    st.markdown("---")

    # =================================================
    # INTRO WIDGET SECTION
    # =================================================
    st.subheader("What is this integration for?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🔐 Secure Payroll Connection")
        st.write(
            "Allows FI members to securely connect their payroll provider "
            "using the Pinwheel widget."
        )

    with col2:
        st.markdown("### 📊 Income & Employment Data")
        st.write(
            "Retrieves verified income and employment data to support "
            "eligibility and decisioning models."
        )

    with col3:
        st.markdown("### 🧠 Model Enablement")
        st.write(
            "Triggers model status updates (Opted-In, Tier changes) "
            "after user interaction with the widget."
        )

    st.markdown("---")

    # =================================================
    # USER FLOW SECTION
    # =================================================
    st.subheader("Pinwheel User Flow")

    st.markdown(
        """
        This diagram represents the end-to-end user journey when a member 
        chooses to connect payroll via Pinwheel.
        """
    )

    # Smaller framed image
    components.html(
        """
        <div style="
            border:1px solid #ccc;
            border-radius:10px;
            padding:10px;
            width:80%;
            margin:auto;
            background-color:white;">
            <img src="https://lucid.app/publicSegments/view/c49e1371-91bf-4804-8725-ef9f29bf5614/image.png" 
                 style="width:100%; border-radius:8px;">
        </div>
        """,
        height=600,
    )

    st.markdown("---")

    # =================================================
    # ARCHITECTURE TECHNICAL DIAGRAM
    # =================================================
    st.subheader("Pinwheel Architecture – Technical Diagram")

    st.markdown(
        """
        Below is the technical architecture representing how Pinwheel 
        interacts with Frontend, Backend, and Model components.
        """
    )

    # Simple clean architecture visual (HTML block diagram)
    components.html(
        """
        <div style="display:flex; justify-content:center; gap:40px; margin-top:30px;">

            <div style="text-align:center;">
                <div style="padding:20px; border:1px solid #ccc; border-radius:10px;">
                    👤<br><strong>User</strong>
                </div>
            </div>

            <div style="text-align:center;">
                <div style="padding:20px; border:1px solid #ccc; border-radius:10px;">
                    💻<br><strong>Frontend (FI App)</strong>
                </div>
            </div>

            <div style="text-align:center;">
                <div style="padding:20px; border:1px solid #ccc; border-radius:10px;">
                    🔗<br><strong>Pinwheel Widget</strong>
                </div>
            </div>

            <div style="text-align:center;">
                <div style="padding:20px; border:1px solid #ccc; border-radius:10px;">
                    ⚙️<br><strong>Backend (Veep)</strong>
                </div>
            </div>

            <div style="text-align:center;">
                <div style="padding:20px; border:1px solid #ccc; border-radius:10px;">
                    🧠<br><strong>ModelShop</strong>
                </div>
            </div>

        </div>

        <div style="text-align:center; margin-top:40px; font-size:14px; color:gray;">
            Flow: User → Frontend → Pinwheel → Backend → ModelShop → Backend → Frontend
        </div>
        """,
        height=300,
    )
