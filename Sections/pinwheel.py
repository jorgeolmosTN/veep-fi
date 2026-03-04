import streamlit as st


def render():

    st.title("Pinwheel Integration")

    # ---------------------------------------------------
    # 1️⃣ WHAT IS PINWHEEL
    # ---------------------------------------------------
    st.header("1. What is Pinwheel?")

    st.markdown("""
Pinwheel is used in the FI flow to:

- Verify employer information  
- Validate income data  
- Link payroll account  
- Enable destination account creation  
- Trigger eligibility refresh in ModelShop  

In short, Pinwheel enables verified payroll connectivity required for EWA.
    """)

    st.divider()

    # ---------------------------------------------------
    # 2️⃣ USER FLOW
    # ---------------------------------------------------
    st.header("2. User Flow")

    user_flow = """
    digraph {
        rankdir=LR;
        node [shape=box, style=rounded];

        User -> "Open EWA";
        "Open EWA" -> "Launch Pinwheel Widget";
        "Launch Pinwheel Widget" -> "Select Employer";
        "Select Employer" -> "Authenticate Payroll";
        "Authenticate Payroll" -> "Payroll Verified";
        "Payroll Verified" -> "Account Linked";
        "Account Linked" -> "Eligibility Refreshed";
    }
    """

    st.graphviz_chart(user_flow)

    st.divider()

    # ---------------------------------------------------
    # 3️⃣ SYSTEM DIAGRAM
    # ---------------------------------------------------
    st.header("3. System Architecture (FE / BFF / BE / Model)")

    system_diagram = """
    digraph {
        rankdir=LR;

        node [shape=box];

        User -> FE;
        FE -> "Pinwheel Widget";
        "Pinwheel Widget" -> "Pinwheel API";

        "Pinwheel API" -> BE;
        BE -> "Member Enrichment";
        "Member Enrichment" -> "Destination Account Creation";
        "Destination Account Creation" -> Model;
        Model -> FE;

        "Pinwheel API" -> "Employer Not Found" [style=dashed];
    }
    """

    st.graphviz_chart(system_diagram)
