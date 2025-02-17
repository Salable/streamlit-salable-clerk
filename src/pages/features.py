import streamlit as st
from datetime import datetime, timezone
from lib.salable import (
    get_capabilities_for_grantee
)

def back_to_home():
    home1, home2, home3 = st.columns(3)
    with home2:
        st.page_link("home.py", label="Back to Home")


def profile_sidebar():
    with st.sidebar:
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
        
        try:
            grantee_id = st.experimental_user.email
            capabilities = get_capabilities_for_grantee(grantee_id)
            st.write("Your Capabilities for the Current Product:")
            for cap in capabilities:
                st.write(cap["name"])
        except Exception as e:
            st.error(f"Error fetching capabilities: {e}")
    back_to_home()
if __name__ == '__main__':
    main()