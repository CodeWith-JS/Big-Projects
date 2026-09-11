const express = require("express");

const db = require("../config/db");

const authMiddleware =
    require("../middleware/authMiddleware");

const adminMiddleware =
    require("../middleware/adminMiddleware");


const router = express.Router();


router.get(
    "/users",
    authMiddleware,
    adminMiddleware,

    async (req, res) => {

        try {

            const [users] = await db.execute(
                `SELECT
                    id,
                    name,
                    email,
                    role,
                    created_at
                 FROM users
                 ORDER BY created_at DESC`
            );


            res.json({
                users
            });


        } catch (error) {

            console.error(
                "Admin users error:",
                error
            );


            res.status(500).json({
                message: "Server error"
            });

        }

    }
);


module.exports = router;