import boto3
import requests
from json import dumps
import json 
import time
client = boto3.client(
    'kinesis',
    region_name='us-east-2',
    aws_access_key_id='AKIASKZVWKQSM3X4UWXT',
    aws_secret_access_key='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'
)

myheaders = {
	"x-rapidapi-host": "yelp-com.p.rapidapi.com",
	"x-rapidapi-key": "a3a614c81amsh073c1eec7f17981p1184abjsn91eba527a088",
	"useQueryString": 'true'
}

x= requests.get('https://yelp-com.p.rapidapi.com/business/DAiqwrmv19Uv-I1bOoAJCQ', headers=myheaders)
t = x.json()
print(json.dumps(t))
print(t)

time.sleep(2)
client.put_record(StreamName='yelpTest', Data=json.dumps(t).encode('utf-8'), PartitionKey='1')
