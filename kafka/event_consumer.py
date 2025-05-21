from kafka import KafkaConsumer
consumer = KafkaConsumer('user-actions', bootstrap_servers='localhost:9092')
for msg in consumer:
    print("Event received:", msg.value.decode())
