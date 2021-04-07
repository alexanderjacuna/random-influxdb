import random
import time
from influxdb import InfluxDBClient

# SET VARUABLES
host = "192.168.1.45"
port = 8086
user = "user"
password = "password" 
dbname = "defaultdb"

# SET MEASUREMENT NAME
measurement = "test"

# CREATE CLIENT OBJECT
client = InfluxDBClient(host, port, user, password, dbname)

if __name__ == "__main__":

	while True:

		# GET RANDOM VALUE
		print("Generating random data...")
		value = random.randint(1,6)

		data = [
		{
		  "measurement": measurement,
			  "fields": {
				  "field" : value
			  }
		  } 
		]

		# WRITE DATA
		print("Sending data...")
		client.write_points(data)

		# SLEEP
		print("Sleeping...")
		time.sleep(5)
