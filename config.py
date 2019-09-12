import psycopg2
import logging
import graypy
from slacker import Slacker
from influxdb import DataFrameClient, InfluxDBClient

class Graylog(logging.Logger):

    def __init__(self, level=logging.NOTSET):

        super(Graylog, self).__init__(__name__, level=level)

        self.handler = graypy.GELFUDPHandler('localhost', 12201)
        self.addHandler(self.handler)

PSQL_USER = "postgres"
PSQL_PASS = "82xyPferj"
PSQL_HOST = "10.1.81.81"
#PSQL_HOST = "sensors.star10.tech"
PSQL_PORT = "5433"
PSQL_DB = "orange3"

psql_connection_params = {
    'user': PSQL_USER,
    'password': PSQL_PASS,
    'host': PSQL_HOST,
    'port':PSQL_PORT,
    'database': PSQL_DB
}

graylog = Graylog()
slack = Slacker('xoxb-354180250709-j6J5htjcvnfDbNEImr9JO5aL')
print("Opened influx connection")
df_client = DataFrameClient(host="10.1.81.81", port=8092, username='admin', password='82xyPferj')
influx_client = InfluxDBClient(host="10.1.81.81", port=8092, username='admin', password='82xyPferj')
log_influx_client = InfluxDBClient(host="10.1.161.1", port=8086, username='admin', password='admin')
