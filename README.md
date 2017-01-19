# django-rest-boilerplate

A simple boilerplate Django Rest project that includes all the necessary packages for authentication and registration.
Also supports PostgreSQL and Gunicorn. Comes with a ready-made landing page.

```
# initialize virtual environment
virutalenv venv
. venv/bin/activate

# install dependencies
pip3 install -r requirements.txt
npm install

# run server
gunicorn website.wsgi

# run webpack in background
./node_modules/.bin/webpack --config webpack.config.js --watch
```
