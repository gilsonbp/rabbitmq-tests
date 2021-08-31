import sys

import pika

RABBIT_URL = "amqp://guest:guest@localhost:5672/local"

connection = pika.BlockingConnection(pika.URLParameters(RABBIT_URL))

channel = connection.channel()

# Create exchange
channel.exchange_declare(exchange="stock", exchange_type="fanout")

# Create randon queue
result = channel.queue_declare(queue="stock_process_product")
queue_name = result.method.queue

channel.queue_bind(exchange="stock", queue=queue_name)

print(" [*] Waiting for stocks. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
