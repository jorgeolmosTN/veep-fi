import streamlit as st
import streamlit.components.v1 as components


def render():

    st.title("Pinwheel Integration")

    st.markdown("""
Pinwheel enables payroll connectivity and verified income validation
required for FI eligibility and EWA disbursement.

It supports:
- Employer verification
- Income validation
- Member enrichment
- Destination account creation
- Eligibility recalculation
- Risk-tier adjustments on early exit
""")

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

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

    render_boxed_mermaid(user_flow, height=380)

    st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

    # =====================================================
    # 2️⃣ EXIT ANYTIME FLOW — RISK IMPACT
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

    render_boxed_mermaid(exit_flow, height=300)

    st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

    # =====================================================
    # 3️⃣ SEQUENCE DIAGRAM — ENTERPRISE VIEW
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
        FE->>BE: Send verified payroll data
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
        FE-->>U: Return to EWA Dashboard
        FE->>BE: Flag Early Exit
        BE->>M: Apply Tier Reduction
        M-->>BE: Risk Tier Updated
    end
"""

    render_boxed_mermaid(sequence_diagram, height=550)


# =====================================================
# PROFESSIONAL BOXED MERMAID RENDERER
# =====================================================
def render_boxed_mermaid(code: str, height: int = 400):
    components.html(
        f"""
<style>
.diagram-box {{
    background-color: #f8f8f8;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 5px;
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
