# django-rest-boilerplate

A simple boilerplate Django Rest project that includes all the necessary packages for authentication and registration.
Also supports PostgreSQL, webpack and Gunicorn. Comes with a ready-made landing page.

```
# initialize virtual environment
virutalenv venv
. venv/bin/activate

# install dependencies
pip3 install -r requirements.txt
npm install

# run migrations
python3 manage.py migrate

# run server (make sure to restart virtual environment)
gunicorn website.wsgi

# to use webpack, include these lines in templates
{% load render_bundle from webpack_loader %}
{% render_bundle 'main' %}

# run webpack once
./node_modules/.bin/webpack --config webpack.config.js

# run webpack in background
./node_modules/.bin/webpack --config webpack.config.js --watch
```
