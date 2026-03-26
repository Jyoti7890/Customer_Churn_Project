import streamlit as st
import os

def load_css():
    """Loads assets/style.css and injects it into the Streamlit app."""
    css_path = os.path.join(os.getcwd(), "assets", "style.css")
    
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    
    # Sidebar Branding (Global)
    st.sidebar.markdown("### ✨ Simple • Smart • Reliable")
    st.sidebar.markdown('<div class="hr-glow"></div>', unsafe_allow_html=True)
    
