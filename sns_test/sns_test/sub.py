import boto3, time, json
import os
from datetime import datetime

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='sub')


""" Process messages by printing out body """

while 1:
    for message in queue.receive_messages():
        print('%s ' % json.loads(message.body)["Message"]  )
        message.delete()
