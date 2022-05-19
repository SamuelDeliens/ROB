function checkPrivileges() {
    getCookies();
    document.right = false;
    if(document.cookies["Bluerov_Log"] != "invite") {
        document.right = true;
    }
}

function getCookies() {
    document.cookies = decodeURIComponent(document.cookie).replace(/\s+/g, '').split(';');
    let cookie = {};
    for(i=0; i<document.cookies.length; i++) {
        cookie[document.cookies[i].split("=")[0]] = document.cookies[i].split("=")[1];
    }
    document.cookies = cookie;
}

