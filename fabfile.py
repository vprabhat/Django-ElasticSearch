from fabric.api import *

@task
def setup_app(username, python_path):
    run('rm -rf /home/%s/Django-ElasticSearch/elasticsearch-6.1.1'%username, warn_only=True)
    run('tar -xvf /home/%s/Django-ElasticSearch/elasticsearch-6.1.1.tar.gz -C /home/%s/Django-ElasticSearch/'%(username, username))
    run('mkdir /home/%s/.virtualenvs'%username, warn_only=True)
    run('rm -rf /home/%s/.virtualenvs/venv'%username, warn_only=True)
    run('mkdir /home/%s/Django-ElasticSearch/elasticsearch-6.1.1/plugins'%username, warn_only=True)
    run('rm /home/%s/Django-ElasticSearch/es_filter/db.sqlite3'%username, warn_only=True)
    run('virtualenv -p %s /home/%s/.virtualenvs/venv'%(python_path, username), warn_only=True)
    run('/home/%s/.virtualenvs/venv/bin/pip install -r /home/%s/Django-ElasticSearch/es_filter/requirements.txt'%(username, username))
    run('/home/%s/.virtualenvs/venv/bin/python /home/%s/Django-ElasticSearch/es_filter/manage.py migrate'%(username, username))
    run('/home/%s/.virtualenvs/venv/bin/python /home/%s/Django-ElasticSearch/es_filter/manage.py createsuperuser'%(username, username))
    run('/home/%s/.virtualenvs/venv/bin/python /home/%s/Django-ElasticSearch/es_filter/manage.py populate_furnitures'%(username, username))
    run('echo "Inital set-up done. Please follow further instructions"')
