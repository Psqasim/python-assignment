import streamlit as st

def apply_dark_theme():
    st.markdown("""
        <style>
        .stApp { background-color: #0E1117; color: #FAFAFA; }
        </style>
    """, unsafe_allow_html=True)

apply_dark_theme()

st.title("📩 Contact Us")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    if st.form_submit_button("Submit"):
        st.success("Message sent successfully!")