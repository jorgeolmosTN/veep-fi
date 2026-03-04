import streamlit as st
import streamlit.components.v1 as components


def render():

    # --------------------------------------------------
    # COMPACT GLOBAL STYLE
    # --------------------------------------------------
    st.markdown("""
    <style>
    .block-container {
        padding-left: 4rem !important;
        padding-right: 4rem !important;
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }

    h1 { margin-bottom: 10px !important; }
    h3 { margin-top: 6px !important; margin-bottom: 6px !important; }

    .section-frame {
        border: 1px solid #dcdcdc;
        border-radius: 10px;
        padding: 16px 20px;
        margin-bottom: 12px;
        background-color: #ffffff;
    }

    .diagram-box {
        border: 1px solid #e5e5e5;
        border-radius: 8px;
        padding: 12px;
        background-color: #fafafa;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("Pinwheel Integration")

    # =====================================================
    # INFO CARD
    # =====================================================
    st.markdown("""
    <div class="section-frame">
        <div style="font-size:15px; font-weight:600; margin-bottom:8px;">
            What Pinwheel Enables
        </div>
        <div style="display:flex; gap:28px; flex-wrap:wrap; font-size:13px;">
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
    # 1️⃣ USER FLOW — HAPPY PATH
    # =====================================================
    st.markdown('<div class="section-frame">', unsafe_allow_html=True)
    st.markdown("### 1. User Flow — Happy Path")

    user_flow = """
flowchart LR

    classDef user fill:#dbeafe,stroke:#2563eb,stroke-width:1px,color:#1e3a8a;
    classDef process fill:#f3f4f6,stroke:#6b7280,stroke-width:1px,color:#111827;
    classDef final fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#14532d;

    User((User)):::user
    FE["Veep FE"]:::process
    Widget["Pinwheel Widget"]:::process
    Employer["Select Employer"]:::process
    Auth["Authenticate Payroll"]:::process
    Income["Income Verified"]:::process
    Linked["Account Linked"]:::process
    Eligible["Eligibility Recalculated"]:::final

    User --> FE --> Widget --> Employer --> Auth --> Income --> Linked --> Eligible
"""

    render_mermaid(user_flow, 300)
    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # 2️⃣ EXIT ANYTIME FLOW — FIXED SEQUENCE
    # =====================================================
    st.markdown('<div class="section-frame">', unsafe_allow_html=True)
    st.markdown("### 2. Exit Anytime Flow — Risk Impact")

    exit_flow = """
flowchart LR

    classDef user fill:#dbeafe,stroke:#2563eb,stroke-width:1px,color:#1e3a8a;
    classDef process fill:#f3f4f6,stroke:#6b7280,stroke-width:1px,color:#111827;
    classDef risk fill:#fee2e2,stroke:#dc2626,stroke-width:1px,color:#7f1d1d;

    User((User)):::user
    FE["Veep FE"]:::process
    Widget["Pinwheel Widget"]:::process
    Exit["Exit Anytime"]:::process
    Dashboard["Return to Dashboard"]:::process
    Tier["Tier Reduction in Risk Score"]:::risk

    User --> FE --> Widget --> Exit --> Dashboard --> Tier
"""

    render_mermaid(exit_flow, 260)
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

    render_mermaid(sequence_diagram, 380)
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
        scrolling=False,
    )
