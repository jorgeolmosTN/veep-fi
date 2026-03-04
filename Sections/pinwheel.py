import streamlit as st
from streamlit_mermaid import mermaid


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

        User --> FE["Veep FE"]
        FE --> Widget["Pinwheel Widget"]
        Widget --> Employer["Select Employer"]
        Employer --> Auth["Authenticate Payroll"]
        Auth --> Income["Income Verified"]
        Income --> Linked["Account Linked"]
        Linked --> Eligible["Eligibility Recalculated"]
    """

    mermaid(user_flow)

    st.divider()

    # =====================================================
    # 2️⃣ SYSTEM ARCHITECTURE
    # =====================================================
    st.header("2. System Architecture (FE / BE / Model)")

    system_diagram = """
    flowchart LR

        %% User
        User((User))

        %% Frontend
        subgraph Frontend
            FE["Veep FE"]
            Widget["Pinwheel Widget"]
        end

        %% Pinwheel
        subgraph Pinwheel
            API["Pinwheel API"]
            EmployerData["Employer Data"]
            Income["Income Verification"]
        end

        %% Backend
        subgraph VeepBackend["Veep Backend"]
            Enrich["Member Enrichment"]
            Destination["Destination Account Creation"]
        end

        %% Model
        subgraph ModelShop
            Eligibility["Eligibility Recalculation"]
        end

        %% Flow
        User --> FE
        FE --> Widget
        Widget --> API

        API --> EmployerData
        EmployerData --> Income

        Income --> Enrich
        Enrich --> Destination
        Destination --> Eligibility

        %% Edge Case
        API -.-> EdgeCase["Employer Not Found (Phase 2)"]
    """

    mermaid(system_diagram)
