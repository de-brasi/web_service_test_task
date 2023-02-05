# import getpass
# import os

# command = os.getcwd() + '/../venv/bin/gunicorn'
# pythonpath = os.getcwd() + '/first_task'

command = '/home/ilya/WorkSpace/Projects/KASKAD_GROUP_simple_http_service/venv/bin/gunicorn'
pythonpath = '/home/ilya/WorkSpace/Projects/KASKAD_GROUP_simple_http_service/first_task/first_task'

bind = '127.0.0.1:8001'
workers = 3

# user = getpass.getuser()
user = 'ilya'
raw_env = 'DJANGO_SETTINGS_MODULE=first_task.settings'
