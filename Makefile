volumes:
	docker volume create --name=influxdbdistribution-volume
	docker volume create --name=flaskdistribution-volume

run-detached:
	docker-compose up -d

run:
	docker-compose up

connect-db:
	psql -h 0.0.0.0 -p 8292 -U postgres