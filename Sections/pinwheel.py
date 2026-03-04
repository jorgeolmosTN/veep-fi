import streamlit as st
import streamlit.components.v1 as components


def render():

    # --------------------------------------------------
    # PAGE LAYOUT CONTROL
    # --------------------------------------------------
    st.markdown("""
    <style>
    .block-container {
        padding-left: 4rem !important;
        padding-right: 4rem !important;
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }

    h1 { margin-bottom: 12px !important; }
    h3 { margin-top: 8px !important; margin-bottom: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

    st.title("Pinwheel Integration")

    # =====================================================
    # INFO CARD WITH DESCRIPTIONS
    # =====================================================
    st.markdown("""
    <div style="
        border:1px solid #e5e5e5;
        border-radius:10px;
        padding:20px;
        margin-bottom:18px;
        background:#ffffff;
    ">
        <div style="font-weight:600; margin-bottom:14px; font-size:15px;">
            What Pinwheel Enables
        </div>

        <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:16px; font-size:13px;">

            <div>
                <div>🏢 <b>Employer Verification</b></div>
                <div style="color:#555;">Confirms active payroll relationship</div>
            </div>

            <div>
                <div>💰 <b>Income Validation</b></div>
                <div style="color:#555;">Retrieves verified compensation data</div>
            </div>

            <div>
                <div>🧩 <b>Member Enrichment</b></div>
                <div style="color:#555;">Updates internal profile attributes</div>
            </div>

            <div>
                <div>🏦 <b>Destination Account</b></div>
                <div style="color:#555;">Creates verified payout account</div>
            </div>

            <div>
                <div>📊 <b>Eligibility Refresh</b></div>
                <div style="color:#555;">Triggers Model recalculation</div>
            </div>

            <div>
                <div>⚠️ <b>Risk Tier Adjustment</b></div>
                <div style="color:#555;">Applied on early widget exit</div>
            </div>

        </div>
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # HAPPY PATH FLOW
    # =====================================================
    st.markdown("### 1. User Flow — Happy Path")

    happy_flow = """
flowchart LR
    classDef user fill:#e0f2fe,stroke:#0284c7,color:#075985;
    classDef process fill:#f3f4f6,stroke:#6b7280,color:#111827;
    classDef final fill:#dcfce7,stroke:#16a34a,color:#14532d;

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

    render_mermaid(happy_flow)

    # =====================================================
    # EXIT FLOW
    # =====================================================
    st.markdown("### 2. Exit Anytime Flow — Risk Impact")

    exit_flow = """
flowchart LR
    classDef user fill:#e0f2fe,stroke:#0284c7,color:#075985;
    classDef process fill:#f3f4f6,stroke:#6b7280,color:#111827;
    classDef risk fill:#fee2e2,stroke:#dc2626,color:#7f1d1d;

    User((User)):::user
    FE["Veep FE"]:::process
    Widget["Pinwheel Widget"]:::process
    Exit["Exit Anytime"]:::process
    Dashboard["Return to Dashboard"]:::process
    Tier["Tier Reduction in Risk Score"]:::risk

    User --> FE --> Widget --> Exit --> Dashboard --> Tier
"""

    render_mermaid(exit_flow)

    # =====================================================
    # SEQUENCE DIAGRAM (CLEAN THEME)
    # =====================================================
    st.markdown("### 3. Pinwheel Integration — Sequence Diagram")

    sequence = """
sequenceDiagram
    participant User
    participant FE as Veep FE
    participant BE as Veep Backend
    participant PW as Pinwheel
    participant Model

    User->>FE: Open EWA
    FE->>PW: Launch Widget

    alt Happy Path
        User->>PW: Select Employer
        PW-->>FE: Return Income + Employer Data
        FE->>BE: Send Payroll Data
        BE->>BE: Member Enrichment
        BE->>BE: Create Destination Account
        BE->>Model: Trigger Eligibility Refresh
        Model-->>BE: Eligibility Updated
        BE-->>FE: Eligibility Confirmed
    else Employer Not Found
        PW-->>FE: Employer Not Found
    else Exit Anytime
        User->>FE: Exit Pinwheel
        FE->>BE: Flag Early Exit
        BE->>Model: Apply Tier Reduction
    end
"""

    render_mermaid(sequence)


# --------------------------------------------------
# CLEAN MERMAID RENDERER
# --------------------------------------------------
def render_mermaid(code: str):

    components.html(
        f"""
        <style>
        .frame {{
            border:1px solid #e5e5e5;
            border-radius:10px;
            padding:18px;
            background:#ffffff;
            margin-bottom:18px;
        }}
        </style>

        <div class="frame">
            <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
            <div class="mermaid">
            %%{{init: {{ 'theme': 'base', 'themeVariables': {{
                'primaryColor': '#f3f4f6',
                'primaryBorderColor': '#6b7280',
                'primaryTextColor': '#111827',
                'lineColor': '#374151',
                'fontSize': '13px'
            }} }} }}%%
            {code}
            </div>
        </div>

        <script>
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        height=420,
        scrolling=False
    )
