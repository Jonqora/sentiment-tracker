#!/bin/bash
set -e
export FLASK_APP=./src/main.py
export FLASK_DEBUG=1
flask run -h 0.0.0.0  # --port 5555