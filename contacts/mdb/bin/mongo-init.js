db.createUser({
    user: "mdbadmin",
    pwd: "mdbadmin",
    roles: [{
        role: "readWrite",
        db: "contacts_db",
	collection: "contacts"
    }]
});
