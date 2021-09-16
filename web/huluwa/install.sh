
# tested  on mac 
sudo python -m ensurepip
sudo python -m pip install Django

sudo pip3 install gunicorn
# sudo gunicorn huluwa.wsgi -b 127.0.0.1:80
sudo gunicorn huluwa.wsgi -b 0.0.0.0:80

