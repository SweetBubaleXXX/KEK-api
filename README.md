# KEK-api
![Python](https://img.shields.io/badge/Python->=3.7-orange)
![gnukek](https://img.shields.io/badge/gnukek-==1.0.0-yellow)

----------

Public [KEK](https://pypi.org/project/gnukek/) encryption API.

----------

## Deployment

Install requirements:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn app.main:app --host {HOST} --port {PORT}
```

Or:

```bash
python app/main.py
```

> You can specify 'HOST' and 'PORT' environment variables


## License

[GPLv3 license](https://github.com/SweetBubaleXXX/KEK-api/blob/main/LICENSE)
