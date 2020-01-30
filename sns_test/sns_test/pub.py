import boto3, time, json, logging
from datetime import datetime

logging.basicConfig(filename="sns-publish.log", level=logging.DEBUG)

""" Connect to SNS """
client = boto3.client('sns')

""" Send 100 messages """
for x in range(100):

    message = str(x)
    pub = client.publish(
                TopicArn="arn:aws:sns:eu-west-3:xxxxx:pub",
                Message=message,
            )    


    m = json.loads(json.dumps(pub, ensure_ascii=False))


    message_id = m["MessageId"]

    print (str(datetime.now()) + " - Message Number " + message + " - With ID " + message_id)
    time.sleep(0)






