// cookie_component.js

function getCookie(event) {
    data = event.detail;
    name = data.args.spec;
    console.log("Getting cookie:", name);
    const cookieArr = document.cookie.split(";");
    for (const cookiePair of cookieArr) {
        const [key, value] = cookiePair.split("=");
        if (name === key.trim()) {
            console.log("Cookie found:", value);
            Streamlit.setComponentValue(value);
        }
    }
    return null;
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, getCookie)
Streamlit.setComponentReady()
