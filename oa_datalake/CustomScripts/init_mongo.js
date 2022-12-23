use staging
db.createCollection("locations");

db.createUser(
    {
        user: "user",
        pwd: "password123",
        roles: [
            {
                role: "readWrite",
                db: "staging"
            }
        ]
    }
);


