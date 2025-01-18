import streamlit as st
from streamlit_option_menu import option_menu
import cv2
from deepface import DeepFace
from tempfile import NamedTemporaryFile
import os


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
        uploaded_file=st.file_uploader("Upload Video",type=['mp4'])
        if uploaded_file:
            #play video
            temp_file = NamedTemporaryFile(delete=False)
            temp_file.write(uploaded_file.read())

            st.sidebar.success("Video uploaded successfully!")

            # Process video and detect emotions
            if temp_file:
                # Load the video
                video_path = temp_file.name
                cap = cv2.VideoCapture(video_path)

                stframe = st.empty()  # For displaying video frames

                # Load Haarcascade for face detection
                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break

                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

                    # Detect faces
                    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                    for (x, y, w, h) in faces:
                        face_roi = rgb_frame[y:y + h, x:x + w]
                        try:
                            # Analyze emotion using DeepFace
                            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
                            dominant_emotion = result[0]['dominant_emotion']

                            # Draw rectangle and emotion label
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                            cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                        except Exception as e:
                            print(f"Error analyzing face: {e}")

                    # Convert frame to BGR for Streamlit
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    # Display frame in Streamlit
                    stframe.image(frame, channels="RGB", use_column_width=True)

                cap.release()
                os.unlink(temp_file.name)  # Delete temporary file after processing
                st.success("Video processing completed!")
            else:
                st.warning("Please upload a video file to start emotion detection.")


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
