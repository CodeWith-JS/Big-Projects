const express = require("express");
const cors = require("cors");
const path = require("path");
require("dotenv").config();

const authRoutes = require("./routes/authRoutes");

const app = express();
const PORT = process.env.PORT || 5000;

// =====================================
// Middleware
// =====================================

app.use(cors());

app.use(express.json());


// =====================================
// Serve FRONTEND
// =====================================

const frontendPath = path.join(
    __dirname,
    "../frontend"
);

console.log("Frontend path:", frontendPath);

app.use(
    express.static(frontendPath)
);


// =====================================
// API ROUTES
// =====================================

app.use(
    "/api/auth",
    authRoutes
);


// =====================================
// ROOT
// =====================================

app.get("/", (req, res) => {

    res.sendFile(
        path.join(
            frontendPath,
            "login.html"
        )
    );

});


// =====================================
// SERVER
// =====================================

app.listen(
    PORT,
    "0.0.0.0",
    () => {

        console.log(
            `Server running on http://localhost:${PORT}`
        );

    }
);