FROM mongodb/mongodb-community-server:4.4.18-ubi8

ENV APP_HOME="/data"

WORKDIR ${APP_HOME}
ENV MONGODB_INITDB_ROOT_USERNAME=mdbadmin
ENV MONGODB_INITDB_ROOT_PASSWORD=mdbadmin

COPY src/contacts.json ${APP_HOME}/src/contacts.json
COPY bin/ ${APP_HOME}/bin/
# Copy the initialization script to the container's init directory
#COPY bin/mongo-init.js /docker-entrypoint-initdb.d/
COPY bin/create_mongodb_schema.sh /docker-entrypoint-initdb.d/

