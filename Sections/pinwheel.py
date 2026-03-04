import streamlit as st
import graphviz


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

    user_flow = graphviz.Digraph()
    user_flow.attr(rankdir='LR')
    user_flow.attr('node', shape='box', style='rounded')

    user_flow.node("User")
    user_flow.node("FE", "Veep FE")
    user_flow.node("Widget", "Pinwheel Widget")
    user_flow.node("Employer", "Select Employer")
    user_flow.node("Auth", "Authenticate Payroll")
    user_flow.node("Verify", "Income Verified")
    user_flow.node("Linked", "Account Linked")
    user_flow.node("Eligible", "Eligibility Recalculated")

    user_flow.edge("User", "FE")
    user_flow.edge("FE", "Widget")
    user_flow.edge("Widget", "Employer")
    user_flow.edge("Employer", "Auth")
    user_flow.edge("Auth", "Verify")
    user_flow.edge("Verify", "Linked")
    user_flow.edge("Linked", "Eligible")

    st.graphviz_chart(user_flow)

    st.divider()

    # =====================================================
    # 2️⃣ SYSTEM ARCHITECTURE DIAGRAM
    # =====================================================
    st.header("2. System Architecture (FE / BE / Model)")

    system = graphviz.Digraph()
    system.attr(rankdir='LR')

    # External
    system.node("User", shape="oval")

    # FE Cluster
    with system.subgraph(name="cluster_fe") as fe:
        fe.attr(label="Frontend")
        fe.node("FE", "Veep FE")
        fe.node("Widget", "Pinwheel Widget")

    # Pinwheel Cluster
    with system.subgraph(name="cluster_pinwheel") as pw:
        pw.attr(label="Pinwheel")
        pw.node("API", "Pinwheel API")
        pw.node("EmployerData", "Employer Data")
        pw.node("Income", "Income Verification")

    # Backend Cluster
    with system.subgraph(name="cluster_be") as be:
        be.attr(label="Veep Backend")
        be.node("Enrich", "Member Enrichment")
        be.node("Destination", "Destination Account Creation")

    # Model Cluster
    with system.subgraph(name="cluster_model") as model:
        model.attr(label="ModelShop")
        model.node("Eligibility", "Eligibility Recalculation")

    # Edges
    system.edge("User", "FE")
    system.edge("FE", "Widget")
    system.edge("Widget", "API")

    system.edge("API", "EmployerData")
    system.edge("EmployerData", "Income")

    system.edge("Income", "Enrich")
    system.edge("Enrich", "Destination")
    system.edge("Destination", "Eligibility")

    # Edge Case
    system.node("EdgeCase", "Employer Not Found\n(Phase 2)", shape="box", style="dashed")
    system.edge("API", "EdgeCase", style="dashed")

    st.graphviz_chart(system)
