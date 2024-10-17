import streamlit.components.v1 as components
_component_func = components.declare_component(f"cookie_comp", path="cookie_component",)


def cookie_manager(name, action, value=None, days=1):
    """
    This is a function to get the cookie, this is created using the streamlit component
    index.js is the javascript file that is used to get the cookie
    :name: name of the cookie
    """
    value = _component_func(spec={"name": name, "action": action, "value": value, "days": days})
    return value
