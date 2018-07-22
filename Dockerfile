FROM tiangolo/uwsgi-nginx-flask:python3.6

# set custom uwsgi
ENV UWSGI_INI /flask_rest_app/uwsgi.ini

# set number of workers as nimber of cpu cores
ENV NGINX_WORKER_PROCESSES auto

COPY ./flask_rest_app /flask_rest_app

RUN pip3 install -r /flask_rest_app/requirements.txt

RUN python3 /flask_rest_app/resetDatabase.py

RUN python3 /flask_rest_app/setup.py develop

WORKDIR /flask_rest_app
