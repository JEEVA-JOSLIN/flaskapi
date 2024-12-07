apt-get update
apt-get install -y libmagic1
gunicorn --bind 0.0.0.0:8000 app:app
