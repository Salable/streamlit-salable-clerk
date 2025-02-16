import streamlit as st
from datetime import datetime, timezone

def profile_sidebar():
    with st.sidebar:
        st.subheader("Profile")
        st.image(st.experimental_user.picture, width=75)
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
        st.write("Logged in")
        st.write(st.experimental_user.email)
        st.write(st.experimental_user.to_dict())

if __name__ == '__main__':
    main()