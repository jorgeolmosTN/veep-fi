import streamlit as st
import streamlit.components.v1 as components


def render():

    # -----------------------------------
    # PAGE PADDING (Left / Right)
    # -----------------------------------
    st.markdown("""
    <style>
    .block-container {
        padding-left: 4rem !important;
        padding-right: 4rem !important;
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("Pinwheel Integration")

    # =====================================================
    # TOP EXPLANATION CARD (Graphical)
    # =====================================================

    st.markdown("""
    <div style="
        background:#f7f7f7;
        border:1px solid #e5e5e5;
        border-radius:10px;
        padding:20px 25px;
        margin-top:10px;
        margin-bottom:20px;
    ">
        <div style="font-size:16px; font-weight:600; margin-bottom:12px;">
            What Pinwheel Enables
        </div>
        <div style="display:flex; gap:40px; flex-wrap:wrap; font-size:14px;">
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

    st.markdown("### 1. User Flow — Happy Path")

    user_flow = """
flowchart LR

    classDef main fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#111;
    classDef neutral fill:#e8eef7,stroke:#335,stroke-width:1px,color:#112;

    User((User)):::neutral
    FE["Veep FE"]:::main
    Widget["Pinwheel Widget"]:::main
    Employer["Select Employer"]:::main
    Auth["Authenticate Payroll"]:::main
    Income["Income Verified"]:::main
    Linked["Account Linked"]:::main
    Eligible["Eligibility Recalculated"]:::neutral

    User --> FE --> Widget --> Employer --> Auth --> Income --> Linked --> Eligible
"""

    render_boxed_mermaid(user_flow, height=340)

    # Minimal spacing
    st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

    # =====================================================
    # 2️⃣ EXIT ANYTIME FLOW
    # =====================================================

    st.markdown("### 2. Exit Anytime Flow — Risk Impact")

    exit_flow = """
flowchart LR

    classDef neutral fill:#e8eef7,stroke:#335,stroke-width:1px,color:#112;
    classDef main fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#111;
    classDef risk fill:#ffe6e6,stroke:#a33,stroke-width:1px,color:#600;

    User((User)):::neutral
    Widget["Pinwheel Widget"]:::main
    Exit["Exit Anytime"]:::main
    Dashboard["Return to EWA Dashboard"]:::main
    Tier["Tier Reduction in Risk Score"]:::risk

    User --> Widget --> Exit --> Dashboard --> Tier
"""

    render_boxed_mermaid(exit_flow, height=260)

    st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

    # =====================================================
    # 3️⃣ SEQUENCE DIAGRAM
    # =====================================================

    st.markdown("### 3. Pinwheel Integration — Sequence Diagram")

    sequence_diagram = """
sequenceDiagram
    participant U as User
    participant FE as Veep FE
    participant BE as Veep Backend
    participant PW as Pinwheel
    participant M as ModelShop

    U->>FE: Open EWA
    FE->>PW: Launch Pinwheel Widget

    alt Happy Path
        U->>PW: Select Employer
        PW->>PW: Authenticate Payroll
        PW->>FE: Return Income + Employer Data
        FE->>BE: Send Verified Payroll Data
        BE->>BE: Member Enrichment
        BE->>BE: Create Destination Account
        BE->>M: Trigger Eligibility Refresh
        M-->>BE: Eligibility Updated
        BE-->>FE: Eligibility Confirmed
        FE-->>U: Updated EWA Dashboard
    else Employer Not Found
        PW-->>FE: Employer Not Found
        FE-->>U: Display Phase 2 Handling
    else Exit Anytime
        U->>FE: Exit Pinwheel
        FE-->>U: Return to Dashboard
        FE->>BE: Flag Early Exit
        BE->>M: Apply Tier Reduction
        M-->>BE: Risk Tier Updated
    end
"""

    render_boxed_mermaid(sequence_diagram, height=500)


# =====================================================
# PROFESSIONAL MERMAID BOX
# =====================================================
def render_boxed_mermaid(code: str, height: int = 350):
    components.html(
        f"""
<style>
.diagram-box {{
    background-color:#fafafa;
    border:1px solid #e6e6e6;
    border-radius:8px;
    padding:18px;
    margin:0;
}}
</style>

<div class="diagram-box">
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
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
