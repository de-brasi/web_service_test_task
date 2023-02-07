## Technologies
- Python
- Django
- gunicorn (WSGI)
## API
    
- / - Hello world
- /getparamval - JSON [
{"p": "1:2:3:4", "v": "1,234"},
            ...,
            {"p": "1:2:3:99", "v": "1,234"}
        ]
## Installation and launch
### Quick start:
```shell
git clone git@github.com:de-brasi/web_service_test_task.git
. ./start.sh
```
### Manual start:
Download source code:
```shell
git clone git@github.com:de-brasi/web_service_test_task.git
```

Install virtualenv:
```shell
pip install virtualenv
```

Create virtual environment:
```shell
virtualenv venv
source venv/bin/activate
```

Download required dependencies:
```shell
pip install -r requirements.txt
```

Run WSGI-server:
```shell
cd ./first_task
#. ./bin/start_gunicorn.sh
source $(pwd)/../venv/bin/activate
gunicorn -c "$(pwd)/gunicorn_config.py" first_task.wsgi
```