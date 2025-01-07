import streamlit as st

def features_page():
    # Center the login form using Streamlit form layout
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvdjEwNjQtMzYta3ZjNHNieHcuanBn.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    d1, d2, d3, d4, d5,d6 = ["Anomaly detection", "Emotion detection", "Unauthorized material detection", "Hand gestures recognition", "Exam management module",'Alert system']
    h1, h2, h3, h4, h5,h6 = ["Anomaly detection in exams can monitor head movements using computer vision and machine learning techniques to identify unusual patterns, such as frequent turning or excessive motion, which may indicate cheating behavior. These systems analyze real-time video feeds, ensuring a fair and secure examination environment.", 
                             "Emotion detection leverages machine learning and deep learning techniques to analyze facial expressions, voice tones, or text to identify human emotions like happiness, anger, or sadness. It finds applications in areas such as customer service, mental health monitoring, and personalized content recommendations.", 
                             "Unauthorized material detection uses computer vision and natural language processing to identify prohibited items, such as mobile phones or cheat sheets, in examination environments. By analyzing real-time video feeds or scanned documents, it ensures compliance with regulations and maintains the integrity of the exam.", 
                             "Hand gesture recognition utilizes computer vision and machine learning to analyze hand movements and interpret gestures in real-time. It enables applications like touchless control, sign language interpretation, and immersive gaming experiences.", 
                             "An Exam Management Module facilitates efficient exam administration by automating tasks like exam scheduling and seating management. It allows administrators to create exam timetables, allocate venues, and assign seating arrangements based on predefined rules.",
                             'An alert system monitors activities like head movements, unauthorized materials, and gestures during exams, instantly notifying administrators of any anomalies. It ensures real-time interventions, enhancing security and fairness in the examination process.']
    i1 = "https://blog.teamsatchel.com/hs-fs/hubfs/Attainment%208%20and%20Progress%208/Girl%20copying%20another%20students%20work%20in%20exam%20i%20nexam%20hall%20in%20college.jpeg?width=773&name=Girl%20copying%20another%20students%20work%20in%20exam%20i%20nexam%20hall%20in%20college.jpeg"
    i2="https://recfaces.com/wp-content/uploads/2021/03/rf-emotion-recognition-rf-830x495-1.jpeg"
    i3="https://resilienteducator.com/wp-content/uploads/2012/11/AdobeStock_141795921_cup.jpg"
    i4="https://t3.ftcdn.net/jpg/09/26/81/52/360_F_926815250_GtfEpuDVOgIQpNVn0yNKqwLTIt5lhX7X.jpg"
    i5="https://spunout.ie/wp-content/uploads/2023/09/student_taking_a_college_exam-945x630.jpg"
    i6="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdq3qbCIOHwQ7twslquRtXDJZVEtyj9RCUzuXRVHxlrQYmpw7dCl7-ZfNN8tc9UxOHaCM&usqp=CAU"
    profile_css = """
        <style>
            .profile-container {
                background-color: #8bdaf0;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                max-width: 300px;
                border: 1px solid #ccc;
                margin: 10px;
                font-family: Arial, sans-serif;
                text-align: center;
            }
            .profile-header {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
                color: #333;
            }
            .profile-item {
                font-size: 14px;
                margin-bottom: 5px;
                color: #555;
            }
            .profile-image img {
                border-radius: 30%;
                max-width: 200px;
                max-height: 200px;
                margin-bottom: 10px;
            }
        </style>
    """

    # HTML template
    def create_profile_html(name, hospital, image_link):
        return f"""
        <div class="profile-container">
            <div class="profile-image">
                <img src="{image_link}" alt="User Image">
            </div>
            <div class="profile-details">
                <div class="profile-header"><strong></strong> {name}</div>
                <div class="profile-item">{hospital}</div>
            </div>
        </div>
        """

    # Display 3 profiles in 3 columns
    col1, col2, col3 = st.columns(3)
    col1.markdown(profile_css + create_profile_html(d1, h1,i1), unsafe_allow_html=True)
    col2.markdown(profile_css + create_profile_html(d2, h2,i2), unsafe_allow_html=True)
    col3.markdown(profile_css + create_profile_html(d3, h3,i3), unsafe_allow_html=True)
    
    # Display 2 profiles in 2 columns
    col4, col5,col6 = st.columns(3)
    col4.markdown(profile_css + create_profile_html(d4, h4,i4), unsafe_allow_html=True)
    col5.markdown(profile_css + create_profile_html(d5, h5,i5), unsafe_allow_html=True)
    col6.markdown(profile_css + create_profile_html(d6, h6,i6), unsafe_allow_html=True)