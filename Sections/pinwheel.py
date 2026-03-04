import streamlit as st
import streamlit.components.v1 as components

def render():

    # =================================================
    # GLOBAL STYLE (minimal, clean)
    # =================================================
    st.markdown("""
        <style>
        h1 { font-size: 28px !important; }
        h2 { font-size: 18px !important; margin-top: 30px; }
        p  { font-size: 14px !important; color:#444; }
        .card {
            padding:18px;
            border-radius:10px;
            background:#f7f9fc;
            border:1px solid #e5e7eb;
            min-height:120px;
        }
        </style>
    """, unsafe_allow_html=True)

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
            <div class="card">
            <strong>Secure Payroll</strong>
            <p>User connects payroll provider via Pinwheel SDK.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card">
            <strong>Income Data</strong>
            <p>Verified employment & income information retrieved.</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="card">
            <strong>Eligibility Trigger</strong>
            <p>Connection updates model status and eligibility tier.</p>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div class="card">
            <strong>FI Enablement</strong>
            <p>Allows Anytime Pay to be activated securely.</p>
            </div>
        """, unsafe_allow_html=True)

    # =================================================
    # FLOW SECTION
    # =================================================
    st.markdown("<h2>Flow</h2>", unsafe_allow_html=True)

    st.image(
        "https://lucid.app/publicSegments/view/c49e1371-91bf-4804-8725-ef9f29bf5614/image.png",
        use_container_width=True
    )

    st.markdown(
        """
        <div style="margin-top:15px;">
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
    # TECHNICAL DIAGRAM SECTION
    # =================================================
    st.markdown("<h2>Technical Diagram</h2>", unsafe_allow_html=True)

    components.html(
        """
        <div style="
            border:1px solid #e5e7eb;
            border-radius:10px;
            padding:20px;
            background:white;
            display:flex;
            justify-content:center;
            gap:25px;
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
        height=220,
    )
