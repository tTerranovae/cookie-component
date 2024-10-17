import streamlit.components.v1 as components

_component_func = components.declare_component(
    f"cookie_comp",
    path="cookie_component",
)


def cookie_manager(name, action="get", value=None, days=1):
    """
    This is a function to get the cookie, this is created using the streamlit component
    index.js is the javascript file that is used to get the cookie
    :name: name of the cookie
    """
    if action not in ["get", "set"]:
        raise ValueError("Invalid action. Action must be 'get' or 'set'.")
    value = _component_func(
        spec={"name": name, "action": action, "value": value, "days": days}
    )
    return value
