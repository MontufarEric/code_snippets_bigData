import boto3
import requests
from json import dumps
import json 
import time
client = boto3.client(
    'kinesis',
    region_name='us-east-2',
    aws_access_key_id='',
    aws_secret_access_key=''
)

myheaders = {
	"x-rapidapi-host": "yelp-com.p.rapidapi.com",
	"x-rapidapi-key": "",
	"useQueryString": 'true'
}

x= requests.get('https://yelp-com.p.rapidapi.com/business/', headers=myheaders)
t = x.json()
print(json.dumps(t))
print(t)

time.sleep(2)
client.put_record(StreamName='yelpTest', Data=json.dumps(t).encode('utf-8'), PartitionKey='1')
