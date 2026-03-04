import streamlit as st


def render():

    st.title("Pinwheel Integration")

    st.subheader("Pinwheel Integration Flow")

    mermaid_code = """
    flowchart LR

        User --> FE["Veep FE"]
        FE --> PW_Widget["Pinwheel Widget"]
        PW_Widget --> PW_API["Pinwheel API"]

        PW_API --> BE["Veep Backend"]

        BE --> Enrich["Member Enrichment"]
        Enrich --> Dest["Create Destination Account"]

        Dest --> Model["ModelShop Eligibility Refresh"]
        Model --> FE

        PW_API -->|Employer Not Found| Edge["Edge Case Handling (Phase 2)"]
    """

    st.markdown(
        f"""
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <div class="mermaid">
        {mermaid_code}
        </div>
        <script>
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("### Flow Explanation")

    st.markdown("""
    **1. User initiates account linking in FE**  
    → Pinwheel widget loads.

    **2. Pinwheel verifies employer & income**  
    → Returns payroll data.

    **3. Backend enriches member profile**

    **4. Destination account created**

    **5. Eligibility refreshed in ModelShop**

    **6. Employer Not Found → Phase 2 handling**
    """)
