import streamlit as st
import streamlit.components.v1 as components


def render():

    # --------------------------------------------------
    # PAGE SPACING CONTROL (VERY TIGHT TOP)
    # --------------------------------------------------
    st.markdown("""
    <style>
    .block-container {
        padding-top: 0.05rem !important;
        padding-bottom: 0.2rem !important;
        padding-left: 4rem !important;
        padding-right: 4rem !important;
    }

    h2 {
        margin-top: 0px !important;
        margin-bottom: 6px !important;
        font-size: 38px;
        font-weight: 700;
    }

    h3 {
        margin-top: 12px !important;
        margin-bottom: 4px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2>Pinwheel Integration</h2>", unsafe_allow_html=True)

    # =====================================================
    # USER FLOW (UPDATED WITH DECISION + MULTI PATHS)
    # =====================================================
    st.markdown("### 1. User Flow — Decision Based")

    user_flow = """
flowchart LR

    classDef userStage fill:#f3f4f6,stroke:#6b7280,color:#111827;
    classDef decision fill:#fff7ed,stroke:#ea580c,color:#7c2d12;
    classDef final fill:#fee2e2,stroke:#dc2626,color:#7f1d1d;
    classDef model fill:#ede9fe,stroke:#7c3aed,color:#4c1d95;

    Access["Access to Veep"]:::userStage
    BE["Veep BE"]:::userStage
    Decision{"Employer Verification Status?"}:::decision

    Pinwheel["Pinwheel Widget"]:::userStage
    Select["Select Employer"]:::userStage
    Auth["Auth Payroll"]:::userStage
    Income["Income Verification"]:::userStage
    Linked["Account Linked"]:::userStage
    Return["Return to Dashboard"]:::userStage

    Advance["Advance Availability Status"]:::final
    ModelStatus["Model Status: Do Not Request Pinwheel"]:::model

    Access --> BE
    BE --> Decision

    Decision -- "Request Pinwheel" --> Pinwheel
    Decision -- "Do Not Request" --> ModelStatus

    Pinwheel --> Select --> Auth --> Income --> Linked --> Return

    Linked --> Advance
    Linked --> ModelStatus
"""

    render_mermaid(user_flow, height=420)

    # =====================================================
    # SEQUENCE DIAGRAM (UNCHANGED LOGIC)
    # =====================================================
    st.markdown("### 2. Pinwheel Integration — Sequence Diagram")

    sequence = """
sequenceDiagram
    participant User
    participant FE as Veep FE
    participant BE as Veep Backend
    participant PW as Pinwheel
    participant Model

    User->>FE: Access Veep
    FE->>BE: Check Employer Verification Status
    BE->>BE: Evaluate Status

    alt Request Pinwheel
        BE-->>FE: Launch Pinwheel
        FE->>PW: Open Widget
        User->>PW: Select Employer & Authenticate
        PW-->>FE: Return Income Data
        FE->>BE: Send Payroll Data
        BE->>Model: Update Advance Availability
        Model-->>BE: Status Updated
    else Do Not Request
        BE-->>FE: Do Not Launch Widget
        BE->>Model: Maintain Current Status
    end
"""

    render_mermaid(sequence, height=650)


# --------------------------------------------------
# MERMAID RENDERER
# --------------------------------------------------
def render_mermaid(code: str, height: int):

    components.html(
        f"""
        <div style="
            border:1px solid #e5e5e5;
            border-radius:10px;
            padding:16px;
            background:#ffffff;
            margin-bottom:12px;
        ">
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
        height=height,
        scrolling=False
    )
