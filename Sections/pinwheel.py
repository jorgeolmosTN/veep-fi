import streamlit as st
import streamlit.components.v1 as components


def render():

    # --------------------------------------------------
    # GLOBAL PAGE COMPACT STYLING
    # --------------------------------------------------
    st.markdown("""
    <style>
    .block-container {
        padding-left: 4rem !important;
        padding-right: 4rem !important;
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }

    h3 {
        margin-top: 8px !important;
        margin-bottom: 8px !important;
    }

    p {
        margin-bottom: 6px !important;
    }

    .section-frame {
        border: 1px solid #dcdcdc;
        border-radius: 10px;
        padding: 18px 22px;
        margin-bottom: 14px;
        background-color: #ffffff;
    }

    .diagram-box {
        border: 1px solid #e5e5e5;
        border-radius: 8px;
        padding: 12px;
        background-color: #fafafa;
        margin-top: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("Pinwheel Integration")

    # =====================================================
    # TOP INFO CARD
    # =====================================================
    st.markdown("""
    <div class="section-frame">
        <div style="font-size:16px; font-weight:600; margin-bottom:8px;">
            What Pinwheel Enables
        </div>
        <div style="display:flex; gap:30px; flex-wrap:wrap; font-size:14px;">
            <div>🏢 Employer Verification</div>
            <div>💰 Income Validation</div>
            <div>🧩 Member Enrichment</div>
            <div>🏦 Destination Account Creation</div>
            <div>📊 Eligibility Recalculation</div>
            <div>⚠️ Risk Tier Adjustment</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # 1️⃣ USER FLOW
    # =====================================================
    st.markdown('<div class="section-frame">', unsafe_allow_html=True)
    st.markdown("### 1. User Flow — Happy Path")

    user_flow = """
flowchart LR
    User((User)) --> FE["Veep FE"]
    FE --> Widget["Pinwheel Widget"]
    Widget --> Employer["Select Employer"]
    Employer --> Auth["Authenticate Payroll"]
    Auth --> Income["Income Verified"]
    Income --> Linked["Account Linked"]
    Linked --> Eligible["Eligibility Recalculated"]
"""

    render_mermaid(user_flow, height=300)
    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # 2️⃣ EXIT FLOW
    # =====================================================
    st.markdown('<div class="section-frame">', unsafe_allow_html=True)
    st.markdown("### 2. Exit Anytime Flow — Risk Impact")

    exit_flow = """
flowchart LR
    User((User)) --> Widget["Pinwheel Widget"]
    Widget --> Exit["Exit Anytime"]
    Exit --> Dashboard["Return to Dashboard"]
    Dashboard --> Tier["Tier Reduction in Risk Score"]
"""

    render_mermaid(exit_flow, height=240)
    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # 3️⃣ SEQUENCE DIAGRAM
    # =====================================================
    st.markdown('<div class="section-frame">', unsafe_allow_html=True)
    st.markdown("### 3. Pinwheel Integration — Sequence Diagram")

    sequence_diagram = """
sequenceDiagram
    participant U as User
    participant FE as Veep FE
    participant BE as Veep Backend
    participant PW as Pinwheel
    participant M as ModelShop

    U->>FE: Open EWA
    FE->>PW: Launch Widget

    alt Happy Path
        U->>PW: Select Employer
        PW-->>FE: Return Income + Employer Data
        FE->>BE: Send Payroll Data
        BE->>BE: Member Enrichment
        BE->>BE: Create Destination Account
        BE->>M: Trigger Eligibility Refresh
        M-->>BE: Eligibility Updated
        BE-->>FE: Eligibility Confirmed
    else Employer Not Found
        PW-->>FE: Employer Not Found
    else Exit Anytime
        U->>FE: Exit Pinwheel
        FE->>BE: Flag Early Exit
        BE->>M: Apply Tier Reduction
    end
"""

    render_mermaid(sequence_diagram, height=420)
    st.markdown('</div>', unsafe_allow_html=True)


# --------------------------------------------------
# MERMAID RENDERER
# --------------------------------------------------
def render_mermaid(code: str, height: int):
    components.html(
        f"""
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<div class="diagram-box">
<div class="mermaid">
{code}
</div>
</div>
<script>
mermaid.initialize({{ startOnLoad: true }});
</script>
        """,
        height=height,
    )
