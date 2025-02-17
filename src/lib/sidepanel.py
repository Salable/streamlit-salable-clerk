import streamlit as st
from datetime import datetime, timezone


def profile_sidebar():
    with st.sidebar:
        if "picture" in st.experimental_user:
            st.image(st.experimental_user.picture, width=25)
        st.write("Logged in as")
        st.write(st.experimental_user.email)
        # Convert auth_time to UTC datetime
        auth_time = st.experimental_user.to_dict().get("auth_time")
        if auth_time:
            last_logged_in = datetime.fromtimestamp(auth_time, tz=timezone.utc).strftime('%Y-%m-%d')
            st.write(f"Last logged in: {last_logged_in}")
        
        if st.button("Log Out"):
            st.logout()
            st.stop()

def back_to_home():
    home1, home2, home3 = st.columns(3)
    with home2:
        st.page_link("home.py", label="Back to Home")