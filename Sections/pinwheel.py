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
        User --> FE["Veep FE"]
        FE --> Widget["Pinwheel Widget"]
        Widget --> Employer["Select Employer"]
        Employer --> Auth["Authenticate Payroll"]
        Auth --> Income["Income Verified"]
        Income --> Linked["Account Linked"]
        Linked --> Eligible["Eligibility Recalculated"]
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
