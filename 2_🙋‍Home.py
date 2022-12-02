import streamlit as st

st.set_page_config(
    page_title="Homepage",
    page_icon="👋",
)

st.title("Welcome to my movie recommendation system")
video_file = open('VE Project 21.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes, start_time=0)