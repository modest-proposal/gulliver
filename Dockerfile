FROM python:3.7.1-stretch
WORKDIR /gulliver
RUN pip install poetry
COPY . /gulliver
RUN poetry build
RUN pip install dist/gulliver*whl
RUN pip install gunicorn
EXPOSE 80
ENTRYPOINT gunicorn --paste production.ini
