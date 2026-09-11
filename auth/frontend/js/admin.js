const token = localStorage.getItem("token");
const storedUser = localStorage.getItem("user");


// ==========================================
// CHECK LOGIN
// ==========================================

if (!token || !storedUser) {

    window.location.href = "login.html";

}


// ==========================================
// PARSE USER
// ==========================================

let user;

try {

    user = JSON.parse(storedUser);

} catch (error) {

    localStorage.removeItem("token");
    localStorage.removeItem("user");

    window.location.href = "login.html";

}


// ==========================================
// CHECK ADMIN
// ==========================================

if (!user || user.role !== "admin") {

    alert("Admin access denied.");

    window.location.href = "dashboard.html";

}


// ==========================================
// DISPLAY USER
// ==========================================

const welcomeName =
    document.getElementById("welcomeName");

const sidebarName =
    document.getElementById("sidebarName");


if (welcomeName) {

    welcomeName.textContent =
        user.name;

}


if (sidebarName) {

    sidebarName.textContent =
        user.name;

}


// ==========================================
// LOGOUT
// ==========================================

const logoutBtn =
    document.getElementById("logoutBtn");


logoutBtn.addEventListener(
    "click",
    () => {

        localStorage.removeItem("token");

        localStorage.removeItem("user");

        window.location.href =
            "login.html";

    }
);