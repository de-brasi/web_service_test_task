#!/bin/bash

#The script must be run inside a django application (not a project)!
#Example:
#      <Django project>
#      ├── <Django app> - sh script must be run here!
#      │         ├── bin
#      │         │   └── start_gunicorn.sh
#      │         ├── db.sqlite3
#      │         ├── first_task
#      │         ├── gunicorn_config.py
#      │         ├── json_getter
#      │         ├── manage.py
#      │         └── __pycache__
#      └── <Your virtualenv> - should named as "venv"
#          ├── bin
#          ├── lib
#          └── pyvenv.cfg

source $(pwd)/../venv/bin/activate
gunicorn -c "$(pwd)/gunicorn_config.py" first_task.wsgi