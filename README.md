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
. ./start.sh
```
### Manual start:
Install virtualenv:
```shell
pip install virtualenv
```

Create virtual environment:
```shell
virtualenv venv
```

Download required dependencies:
```shell
pip install -r requirements.txt
```

Run WSGI-server:
```shell
cd ./first_task
. ./bin/start_gunicorn.sh
```