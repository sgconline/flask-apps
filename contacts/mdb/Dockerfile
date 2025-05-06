FROM mongodb/mongodb-community-server:4.4.18-ubi8

ENV APP_HOME="/data"

WORKDIR ${APP_HOME}
ENV MONGODB_INITDB_ROOT_USERNAME=mdbadmin 
ENV MONGODB_INITDB_ROOT_PASSWORD=mdbadmin 
# RUN chown mongod:mongod ${APP_HOME}
# RUN chmod 777 ${APP_HOME}
# RUN mkdir -p ${APP_HOME}/bin
# RUN mkdir -p ${APP_HOME}/src
COPY src/contacts.json ${APP_HOME}/src/contacts.json
COPY bin/create_mongodb_schema.sh ${APP_HOME}/bin/create_mongodb_schema.sh
RUN /bin/bash ${APP_HOME}/bin/create_mongodb_schema.sh 

