Rename the file `settings_default.py` to `settings.py` and change the `SECRET_KEY`

`gunicorn --bind 0.0.0.0:8000 --workers 3 app.wsgi.application`