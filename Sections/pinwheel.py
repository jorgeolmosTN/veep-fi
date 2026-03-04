import streamlit as st
import streamlit.components.v1 as components


def render():

    # --------------------------------------------------
    # PAGE SPACING CONTROL
    # --------------------------------------------------
    st.markdown("""
    <style>
    .block-container {
        padding-left: 4rem !important;
        padding-right: 4rem !important;
        padding-top: 0.3rem !important;
        padding-bottom: 0.3rem !important;
    }

    h1 { margin-bottom: 8px !important; }
    h3 { margin-top: 8px !important; margin-bottom: 4px !important; }
    </style>
    """, unsafe_allow_html=True)

    st.title("Pinwheel Integration")

    # =====================================================
    # INFO SECTION
    # =====================================================
    st.markdown("### What Pinwheel Enables")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("🏢 **Employer Verification**")
        st.caption("Confirms active payroll relationship")

        st.markdown("🏦 **Destination Account Creation**")
        st.caption("Creates verified payout account")

    with col2:
        st.markdown("💰 **Income Validation**")
        st.caption("Retrieves verified compensation data")

        st.markdown("📊 **Eligibility Refresh**")
        st.caption("Triggers Model recalculation")

    with col3:
        st.markdown("🧩 **Member Enrichment**")
        st.caption("Updates internal profile attributes")

        st.markdown("⚠️ **Risk Tier Adjustment**")
        st.caption("Applied on early widget exit")

    st.markdown("---")

    # =====================================================
    # 1️⃣ HAPPY PATH
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
    Final["Advance Availability Status"]:::final

    User --> FE --> Widget --> Employer --> Auth --> Income --> Linked --> Final
"""

    render_mermaid(happy_flow)

    # =====================================================
    # 2️⃣ EXIT FLOW
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
    # 3️⃣ SEQUENCE DIAGRAM
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
        Model-->>BE: Advance Availability Updated
        BE-->>FE: Status Confirmed
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
# MERMAID RENDERER (AUTO HEIGHT — NO FIXED SPACE)
# --------------------------------------------------
def render_mermaid(code: str):

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
        scrolling=True
    )
