#!/bin/bash
source /home/ilya/WorkSpace/Projects/KASKAD_GROUP_simple_http_service/venv/bin/activate
exec gunicorn -c "/home/ilya/WorkSpace/Projects/KASKAD_GROUP_simple_http_service/first_task/gunicorn_config.py" first_task.wsgi
