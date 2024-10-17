import streamlit.components.v1 as components
_component_func = components.declare_component(f"cookie_comp", path="components",)


def get_cookie(name):
    """
    This is a function to get the cookie, this is created using the streamlit component
    index.js is the javascript file that is used to get the cookie
    :name: name of the cookie
    """
    value = _component_func(name=name, spec=name)
    return value
