import streamlit as st
from datetime import datetime, timezone
from lib.salable import (
    get_licenses_for_grantee,
)
from lib.sidepanel import (
    profile_sidebar,
    back_to_home
)

def main():
    if not st.experimental_user.is_logged_in:
        st.write("Please log in to continue.")
        if st.button("Log In"):
            st.login()
            st.stop()
    else:
        profile_sidebar()
        col1, col2 = st.columns(2, gap="medium")
        with col1:
            st.header("Clerk Profile")
            st.write(st.experimental_user.email)
            st.write(st.experimental_user.to_dict())

        try:
            # Use the grantee_id from the current user as the license check identifier
            grantee_id = st.experimental_user.email
            license_info = get_licenses_for_grantee(grantee_id)
            with col2:
                st.header("Salable Licenses")
                st.write(license_info)
        except Exception as e:
            st.error(f"Error checking license: {e}")
    back_to_home()

if __name__ == '__main__':
    main()