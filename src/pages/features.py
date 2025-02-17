import streamlit as st
from lib.salable import (
    get_capabilities_for_grantee,
    get_checkout_link
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
        
        try:
            grantee_id = st.experimental_user.email
            capabilities = get_capabilities_for_grantee(grantee_id)
            st.write("Your Capabilities for the Current Product:")
            if not capabilities:
                st.write("No product features are enabled. You can purchase a license to unlock features.")
                st.link_button(url=get_checkout_link(st.experimental_user.email)["checkoutUrl"], label="Buy Now")
            else: 
                for cap in capabilities:
                    st.write(cap["name"])
        except Exception as e:
            st.error(f"Error fetching capabilities: {e}")
    back_to_home()
if __name__ == '__main__':
    main()