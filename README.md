# python-flask-docker
Basic Python Flask rest and web app in Docker

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/parm-ameotech/flask-python-docker
$ docker build -t python-flask-docker .
```

### Download precreated image
You can also just download the existing image from [DockerHub](https://hub.docker.com/r/parm-ameotech/flask-python-docker/).
```
docker pull python-flask-docker
```

### Run the container
Create a container from the image.
```
$ docker run --name my-container -d -p 8080:8080 flask-python-docker
```

Now visit http://localhost:8080
```
 The hostname of the container is 6095273a4e9b and its IP is 172.17.0.2. 
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-container
172.17.0.2
$ docker inspect -f '{{ .Config.Hostname }}' my-container
6095273a4e9b
```

