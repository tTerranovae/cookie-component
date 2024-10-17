from time import sleep

import streamlit as st

from cookie_component import cookie_manager

# Page layout
st.set_page_config(page_title="Cookie Manager", layout="centered")

# Header and description
st.title("✨Cookie Manager")
st.write(
    """
 The Cookie Management Component provides a straightforward and efficient way to interact with browser cookies. This component allows developers to easily get or set cookies in the user's browser, facilitating the management of user preferences, session information, and other data that may need to persist across page refreshes or sessions.
"""
)
# Set cookie form
st.subheader("Set a Cookie in the Browser")
with st.form("cookie_form"):
    name = st.text_input("Cookie Name", placeholder="Enter the cookie name")
    value = st.text_input("Cookie Value", placeholder="Enter the cookie value")
    expires = st.number_input("Expires (days)", min_value=1, value=1)
    submitted = st.form_submit_button("Set Cookie")
    if not name or not value:
        st.warning("Please enter a cookie name and value.")
    if submitted and name and value:
        cookie_manager(name, "set", value, expires)
        st.success(f"Cookie *{name}* has been set with the value *{value}*. 🎉")

# Retrieve cookie
st.subheader("Retrieve a Cookie from the Browser")
with st.form("cookie_form_get"):
    name = st.text_input("Cookie Name", placeholder="Enter the cookie name")
    if st.form_submit_button("Get Cookie"):
        with st.spinner("Retrieving cookie..."):
            cookie_value = cookie_manager(name, "get")
            sleep(2)
            if cookie_value:
                st.success(f"Value of cookie *{name}*: {cookie_value} 🎉")
            else:
                st.warning(f"Cookie *{name}* not found.")


# Example code
st.subheader("Example Usage")
st.code(
    """
#! app.py
import streamlit as st
from cookie_component import cookie_manager

# Get a cookie
cookie_value = cookie_manager(<cookie_name>, 'get')

# Set a cookie
cookie_manager(<cookie_name>, 'set', <value>)
""",
    language="python",
)

# Component information
st.subheader("Component Documentation")
st.write(
    """
1. Check `cookie_component/__init__.py` for the Python implementation.
2. Review `cookie_component/index.js` for the JavaScript logic.
3. Look at `cookie_component/streamlit-component-lib.js` for the integration between Streamlit and JavaScript.
"""
)
