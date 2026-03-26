import streamlit as st
import os
from utils.data_loader import load_data, load_model
from utils.ui_components import load_css


def main():

    # =========================
    # App Settings
    # =========================

    st.set_page_config(
        page_title="Smart Portfolio Dashboard",
        layout="wide",
        initial_sidebar_state="expanded",
    )


    # =========================
    # Load Custom CSS
    # =========================

    load_css()



    # =========================
    # Load Data & Model
    # =========================

    with st.spinner("⏳ Loading system... Please wait"):
        df = load_data()
        model = load_model()


    # =========================
    # System Status
    # =========================

    if df is not None and model is not None:

        st.sidebar.success("✅ System Ready & Active")

        st.sidebar.markdown("### 📌 System Overview")
        st.sidebar.markdown("🕒 Last Updated: **Today**")
        st.sidebar.markdown("📊 Status: **Running Smoothly**")


        # =========================
        # Main Header
        # =========================

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown(
            "<h1 style='text-align:center;'>Bank Customer Churn Analysis Dashboard</h1>",
            unsafe_allow_html=True
        )

        st.markdown("""
       <h3 style='text-align:center;'> 🚀 Monitor • Predict • Retain Bank Customers</h3>

        """, unsafe_allow_html=True)


        st.markdown("""
        ### ✅ What You Can Do in This Banking Dashboard:
:

        🔹 Analyze bank customer behavior  
        🔹 Identify customers likely to leave  
        🔹 Monitor account and credit patterns  
        🔹 Reduce customer churn  
        🔹 Improve bank profitability  

        📈 Use predictive analytics to strengthen customer loyalty.""")
        st.markdown('</div>', unsafe_allow_html=True)


        st.markdown('<div class="hr-glow"></div>', unsafe_allow_html=True)


        # =========================
        # KPI Section
        # =========================

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("## 📊 Banking Performance Indicators")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "👥 Total Customers",
                f"{len(df):,}"
            )

        with col2:
            risk_rate = df["churn"].mean() * 100

            st.metric(
                "📉🔥 Customer Churn Risk",
                f"{risk_rate:.1f}%",
                delta="-0.1%"
            )

        with col3:
            avg_credit = df["credit_score"].mean()

            st.metric(
                "💳 Average Credit Score",
                f"{avg_credit:.0f}"
            )
        st.markdown('</div>', unsafe_allow_html=True)


        st.markdown('<div class="hr-glow"></div>', unsafe_allow_html=True)


        # =========================
        # Insight Section
        # =========================

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("## 💡 Banking Customer Insights")

        st.markdown("""
        📌 **Banking Business Summary:**

        ✔ Customers with low balance have higher churn risk  
        ✔ Long-term customers generate stable revenue  
        ✔ Credit score impacts loyalty  
        ✔ Early churn detection saves marketing cost  
        ✔ Personalized offers improve retention  

🎯 Focus on valuable customers to grow banking business.""")
        st.markdown('</div>', unsafe_allow_html=True)



        st.markdown('<div class="hr-glow"></div>', unsafe_allow_html=True)


        # =========================
        # Footer
        # =========================

        st.markdown(
            "<center>🔍 Smart Analytics Platform | Version 2.0 | Powered by Machine Learning 🤖</center>",
            unsafe_allow_html=True
        )


    else:

        st.error(
            "❌ System Error: Data or model not found. Please check setup."
        )


# =========================
# Run App
# =========================

if __name__ == "__main__":
    main()
