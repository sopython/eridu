import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='docker.local',
        port=5672))
channel = connection.channel()

channel.exchange_declare(exchange='eridu',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_key = 'posts.#'

print(' [*] Waiting for logs. To exit press CTRL+C')

channel.queue_bind(exchange='eridu',
                   queue=queue_name,
                   routing_key=binding_key)


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
