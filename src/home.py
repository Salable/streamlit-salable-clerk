import streamlit as st
from datetime import datetime, timezone

def profile_sidebar():
    with st.sidebar:
        st.subheader("Profile")
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