import streamlit as st

# Set the title of the Streamlit app
st.title("Ambulance Detection")

# Display two videos: one as input and one as output
st.header("Input Video")
st.video("test.mp4")  # Replace with the path to your input video file

st.header("Output Video")
st.video("128902410-a6724e49-c7b7-4862-8ef2-dc71e4b9105e.mp4")  # Replace with the path to your output video file