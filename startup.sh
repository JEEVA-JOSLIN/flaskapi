apt-get update
apt-get install -y libmagic1
apt-get install build-essential
apt-get install python3-dev
apt-get install libjpeg-dev
gunicorn --workers 3 --bind 0.0.0.0:8000 app:app
