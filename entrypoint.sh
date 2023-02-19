# start the flask app
gunicorn -b :8011 wsgi:app