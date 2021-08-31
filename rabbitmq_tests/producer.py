import datetime

import pika

RABBIT_URL = "amqp://guest:guest@localhost:5672/local"

connection = pika.BlockingConnection(pika.URLParameters(RABBIT_URL))

channel = connection.channel()

# Create exchange
channel.exchange_declare(exchange="stock", exchange_type="fanout")

# Publish on exchange
message = f"Message {datetime.datetime.now()}"

channel.basic_publish(exchange="stock", routing_key="", body=message)

print(f" [x] Sent: {message}")

connection.close()
