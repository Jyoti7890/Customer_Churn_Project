import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_model
from utils.ui_components import load_css


def show_explainability():
    # =============================
    # Page Settings & CSS
    # =============================
    load_css()

    st.markdown("""
        <div class="glass-card">
            <h1 style='text-align:center;'>🧠 Portfolio Intelligence Drivers</h1>
            <p style='text-align:center; color:#a78bfa;'>
            Clear explanation of churn risk and recommended actions
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="hr-glow"></div>', unsafe_allow_html=True)

    # =============================
    # Load model (ONLY for global view)
    # =============================
    model = load_model()

    # Tabs
    tab_global, tab_local = st.tabs(
        ["🌐 Portfolio-Wide Factors", "📍 Account-Specific Explanation"]
    )

    PURPLE = "#8b5cf6"
    WHITE = "#e5e7eb"
    ACCENT = "#a78bfa"

    # ======================================================
    # TAB 1: GLOBAL EXPLAINABILITY (STATIC – MODEL BASED)
    # ======================================================
    with tab_global:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Portfolio-Wide Risk Drivers")
        st.markdown(
            "These factors generally influence customer retention across the bank."
        )

        if model is None:
            st.warning("Global insights unavailable.")
        else:
            try:
                xg_model = model.named_steps["model"]
                importances = xg_model.feature_importances_

                feature_names = [
                    "Credit Score",
                    "Geography",
                    "Customer Segment",
                    "Age",
                    "Tenure",
                    "Account Balance",
                    "Usage Level",
                    "Credit Card",
                    "Engagement",
                    "Estimated Income"
                ]

                min_len = min(len(feature_names), len(importances))
                imp_df = pd.DataFrame({
                    "Factor": feature_names[:min_len],
                    "Weight": importances[:min_len]
                }).sort_values("Weight", ascending=False).head(8)

                fig = px.bar(
                    imp_df,
                    x="Weight",
                    y="Factor",
                    orientation="h",
                    color_discrete_sequence=[PURPLE]
                )

                fig.update_layout(
                    yaxis={"categoryorder": "total ascending"},
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                    font=dict(color=WHITE),
                    margin=dict(l=0, r=0, t=10, b=0),
                )

                st.plotly_chart(fig, use_container_width=True)

            except Exception as e:
                st.error(f"Unable to load global insights: {e}")

        st.markdown('</div>', unsafe_allow_html=True)

    # ======================================================
    # TAB 2: LOCAL EXPLAINABILITY (NO MODEL CALL)
    # ======================================================
    with tab_local:
        if "last_prediction" not in st.session_state:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.warning(
                "Please generate a churn prediction first to view customer explanation."
            )
            st.markdown('</div>', unsafe_allow_html=True)
            return

        pred_data = st.session_state["last_prediction"]
        input_df = pred_data["input"]
        status = pred_data["status"]

        st.markdown(f"""
        <div class="glass-card">
            <p style="color:{ACCENT}; font-size:12px; margin:0;">PREDICTION RESULT</p>
            <h3 style="color:{WHITE}; margin:0;">Customer Risk Level: {status}</h3>
        </div>
        """, unsafe_allow_html=True)

        # -------------------------------
        # PART 1: WHY
        # -------------------------------
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 1) WHY THIS CUSTOMER IS AT RISK")
        st.markdown("This customer is considered at risk mainly because:")

        reasons = []

        if input_df["active_member"].iloc[0] == 0:
            reasons.append("The customer is not actively using bank services")

        if input_df["credit_score"].iloc[0] < 600:
            reasons.append("The credit score is lower than the typical customer average")

        if input_df["balance"].iloc[0] < 10000:
            reasons.append("The account balance is relatively low")

        if input_df["age"].iloc[0] > 50:
            reasons.append("This age group shows higher churn trends historically")

        if reasons:
            for r in reasons:
                st.markdown(f"• {r}")
        else:
            st.markdown("• The customer profile appears stable with no major warning signs")

        st.markdown('</div>', unsafe_allow_html=True)

        # -------------------------------
        # PART 2: WHAT ACTION
        # -------------------------------
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 2) WHAT ACTION THE BANK SHOULD TAKE")
        st.markdown("Recommended steps:")

        st.markdown("• Assign a relationship manager for personal outreach")

        if input_df["active_member"].iloc[0] == 0:
            st.markdown("• Encourage usage of core banking services")

        if input_df["balance"].iloc[0] < 20000:
            st.markdown("• Offer a loyalty benefit or account upgrade")

        st.markdown("• Ensure products match the customer’s actual needs")
        st.markdown('</div>', unsafe_allow_html=True)

        # -------------------------------
        # PART 3: WHAT WOULD IMPROVE
        # -------------------------------
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 3) WHAT WOULD IMPROVE THE SITUATION (NO CHANGES APPLIED)")

        st.markdown(
            "If the customer becomes more active, it may help reduce future churn risk."
        )

        st.markdown(
            "Improvement in credit score over time can strengthen long-term stability."
        )

        st.markdown(
            "Maintaining a higher balance and deeper engagement can increase loyalty."
        )

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="hr-glow"></div>', unsafe_allow_html=True)
    st.markdown("""
        <center style='color:#94a3b8;'>
        Smart Banking Intelligence • Explainability Module
        </center>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    show_explainability()
