import streamlit as st
import streamlit.components.v1 as components

def render():

    # =================================================
    # GLOBAL STYLE
    # =================================================
    st.markdown("""
        <style>
        .main-container {
            padding-left: 60px;
            padding-right: 60px;
        }
        h1 { font-size: 28px !important; }
        h2 { font-size: 18px !important; margin-top: 40px; }
        p  { font-size: 14px !important; margin:0; }

        .card {
            padding:20px;
            border-radius:14px;
            color:white;
            min-height:140px;
        }

        .icon {
            font-size:28px;
            margin-bottom:10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # =================================================
    # TITLE
    # =================================================
    st.markdown("<h1>Pinwheel Integration</h1>", unsafe_allow_html=True)

    # =================================================
    # WHAT SECTION
    # =================================================
    st.markdown("<h2>What</h2>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
            <div class="card" style="background:#4F46E5;">
                <div class="icon">🔐</div>
                <strong>Secure Payroll</strong>
                <p>User connects payroll provider securely via Pinwheel SDK.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card" style="background:#7C3AED;">
                <div class="icon">📊</div>
                <strong>Income Data</strong>
                <p>Verified employment & income data retrieved.</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="card" style="background:#059669;">
                <div class="icon">🧠</div>
                <strong>Model Activation</strong>
                <p>Updates model status and eligibility tier.</p>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div class="card" style="background:#D97706;">
                <div class="icon">⚡</div>
                <strong>FI Enablement</strong>
                <p>Unlocks Anytime Pay functionality securely.</p>
            </div>
        """, unsafe_allow_html=True)

    # =================================================
    # FLOW SECTION
    # =================================================
    st.markdown("<h2>Flow</h2>", unsafe_allow_html=True)

    components.html(
        """
        <div style="
            display:flex;
            justify-content:center;
            margin-top:20px;
        ">
            <div style="
                width:75%;
                border:1px solid #e5e7eb;
                border-radius:14px;
                padding:20px;
                background:white;
            ">
                <img src="https://lucid.app/publicSegments/view/e9f65060-fa9b-4f37-90bd-be8142decf57/image.png"
                     style="width:100%; height:auto; border-radius:8px;">
            </div>
        </div>
        """,
        height=650,
    )

    st.markdown(
        """
        <div style="text-align:center; margin-top:20px;">
            <a href="https://lucid.app/lucidchart/f5415687-d638-421f-8213-caa6d62a88c0/view"
               target="_blank"
               style="
                    padding:8px 16px;
                    background:#111827;
                    color:white;
                    border-radius:6px;
                    text-decoration:none;
                    font-size:13px;">
               Open Full Flow in Lucid
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =================================================
    # TECHNICAL DIAGRAM
    # =================================================
    st.markdown("<h2>Technical Diagram</h2>", unsafe_allow_html=True)

    components.html(
        """
        <div style="
            border:1px solid #e5e7eb;
            border-radius:14px;
            padding:25px;
            background:white;
            display:flex;
            justify-content:center;
            gap:30px;
            flex-wrap:wrap;
        ">
            <div>👤 User</div>
            <div>→</div>
            <div>💻 FI Frontend</div>
            <div>→</div>
            <div>🔗 Pinwheel SDK</div>
            <div>→</div>
            <div>⚙️ Veep Backend</div>
            <div>→</div>
            <div>🧠 ModelShop</div>
        </div>

        <div style="text-align:center; margin-top:15px; font-size:12px; color:gray;">
        Widget token → Backend exchange → Payroll data → Model update → Eligibility refresh
        </div>
        """,
        height=240,
    )

    st.markdown('</div>', unsafe_allow_html=True)
