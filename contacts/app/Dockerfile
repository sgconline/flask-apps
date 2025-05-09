FROM python:3.11-slim

ENV APP_HOME="/opt/contacts" 
ENV VENV_LOC="/opt/venv" 

WORKDIR ${APP_HOME}
COPY requirements.txt ${APP_HOME}/requirements.txt
COPY bin/entrypoint.sh ${APP_HOME}/
COPY contacts.py ${APP_HOME}/contacts.py
COPY model.py ${APP_HOME}/model.py
COPY .env ${APP_HOME}/.env
COPY templates/ ${APP_HOME}/templates
COPY static/ ${APP_HOME}/static
# COPY db/ ${APP_HOME}/db

RUN python -m venv ${VENV_LOC} && \
${VENV_LOC}/bin/python -m pip install pip --upgrade && \
${VENV_LOC}/bin/python -m pip install -r requirements.txt

RUN chmod +x ./entrypoint.sh
CMD ["./entrypoint.sh"]
