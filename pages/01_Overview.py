import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from utils.data_loader import load_data
from utils.ui_components import load_css


# =============================
# Theme Colors (LOCKED ❌ BLUE)
# =============================
PURPLE = "#8b5cf6"
GRAY = "#94a3b8"
RED = "#ef4444"
GREEN = "#22c55e"
WHITE = "#e5e7eb"

BG = "rgba(0,0,0,0)"


def show_overview():

    # =============================
    # Inject CSS
    # =============================
    load_css()

    # =============================
    # Page Header
    # =============================
    st.markdown("""
        <div class="glass-card">
            <h1 style="text-align:center;"> Bank Customer Churn Overview</h1>
            <p style="text-align:center; color:#a78bfa;">
                Customer Stability • Risk Signals • Retention Intelligence
            </p>
        </div>
    """, unsafe_allow_html=True)

    # =============================
    # Load Data
    # =============================
    df = load_data()
    if df is None:
        st.error("❌ Data system offline")
        return

    # =============================
    # Filters
    # =============================
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 🔍 Customer Segmentation Filters")
    st.caption("Refine customer groups to analyze churn risk patterns")

    c1, c2, c3 = st.columns(3)

    with c1:
        countries = st.multiselect(
            "Region",
            df["country"].unique(),
            default=df["country"].unique()
        )

    with c2:
        genders = st.multiselect(
            "Gender",
            df["gender"].unique(),
            default=df["gender"].unique()
        )

    with c3:
        products = st.multiselect(
            "Products",
            df["products_number"].unique(),
            default=df["products_number"].unique()
        )

    st.markdown('</div>', unsafe_allow_html=True)

    filtered_df = df[
        (df["country"].isin(countries)) &
        (df["gender"].isin(genders)) &
        (df["products_number"].isin(products))
    ]

    # =============================
    # KPI Section
    # =============================
    st.markdown('<div class="hr-glow"></div>', unsafe_allow_html=True)
    st.markdown("## 📊 Customer Churn Health Snapshot")
    st.caption("Key indicators measuring customer risk and engagement")

    k1, k2, k3, k4, k5 = st.columns(5)

    with k1:
        st.metric("Total Customers", f"{len(filtered_df):,}")

    with k2:
        churn = filtered_df["churn"].mean() * 100
        st.metric("Churn Rate", f"{churn:.1f}%")

    with k3:
        active = filtered_df["active_member"].mean() * 100
        st.metric("Active Customers", f"{active:.0f}%")

    with k4:
        credit = filtered_df["credit_score"].mean()
        st.metric("Avg Credit Score", f"{credit:.0f}")

    with k5:
        bal = filtered_df["balance"].mean()
        st.metric("Avg Balance", f"${bal/1000:,.0f}K")

    # =============================
    # Region & Gender
    # =============================
    st.markdown('<div class="hr-glow"></div>', unsafe_allow_html=True)
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("## 🌍 Churn Risk by Region")
        st.caption("Regions with higher churn probability")

        risk_country = filtered_df.groupby("country", observed=False)["churn"].mean().reset_index()
        risk_country["Risk %"] = risk_country["churn"] * 100

        fig_country = px.bar(
            risk_country,
            x="country",
            y="Risk %",
            text="Risk %",
            color_discrete_sequence=[PURPLE]
        )
        fig_country.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig_country.update_layout(
            plot_bgcolor=BG,
            paper_bgcolor=BG,
            font=dict(color=WHITE, family="Poppins"),
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)")
        )
        st.plotly_chart(fig_country, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("## 👥 Customer Gender Distribution")
        st.caption("Churn exposure across gender segments")

        gender_mix = filtered_df["gender"].value_counts().reset_index()
        gender_mix.columns = ["Gender", "Count"]

        fig_gender = px.pie(
            gender_mix,
            values="Count",
            names="Gender",
            hole=0.7,
            color_discrete_sequence=[PURPLE, GRAY]
        )
        fig_gender.update_layout(
            plot_bgcolor=BG,
            paper_bgcolor=BG,
            font=dict(color=WHITE, family="Poppins"),
            legend=dict(orientation="h", y=-0.15, x=0.5, xanchor="center")
        )
        st.plotly_chart(fig_gender, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

   
    # =============================
    # Age Stability
    # =============================
    st.markdown('<div class="hr-glow"></div>', unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("## 📈 Customer Stability Across Age Groups")
    st.caption("Retention strength and churn exposure by age")

    bins = [18, 25, 35, 45, 55, 65, 100]
    labels = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]

    filtered_df["Age Group"] = pd.cut(
        filtered_df["age"], bins=bins, labels=labels, right=False
    )

    age_data = filtered_df.groupby("Age Group", observed=False)["churn"].mean().reset_index()
    age_data["Stable"] = (1 - age_data["churn"]) * 100
    age_data["Risk"] = age_data["churn"] * 100

    fig_age = go.Figure()
    fig_age.add_bar(x=age_data["Age Group"], y=age_data["Stable"], name="Stable", marker_color=PURPLE)
    fig_age.add_bar(x=age_data["Age Group"], y=age_data["Risk"], name="Risk", marker_color=RED)

    fig_age.update_layout(
        plot_bgcolor=BG,
        paper_bgcolor=BG,
        font=dict(color=WHITE, family="Poppins"),
        barmode="stack",
        legend=dict(orientation="h", y=1.1, x=1, xanchor="right"),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)")
    )
    st.plotly_chart(fig_age, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # =============================
    # Footer
    # =============================
    st.markdown('<div class="hr-glow"></div>', unsafe_allow_html=True)
    st.markdown("""
        <center style="color:#94a3b8;">
            Smart Banking Intelligence • Version 2.0 • AI Powered Churn Analytics
        </center>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    show_overview()
