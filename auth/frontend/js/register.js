const registerForm = document.getElementById("registerForm");

registerForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword =
        document.getElementById("confirmPassword").value;

    const message = document.getElementById("message");

    // Check password match
    if (password !== confirmPassword) {
        message.textContent = "Passwords do not match.";
        return;
    }

    // Check password length
    if (password.length < 6) {
        message.textContent =
            "Password must contain at least 6 characters.";
        return;
    }

    message.textContent = "Creating account...";

    try {
        const response = await fetch(
            "http://localhost:5000/api/auth/register",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    name,
                    email,
                    password
                })
            }
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.message || "Registration failed"
            );
        }

        message.textContent =
            "Account created successfully!";

        // Redirect to login
        setTimeout(() => {
            window.location.href = "login.html";
        }, 1200);

    } catch (error) {
        console.error("Registration error:", error);

        message.textContent =
            error.message || "Unable to connect to server.";
    }
});