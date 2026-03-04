import streamlit as st
import streamlit.components.v1 as components


def render():

    st.title("Pinwheel Integration")

    st.markdown("""
Pinwheel enables payroll connectivity and verified income validation
required for FI eligibility and EWA disbursement.
    """)

    st.divider()

    # =====================================================
    # 1️⃣ USER FLOW
    # =====================================================
    st.header("1. User Flow")

   user_flow = """
flowchart LR

    %% Layout
    classDef main fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#111;
    classDef decision fill:#ffffff,stroke:#333,stroke-width:1px,color:#111;
    classDef risk fill:#ffe6e6,stroke:#a33,stroke-width:1px,color:#600;
    classDef neutral fill:#e8eef7,stroke:#335,stroke-width:1px,color:#112;

    %% Nodes
    User((User)):::neutral
    FE["Veep FE"]:::main
    Widget["Pinwheel Widget"]:::main

    Employer["Select Employer"]:::main
    Auth["Authenticate Payroll"]:::main
    Income["Income Verified"]:::main
    Linked["Account Linked"]:::main
    Eligible["Eligibility Recalculated"]:::neutral

    Exit["Exit Anytime"]:::decision
    Dashboard["EWA Dashboard"]:::main
    Tier["Tier Reduction in Risk Score"]:::risk

    %% Main Flow
    User --> FE --> Widget --> Employer --> Auth --> Income --> Linked --> Eligible

    %% Exit Path
    Widget -.-> Exit --> Dashboard --> Tier
"""

    render_mermaid(user_flow)

    st.divider()

    # =====================================================
    # 2️⃣ SYSTEM ARCHITECTURE
    # =====================================================
    st.header("2. System Architecture (FE / BE / Model)")

    system_diagram = """
    flowchart LR

        User((User))

        subgraph Frontend
            FE["Veep FE"]
            Widget["Pinwheel Widget"]
        end

        subgraph Pinwheel
            API["Pinwheel API"]
            EmployerData["Employer Data"]
            Income["Income Verification"]
        end

        subgraph VeepBackend["Veep Backend"]
            Enrich["Member Enrichment"]
            Destination["Destination Account Creation"]
        end

        subgraph ModelShop
            Eligibility["Eligibility Recalculation"]
        end

        User --> FE
        FE --> Widget
        Widget --> API

        API --> EmployerData
        EmployerData --> Income

        Income --> Enrich
        Enrich --> Destination
        Destination --> Eligibility

        API -.-> EdgeCase["Employer Not Found (Phase 2)"]
    """

    render_mermaid(system_diagram)


def render_mermaid(code: str):
    components.html(
        f"""
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <div class="mermaid">
            {code}
        </div>
        <script>
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        height=500,
    )
