FROM python:3.11-slim
RUN apt-get update && apt-get install nginx -y

ENV APP_HOME="/opt/contacts" 
ENV VENV_LOC="${VENV_LOC}" 

COPY src/nginx/default /etc/nginx/sites-available/default
#COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
COPY ./src ${APP_HOME}

WORKDIR ${APP_HOME}
COPY requirements.txt ${APP_HOME}/requirements.txt
COPY src/config ${APP_HOME}/
COPY contacts.py ${APP_HOME}/contacts.py
COPY model.py ${APP_HOME}/model.py
COPY templates/ ${APP_HOME}/templates
COPY static/ ${APP_HOME}/static
COPY db/ ${APP_HOME}/db

RUN python -m venv ${VENV_LOC} && \
${VENV_LOC}/bin/python -m pip install pip --upgrade && \
${VENV_LOC}/bin/python -m pip install -r requirements.txt

RUN chmod +x config/entrypoint.sh
CMD ["./config/entrypoint.sh"]
