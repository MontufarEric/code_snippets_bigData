from kafka import KafkaConsumer
from json import loads

f = open('/home/fieldengineer/Documents/011_kafka/Kafka_Shakespeare.txt','w')
consumer = KafkaConsumer( 'bigdata', bootstrap_servers=['localhost:9099'], auto_offset_reset='earliest')

for message in consumer:
	message = message.value
	f.write(message.decode("utf-8"))


f.close()

