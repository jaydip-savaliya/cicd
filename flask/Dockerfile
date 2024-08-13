FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN apt-get update
RUN pip install -r requirements.txt
RUN pip install uwsgi
COPY . .
CMD [ "uwsgi","--ini","app.ini"]