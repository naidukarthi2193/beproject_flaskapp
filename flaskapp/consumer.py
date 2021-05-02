import pika
import os


def consumer(connection):
    try:
        channel = connection.channel()  # start a channel
        channel.queue_declare(queue='TestQueue')  # Declare a queue

        def callback(ch, method, properties, body):
            print(" [x] Received " + str(body))

        channel.basic_consume('TestQueue',
                              callback,
                              auto_ack=True)

        print(' [*] Waiting for messages:')
        channel.start_consuming()
    except Exception as e:
        print("RABBIT ERROR", e)
