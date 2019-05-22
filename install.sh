apt-get update
apt-get install python3 docker docker-compose
service docker restart
python3 -m pip install -r requirements.txt
python3 run.py
