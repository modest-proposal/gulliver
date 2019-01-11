Installation
------------

Install Python 3.6+ and `Poetry <https://poetry.eustace.io/>`_.

Clone the repository::

  git clone https://github.com/modest-proposal/gulliver.git

Install::

  poetry install

Run::

  poetry run gunicorn --paste development.ini

The application will be available at the address: ``http://localhost:6543/``.

PostgreSQL
----------

By default, the development setup will store the data in the ``Data.fs``
file. If you want to use PostgreSQL for data storage, change the
``zodbconn.uri`` setting in the ``development.ini`` file.

The recommended way for working with PostgreSQL is via Docker::

  docker pull postgres

To store the data outside the Docker container, create a folder
(say ``$HOME/docker/volumes/postgres``) and mount it as a volume::

  docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres

After starting the Docker container with the above command and changing
the ``development.ini`` file as described, the application can be started
as before::

  poetry run gunicorn --paste development.ini

Docker
------

To build a Docker image, use the commands::

  poetry build
  docker build -t gulliver-docker .

To run the Docker image, use the command::

  docker run -it --rm -p 6543:80 gulliver-docker

After that, the application should be available at the address
``http://localhost:6543``.
