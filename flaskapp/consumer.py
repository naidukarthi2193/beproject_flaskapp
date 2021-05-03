import pika
import os
import json
from firebase_admin import credentials, firestore, initialize_app

from google.cloud.firestore import ArrayUnion
db = firestore.client()


def consumer(connection):
    try:
        channel = connection.channel()  # start a channel
        channel.queue_declare(queue='TestQueue')  # Declare a queue

        def callback(ch, method, properties, body):
            print("Received " + str(body))
            body = body.decode('utf8').replace("'", '"')
            data = json.loads(body)
            attention_ref = db.collection(
                'attention').document(data["lecture_id"])
            attention_ref.update(
                {data["email"]: ArrayUnion([data])})

        channel.basic_consume('TestQueue',
                              callback,
                              auto_ack=True)

        print('Waiting for messages')
        channel.start_consuming()

    except Exception as e:
        print("RABBIT ERROR", e)
        raise Exception(e)
