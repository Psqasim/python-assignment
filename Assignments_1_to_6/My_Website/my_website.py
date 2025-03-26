import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Python Web App",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
def apply_dark_theme():
    st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        .main-title {
            color: #00FF88;
            text-align: center;
            font-size: 2.8em;
            text-shadow: 2px 2px 4px #00000080;
        }
        .sidebar .sidebar-content {
            background-color: #1A1D24 !important;
        }
        .stTextInput input, .stSlider .st-c7 {
            background-color: #2D3748 !important;
            border: 1px solid #4A5568 !important;
            color: #E2E8F0 !important;
        }
        .stButton>button {
            background-color: #00FF88 !important;
            color: #0E1117 !important;
        }
        </style>
    """, unsafe_allow_html=True)

apply_dark_theme()

# Main Content
with st.container():
    st.markdown('<h1 class="main-title">🚀 Python Web App</h1>', unsafe_allow_html=True)
    
    # About Section
    with st.expander("📌 About This App", expanded=True):
        st.markdown("""
        **Welcome to this interactive Python web application!**
        - User input handling
        - Interactive elements
        - Responsive design
        - Multi-page navigation
        """)
    
    # Two-column layout
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        # User Interaction
        st.subheader("👤 User Interaction")
        name = st.text_input("Enter your name:", placeholder="Type your name...")
        if name:
            st.success(f"Welcome, {name}! 👋")
            
        number = st.slider("Select a number", 1, 100, 50)
        st.markdown(f"**Selected value:** `{number}`")
        
        # Magic Button
        if st.button("Generate Magic", key="magic_btn"):
            st.balloons()
            st.success("✨ Magic activated!")

    with col2:
        # Image Display
        st.subheader("📸 Technology Showcase")
        try:
            st.image(
                "https://images.unsplash.com/photo-1515879218367-8466d910aaa4",
                caption="Python Development Environment",
                use_column_width=True
            )
        except Exception as e:
            st.error(f"Image load error: {str(e)}")

    # Contact Form
    st.divider()
    st.subheader("📩 Contact Form")
    with st.form("contact_form"):
        email = st.text_input("Email address", placeholder="your.email@example.com")
        message = st.text_area("Your message", height=150,
                             placeholder="Type your message here...")
        if st.form_submit_button("Send Message"):
            if email and message:
                st.success("Message sent successfully!")
            else:
                st.warning("Please fill all required fields")

# Sidebar Navigation
with st.sidebar:
    st.title("🔗 Navigation")
    st.divider()
    st.page_link("my_website.py", label="Home", icon="🏠")
    st.page_link("pages/features.py", label="Features", icon="⭐")
    st.page_link("pages/contact.py", label="Contact", icon="📩")
    st.divider()
    st.markdown("**Developer:** Muhammad Qasim")
    st.markdown("**Version:** 1.1.0")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #718096;">
    © 2024 Python Web App | MIT License | Version 1.1.0
</div>
""", unsafe_allow_html=True)