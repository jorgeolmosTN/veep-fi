import streamlit as st
import streamlit.components.v1 as components


def render():

    # =================================================
    # GLOBAL STYLE (cleaner typography)
    # =================================================
    st.markdown("""
        <style>
        h1 { font-size: 30px !important; }
        h2 { font-size: 20px !important; margin-bottom: 10px; }
        h3 { font-size: 16px !important; }
        p  { font-size: 14px !important; }
        </style>
    """, unsafe_allow_html=True)

    # =================================================
    # PAGE TITLE
    # =================================================
    st.markdown("<h1>Pinwheel Integration</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # =================================================
    # INFO CARDS
    # =================================================
    st.markdown("<h2>What is this integration for?</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    card_base = """
        <div style="
            padding:18px;
            border-radius:12px;
            color:white;
            min-height:130px;
        ">
    """

    with col1:
        st.markdown(
            card_base.replace(">", " background-color:#4A90E2;'>") +
            "<h3>🔐 Secure Payroll</h3>"
            "<p>Users connect their payroll provider securely using the Pinwheel widget.</p>"
            "</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            card_base.replace(">", " background-color:#7B61FF;'>") +
            "<h3>📊 Income Verification</h3>"
            "<p>Verified income & employment data is retrieved to support eligibility logic.</p>"
            "</div>",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            card_base.replace(">", " background-color:#00B894;'>") +
            "<h3>🧠 Model Activation</h3>"
            "<p>User interaction updates Model status (Opted-In) and adjusts tier if required.</p>"
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown("---")

    # =================================================
    # USER FLOW SECTION
    # =================================================
    st.markdown("<h2>Pinwheel User Flow</h2>", unsafe_allow_html=True)

    st.image(
        "https://lucid.app/publicSegments/view/c49e1371-91bf-4804-8725-ef9f29bf5614/image.png",
        use_container_width=True
    )

    st.markdown(
        """
        <div style="text-align:center; margin-top:20px;">
            <a href="https://lucid.app/lucidchart/f5415687-d638-421f-8213-caa6d62a88c0/view"
               target="_blank"
               style="
                    display:inline-block;
                    padding:10px 22px;
                    background-color:#4A90E2;
                    color:white;
                    font-size:14px;
                    border-radius:8px;
                    text-decoration:none;
                    font-weight:500;
               ">
               🔎 Open Interactive Flow in Lucid
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # =================================================
    # TECHNICAL ARCHITECTURE SECTION
    # =================================================
    st.markdown("<h2>Pinwheel Architecture – Technical Diagram</h2>", unsafe_allow_html=True)

    components.html(
        """
        <div style="display:flex; justify-content:center; align-items:center; gap:20px; flex-wrap:wrap; margin-top:25px;">

            <div style="padding:12px 20px; border-radius:10px; background:#f1f3f6;">
                👤 User
            </div>

            <div>➡️</div>

            <div style="padding:12px 20px; border-radius:10px; background:#e3f2fd;">
                💻 FI Frontend
            </div>

            <div>➡️</div>

            <div style="padding:12px 20px; border-radius:10px; background:#ede7f6;">
                🔗 Pinwheel Widget (SDK)
            </div>

            <div>➡️</div>

            <div style="padding:12px 20px; border-radius:10px; background:#fff3e0;">
                ⚙️ Veep Backend
            </div>

            <div>➡️</div>

            <div style="padding:12px 20px; border-radius:10px; background:#e8f5e9;">
                🧠 ModelShop
            </div>

        </div>

        <div style="text-align:center; margin-top:25px; font-size:13px; color:gray;">
            Flow: User → Frontend → Pinwheel Widget → Backend (token exchange) → ModelShop → Backend → Frontend eligibility refresh
        </div>
        """,
        height=260,
    )
