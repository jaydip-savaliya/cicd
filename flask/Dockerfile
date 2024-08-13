FROM python:3.10
WORKDIR /app
COPY flask/requirements.txt .
RUN apt-get update
RUN pip install -r requirements.txt
RUN pip install uwsgi
COPY ./flask .
CMD [ "uwsgi","--ini","app.ini"]