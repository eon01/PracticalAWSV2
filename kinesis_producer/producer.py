import boto3
import json
import requests
import time

url = "https://pokeapi.co/api/v2/pokemon/"
stream = "KinesisStream"
partition_key = "name"

kinesis_client = boto3.client('kinesis', region_name='eu-west-3')


while 1:
    for pokemon in range(1,10):
        route = url + str(pokemon)

        # resp type is byte
        resp = requests.get(route)

        kinesis_client.put_record(
                            StreamName=stream,
                            Data=json.dumps(resp.content.decode('utf8')),
                            PartitionKey=partition_key)
