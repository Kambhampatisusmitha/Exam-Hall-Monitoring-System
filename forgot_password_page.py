import streamlit as st
from db_manager import forgot_password
from db_manager import valid_user
def forgot_password_page():
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://img.freepik.com/free-vector/abstract-soft-colorful-watercolor-texture-background-design_1055-13464.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    with st.form(key="forgot_password_form"):
        st.title("Change Password Here!!")
        email = st.text_input("Enter your registered email")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if valid_user(email):
                st.success("OTP sent to your email!")
            else:
                st.error("Invalid Email!")