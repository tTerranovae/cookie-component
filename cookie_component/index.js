// cookie_component.js

function cookieManager(event) {
    data = event.detail;
    const { name, action, value, days } = data.args.spec;
    if (action === "get") {
        getCookie(name);
    } else if (action === "set") {
        setCookie(name, value, days);
    }
}
function getCookie(name) {
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

function setCookie(name, value, days) {
    console.log("Setting cookie:", name, value, days);
    let expires = "";
    if (days) {
        let date = new Date();
        date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + encodeURIComponent(value) + expires + "; path=/";
}


Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, cookieManager)
Streamlit.setComponentReady()
