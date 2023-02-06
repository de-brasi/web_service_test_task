pip install --quiet virtualenv
virtualenv venv
source venv/bin/activate
pip install --quiet -r requirements.txt
cd ./first_task
. ./bin/start_gunicorn.sh

