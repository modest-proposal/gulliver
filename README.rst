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

Docker
------

To build a Docker image, use the command::

  docker build -t gulliver_docker .

To run the Docker image, use the command::

  docker run -it --rm -p 6543:80 gulliver_docker

After that, the application should be available at the address
``http://localhost:6543``.
