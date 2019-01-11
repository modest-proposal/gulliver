FROM python:3.6.8-stretch
WORKDIR /gulliver
COPY ./dist production.ini /gulliver/
RUN pip install gulliver*whl
RUN pip install gunicorn
EXPOSE 80
ENTRYPOINT gunicorn --paste production.ini
