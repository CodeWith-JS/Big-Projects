document.addEventListener("DOMContentLoaded", () => {

    const token = localStorage.getItem("token");
    const userData = localStorage.getItem("user");

    // ----------------------------------------
    // Check authentication
    // ----------------------------------------

    if (!token || !userData) {

        window.location.href = "/login.html";

        return;
    }


    let user;

    try {

        user = JSON.parse(userData);

    } catch (error) {

        console.error(
            "Invalid user data:",
            error
        );

        localStorage.removeItem("user");
        localStorage.removeItem("token");

        window.location.href = "/login.html";

        return;
    }


    // ----------------------------------------
    // Prevent admin from accessing user page
    // ----------------------------------------

    if (user.role === "admin") {

        window.location.href =
            "/admin-dashboard.html";

        return;
    }


    // ----------------------------------------
    // User initials
    // ----------------------------------------

    const name =
        user.name || "User";

    const initials =
        name
            .split(" ")
            .map(word => word.charAt(0))
            .join("")
            .substring(0, 2)
            .toUpperCase();


    // ----------------------------------------
    // Helper
    // ----------------------------------------

    function setText(id, value) {

        const element =
            document.getElementById(id);

        if (element) {

            element.textContent =
                value || "—";
        }
    }


    // ----------------------------------------
    // Update UI
    // ----------------------------------------

    setText(
        "sidebarName",
        user.name
    );

    setText(
        "sidebarRole",
        user.role
            ? user.role.toUpperCase()
            : "USER"
    );

    setText(
        "topbarName",
        user.name
    );

    setText(
        "profileName",
        user.name
    );

    setText(
        "profileEmail",
        user.email
    );

    setText(
        "profileRole",
        user.role
            ? user.role.toUpperCase()
            : "USER"
    );


    // ----------------------------------------
    // Avatar
    // ----------------------------------------

    setText(
        "sidebarAvatar",
        initials
    );

    setText(
        "topAvatar",
        initials
    );

    setText(
        "heroAvatar",
        initials
    );


    // ----------------------------------------
    // Logout
    // ----------------------------------------

    function logout() {

        localStorage.removeItem("token");

        localStorage.removeItem("user");

        window.location.href =
            "/login.html";
    }


    const logoutBtn =
        document.getElementById("logoutBtn");

    const accountLogout =
        document.getElementById("accountLogout");


    if (logoutBtn) {

        logoutBtn.addEventListener(
            "click",
            logout
        );

    }


    if (accountLogout) {

        accountLogout.addEventListener(
            "click",
            logout
        );

    }


    // ----------------------------------------
    // Navigation active state
    // ----------------------------------------

    const navItems =
        document.querySelectorAll(".nav-item");


    navItems.forEach(item => {

        item.addEventListener("click", () => {

            navItems.forEach(nav => {

                nav.classList.remove("active");

            });

            item.classList.add("active");

        });

    });

});