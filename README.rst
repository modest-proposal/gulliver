To build the Docker image, use the command::

  docker build -t gulliver_docker .

To run the Docker image, use the command::

  docker run -it --rm -p 8000:80 gulliver_docker

After that, the application should be available at the address
"http://localhost:8000".
