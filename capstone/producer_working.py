import os
from googleapiclient.discovery import build
import json
from kafka import KafkaProducer
from time import sleep
import pandas as pd


def getPlaylistId(userName):
    
    request = youtube.channels().list(
    part = 'contentDetails', 
    forUsername = userName
    )
    try: 
        user = request.execute()
        return(user['items'][0]['contentDetails']['relatedPlaylists']['uploads'])
    except: 
        print(f'ERROR READING VIDEOS FROM: {userName}')


def getVideos(playlistId, numOfVideos=50, page='CDIQAA' ):
    request = youtube.playlistItems().list(
    part = 'contentDetails', 
    playlistId = playlistId,
    maxResults = numOfVideos,
    pageToken = page)
    try:
        videos = request.execute()
        for i in videos['items']: 
            print(i['contentDetails']['videoId'])
        return [vid['contentDetails']['videoId'] for vid in videos['items']]
    except: 
        print(f"ERROR READING SONGS FROM PAGE {page}")
        return []


def getData(videoId):
    request = youtube.videos().list(
    part = 'statistics, snippet',
    id = videoId )
    try: 
        metadata = request.execute()
        stats = metadata['items'][0]['statistics']
        title = metadata['items'][0]['snippet']['title']
        date = metadata['items'][0]['snippet']['publishedAt']
        channelId = metadata['items'][0]['snippet']['channelId']
        try: 
            tags = metadata['items'][0]['snippet']['tags']
        except:
            tags =[]
        return {'stats':stats, 'videoId': videoId, 'channelId': channelId, 'date': date, 'title': title, 'tags':tags}  
#         return(stats,date , title, tags)
    except:
        print("ERROR ------------------")
        return()





if __name__ == "__main__": 

	producer = KafkaProducer(bootstrap_servers=['localhost:9099'],value_serializer=lambda x: json.dumps(x).encode('utf-8'))
	
	api_key = os.environ.get("YOUTUBE_KEY")
	youtube = build('youtube', 'v3', developerKey=api_key)

	users = pd.read_csv('users.csv')
	users = [i[1] for i in users['userName'].items()]

	pl = map(lambda x: getPlaylistId(x), users)
	vids = map(lambda x: getVideos(x,5), pl)

	for col in vids: 
	    for vid in col: 
	        print(vid)
	#         print(json.dumps(getData(vid), indent=4))
	        producer.send('test', json.dumps(getData(vid)))
	        sleep(1)