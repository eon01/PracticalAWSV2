import boto3
import time

stream = "KinesisStream"
partition_key = "my_key"

# Connect to Kinesis
kinesis_client = boto3.client('kinesis', region_name='eu-west-3')

# Inspecting the stream
response = kinesis_client.describe_stream(StreamName=stream)

# Get the shard ID
my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

# Create a shard iterator with the type LATEST
shard_iterator = kinesis_client.get_shard_iterator(
									StreamName=stream,
                                    ShardId=my_shard_id,
                                    ShardIteratorType='LATEST')


my_shard_iterator = shard_iterator['ShardIterator']

# Get the record using the shard iterators
record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator)

# Iterating through the next shard iterators
# Each data record can be up to 1 MiB in size, and each shard can read up to 2 MiB per second.
# You can ensure that your calls don't exceed the maximum supported size or throughput
# by using the Limit parameter to specify the maximum number of records that GetRecords can return.
while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(
    								ShardIterator=record_response['NextShardIterator'],
                                    Limit=2)

	# printing the result to the screen
    print(record_response)

    # sleeping for 3 seconds
    time.sleep(3)
