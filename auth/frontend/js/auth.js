const API_URL = "http://localhost:5000/api";

const loginForm = document.getElementById("loginForm");
const message = document.getElementById("message");

loginForm.addEventListener("submit", async (e) => {

    e.preventDefault();

    const email =
        document.getElementById("email").value.trim();

    const password =
        document.getElementById("password").value;

    message.textContent = "Signing in...";

    try {

        const response = await fetch(
            `${API_URL}/auth/login`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    email,
                    password
                })
            }
        );

        const data = await response.json();

        console.log("LOGIN RESPONSE:", data);

        if (!response.ok) {

            message.textContent =
                data.message || "Login failed";

            return;
        }

        // Check that backend actually returned JWT
        if (!data.token) {

            console.error(
                "No token received:",
                data
            );

            message.textContent =
                "Login succeeded but server did not return a token.";

            return;
        }

        // Check user object
        if (!data.user) {

            console.error(
                "No user received:",
                data
            );

            message.textContent =
                "Login succeeded but server did not return user information.";

            return;
        }

        // Save authentication
        localStorage.setItem(
            "token",
            data.token
        );

        localStorage.setItem(
            "user",
            JSON.stringify(data.user)
        );

        console.log("USER:", data.user);
        console.log("ROLE:", data.user.role);

        message.textContent =
            "Login successful!";

        // Role-based redirect
        if (data.user.role === "admin") {

            window.location.href =
                "/admin-dashboard.html";

        } else {

            window.location.href =
                "/user-dashboard.html";
        }

    } catch (error) {

        console.error(
            "LOGIN ERROR:",
            error
        );

        message.textContent =
            "Unable to connect to server.";
    }
});