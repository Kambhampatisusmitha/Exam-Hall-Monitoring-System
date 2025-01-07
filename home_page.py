import streamlit as st

def home_page():
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url('https://www.shutterstock.com/image-photo/blur-abstract-background-examination-room-260nw-570148435.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    # Center the image
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://www.splashgain.com/wp-content/uploads/2022/09/Eklavvya-Remote-Proctoring.webp" style="max-width: 50%;">
        </div>
        """,
        unsafe_allow_html=True
    )
