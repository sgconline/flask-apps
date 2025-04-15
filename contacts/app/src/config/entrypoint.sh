#!/bin/bash
RUN_PORT="8000"
/opt/venv/bin/gunicorn contacts:app --bind "0.0.0.0:${RUN_PORT}" # --daemon

