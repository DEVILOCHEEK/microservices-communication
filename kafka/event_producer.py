# kafka/event_producer.py
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('user-actions', b'user_logged_in')
producer.flush()
