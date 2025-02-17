import streamlit as st
from datetime import datetime, timezone
from lib.sidepanel import (
    profile_sidebar
)

def main():
    if not st.experimental_user.is_logged_in:
        st.write("Please log in to continue.")
        if st.button("Log In"):
            st.login()
            st.stop()
    else:
        profile_sidebar()
        st.title("Welcome to Streamlit")
        col1, col2 = st.columns(2)

        with col1:
            st.header("View your Profile")
            st.page_link("pages/profile.py", label="User Profile")

        with col2:
            st.header("View your Product")
            st.page_link("pages/features.py", label="Product Features")
            

if __name__ == '__main__':
    main()