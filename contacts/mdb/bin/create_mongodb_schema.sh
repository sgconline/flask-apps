#!/bin/bash
MDB_CMD="mongo"
MDB_USER="mdbadmin"
MDB_PWD="mdbadmin"
MDB_ADDR="localhost"
MDB_PORT=27017
# Compile connection string mongo mongodb://mdbadmin:mdbadmin@localhost
MDB_CONN_STR="${MDB_CMD} ${MDB_CMD}db://${MDB_USER}:${MDB_PWD}@${MDB_ADDR}:${MDB_PORT}"
MDB_JSON_DB="/opt/src/contacts.json"

if which ${MDB_CMD}; then
${MDB_CONN_STR} <<EOF
use contacts_db
db.createCollection("contacts")
exit
EOF
# Import data from a JSON file

MDB_IMP="${MDB_CMD}import"
# Compile connection string 
# mongoimport mongodb://mdbadmin:mdbadmin@localhost:27017/contacts_db --collection contacts --jsonArray --type json --file contacts.json --authenticationDatabase admin
MDB_CONN_STR="${MDB_IMP} ${MDB_CMD}db://${MDB_USER}:${MDB_PWD}@${MDB_ADDR}:${MDB_PORT}"
echo "${MDB_CONN_STR}/contacts_db --collection contacts --jsonArray --type json --file ${MDB_JSON_DB} --authenticationDatabase admin"
${MDB_CONN_STR}/contacts_db --collection contacts --jsonArray --type json --file ${MDB_JSON_DB} --authenticationDatabase admin
else echo "Cannot locate mongo command"
     exit 1
fi
