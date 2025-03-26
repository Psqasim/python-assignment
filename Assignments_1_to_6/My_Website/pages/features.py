import streamlit as st

def apply_dark_theme():
    st.markdown("""
        <style>
        .stApp { background-color: #0E1117; color: #FAFAFA; }
        </style>
    """, unsafe_allow_html=True)

apply_dark_theme()

st.title("⭐ Features")
st.write("""
### Application Features
- Dark Mode Interface
- Multi-page Navigation
- Responsive Design
- Interactive Components
- Form Handling
""")