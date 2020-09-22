#!/usr/bin/env python
import pika
import sys

class EmitBroker():

    def __init__(self, host, routing_key, message):
        self.host = host
        self.routing_key = routing_key
        self.message = message

    def publish(self):
        # Establishes connection with Rabbit MQ
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host))
        channel = connection.channel()

        # Creates (if it doesn't already exist) a exchange named 'BROKER' and with the type 'topic'
        channel.exchange_declare(exchange='BROKER', exchange_type='topic')

        # Sends message with the routing key to the exchange named 'BROKER'
        channel.basic_publish(
            exchange='BROKER', routing_key=self.routing_key, body=self.message)
        print(" [x] Sent %r:%r" % (self.routing_key, self.message))

        # Terminate connection
        connection.close()