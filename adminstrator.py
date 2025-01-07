import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
user_data = st.session_state.get('user', None)
def admin_home_page():
    with st.sidebar:
        # Extracting user data from session state after successful login
        user_data = st.session_state.get('user', None)
        if user_data:
            with st.sidebar:
                # Add custom CSS to center content
                st.markdown(
                    """
                    <style>
                    .center-content {
                        text-align: center;
                        margin: auto;
                    }
                    .center-image img {
                        display: block;
                        margin: auto;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )

                # Centered title
                
                st.markdown(
                    f"<h1 class='center-content' style='color: red; t'>{user_data[1]} Profile</h1>",
                    unsafe_allow_html=True
                )
                
                # Centered image
                st.markdown(
                    f"""
                    <div class="center-image">
                        <img src="https://cdn-icons-png.flaticon.com/512/4128/4128176.png" width="250">
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                #need gap
                st.markdown("<br>",unsafe_allow_html=True)
                # Centered user details
                st.markdown(
                    f"""
                    <div class="center-content">
                        <p ><strong>Name:</strong> {user_data[1]}</p>
                        <p ><strong>User Type:</strong> {user_data[3]}</p>
                        <p><strong>Email:</strong> {user_data[2]}</p>
                        <p><strong>Department:</strong> {user_data[4]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


        else:
            st.error("User not logged in!")
    def exam_monitor():
        st.markdown(
            """
            <style>
            /* Apply background image to the main content area */
            .main {
                background-image: url('https://img.freepik.com/premium-photo/creative-educational-sketch-white-backdrop-with-copybooks-education-knowledge-concept-3d-rendering_670147-66821.jpg');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }
            </style>
            """,
            unsafe_allow_html=True
            )
        video=st.file_uploader("Upload Video",type=['mp4'])
        if video:
            #play video
            st.video(video)
    def management():
        st.markdown(
            """
            <style>
            /* Apply background image to the main content area */
            .main {
                background-image: url('https://png.pngtree.com/background/20210715/original/pngtree-white-simple-texture-background-picture-image_1323742.jpg');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.image('https://t3.ftcdn.net/jpg/07/14/82/24/360_F_714822432_l3cqWz96Yf6FWOARBmTn5tdcDchuxx0h.jpg',use_column_width=True)
    # Navigation menu for user dashboard
    selected_tab = option_menu(
        menu_title=None,
        options=["Exam Monitoring", "Exam Management",'Logout'],
        icons=['camera-fill','newspaper','file-lock2-fill'], menu_icon="cast", default_index=0,
        orientation="horizontal",
    styles={
            "nav-link-selected": {
                "background-color": "#ffc11c",  # Background color of the selected item
                "color": "black",
            },
            "nav-link": {
                "background-color": "#ffefc4",  # Background color of unselected items
                "color": "black",  # Text color of unselected items
            },
        },
    )
    if selected_tab == "Exam Monitoring":
        exam_monitor()
    elif selected_tab == "Exam Management":
        management()
    elif selected_tab=='Logout':
        # Logout functionality
        st.session_state.clear()
        st.rerun()
