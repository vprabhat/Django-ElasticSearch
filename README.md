# A basic implementation of ElasticSearch with Django. Only Filter query has been used in this project.

# Pre-requisites --
## Make sure you have java installed or set JAVA_HOME environment variable
## Install virtualenv and virtualenv-wrapper using pip
```
pip install virtualenv virtualenvwrapper
```
## Install fabric
```
sudo apt-get install fabric
```
## Install openssh-server
```
sudo apt-get install openssh-server
```
## add your public key
```
ssh-add
```
## Make sure
```
ssh localhost
```
command works


# Next Steps --
## Go to home folder
```
cd ~
```
## Clone the repository to your home (/home/username/) folder (This is necessary)
```
git clone https://github.com/vprabhat/Django-ElasticSearch.git
```
## Go to project directory
```
cd ~/Django-ElasticSearch/
```
## Do Initial Setup --
```
fab setup_app:<username>,<path to python3> -H localhost -u <username>
``` 
(Please do not do this as root user)
		example:
```
fab setup_app:vprabhat,/usr/bin/python3 -H localhost -u vprabhat
```
## Run ES server to check if its working
```
elasticsearch-6.1.1/bin/elasticsearch
```
## Goto localhost:9200 to check if its working. If it does, close it and run it in background
```
elasticsearch-6.1.1/bin/elasticsearch -d
```
## Enter django app dir
```
cd es_filter
```
## Activate virtualenv created in setup_app step
```
source /home/<username>/.virtualenvs/venv/bin/activate
```
## Run Server to check Furniture models (localhost:8000/admin) and close (optional)
```
python manage.py runserver 0.0.0.0:8000
```
## Push Indices for all furniture models to es-server
```
python manage.py push_indices
```
## Run server again
```
python manage.py runserver 0.0.0.0:8000
```
### Goto localhost:8000/esa/home to test filtering (This is only for SOFA category. And doesn't include pricing. You can include pricing in API testing)
