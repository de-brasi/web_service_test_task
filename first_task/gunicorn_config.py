import os, getpass

command = os.getcwd() + '/../venv/bin/gunicorn'
pythonpath = os.getcwd() + '/first_task'
bind = '127.0.0.1:8001'
workers = 3
user = getpass.getuser()
raw_env = 'DJANGO_SETTINGS_MODULE=first_task.settings'
