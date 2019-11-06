# python-flask-docker
Basic Python Flask rest and web app in Docker

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/parm-ameotech/flask-python-docker
$ docker build -t flask-python-docker .
```

### Download precreated image
You can also just download the existing image from [DockerHub](https://hub.docker.com/r/parm-ameotech/flask-python-docker/).
```
docker pull flask-python-docker
```

### Run the container
Create a container from the image.
```
$ docker run --name my-container -d -p 8080:8080 flask-python-docker
```

Now visit http://localhost:8080


