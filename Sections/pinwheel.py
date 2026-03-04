import streamlit as st
import streamlit.components.v1 as components

def render():

    # =================================================
    # PAGE CONFIG (smaller typography)
    # =================================================
    st.markdown("""
        <style>
        h1 { font-size: 32px !important; }
        h2 { font-size: 22px !important; }
        h3 { font-size: 18px !important; }
        p  { font-size: 14px !important; }
        </style>
    """, unsafe_allow_html=True)

    # =================================================
    # TITLE
    # =================================================
    st.markdown("<h1>Pinwheel Integration</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # =================================================
    # COLORFUL INFO CARDS
    # =================================================
    st.markdown("<h2>What is this integration for?</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    card_style = """
        <div style="
            padding:20px;
            border-radius:12px;
            color:white;
            min-height:140px;
        ">
    """

    with col1:
        st.markdown(card_style.replace(">", " background-color:#4A90E2;'>") +
            "<h3>🔐 Secure Payroll</h3>"
            "<p>Users securely connect their payroll provider via the Pinwheel widget.</p>"
            "</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(card_style.replace(">", " background-color:#7B61FF;'>") +
            "<h3>📊 Income Data</h3>"
            "<p>Verified income & employment data is retrieved for eligibility validation.</p>"
            "</div>", unsafe_allow_html=True)

    with col3:
        st.markdown(card_style.replace(">", " background-color:#00B894;'>") +
            "<h3>🧠 Model Update</h3>"
            "<p>Model status and tier are updated after user interaction.</p>"
            "</div>", unsafe_allow_html=True)

    st.markdown("---")

    # =================================================
    # USER FLOW
    # =================================================
    st.markdown("<h2>Pinwheel User Flow</h2>", unsafe_allow_html=True)

    components.iframe(
    "https://lucid.app/lucidchart/f5415687-d638-421f-8213-caa6d62a88c0/view",
    height=900,
    scrolling=True
)

    st.markdown("---")

    # =================================================
    # CORRECT TECHNICAL ARCHITECTURE
    # =================================================
    st.markdown("<h2>Pinwheel Architecture – Technical Diagram</h2>", unsafe_allow_html=True)

    components.html(
        """
        <div style="display:flex; justify-content:center; align-items:center; gap:25px; flex-wrap:wrap; margin-top:30px;">

            <div style="padding:15px 25px; border-radius:10px; background:#f1f3f6;">
                👤 User
            </div>

            <div>➡️</div>

            <div style="padding:15px 25px; border-radius:10px; background:#e3f2fd;">
                💻 FI Frontend
            </div>

            <div>➡️</div>

            <div style="padding:15px 25px; border-radius:10px; background:#ede7f6;">
                🔗 Pinwheel SDK / Widget
            </div>

            <div>➡️</div>

            <div style="padding:15px 25px; border-radius:10px; background:#fff3e0;">
                ⚙️ Veep Backend
            </div>

            <div>➡️</div>

            <div style="padding:15px 25px; border-radius:10px; background:#e8f5e9;">
                🧠 ModelShop
            </div>

        </div>

        <div style="text-align:center; margin-top:30px; font-size:13px; color:gray;">
            Data Flow: Widget token → Backend exchange → Payroll data → Model eligibility update → FE refresh
        </div>
        """,
        height=250,
    )
