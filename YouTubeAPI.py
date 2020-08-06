# // == Lines needed to calculate playlist duration
# importing regular expressions module
#import re //
# import time delta
#from datetime import timedelta //
# Build the service Object
from googleapiclient.discovery import build
# Placement of API key
api_key = 'Your key goes here.'
# Connect to youtube service
youtube = build('youtube', 'v3', developerKey=api_key)

# regular expression complier to capture more than one digit that lead to H
#hours_pattern = re.compile(r'(\d+)H') //
# regular expression complier to capture more than one digit that lead to M
#minutes_pattern = re.compile(r'(\d+)M') //
# regular expression complier to capture more than one digit that lead to S
#seconds_pattern = re.compile(r'(\d+)S') //

#total_seconds = 0 //

# clear variable for the Id.
playlist_id = "PL8uoeex94UhHFRew8gzfFJHIpRFWyY4YW"

# Adding vid_ids to this list, sorting list based on number of views
# adding view count, and link, each video will be dictionary with each piece of info
videos = []

# setting nextPageToken to none so when the while loop starts, first page only
nextPageToken = None
while True:

	# playlist request
	pl_request = youtube.playlistItems().list(
			# which part of data you wish to call upon
			part='contentDetails',
			# playlistId
			playlistId=playlist_id,
			# max results
			maxResults=50,
			# to let api know what page of results we are on.
			pageToken=nextPageToken

	# You can also add content Details to gather Id from them. 
	# Returns a resource for the API route using youtube service
	#request = youtube.channels().list(
			# How to look up stats for a channel
	#		part='contentDetails, statistics',
			# What channel we are getting stats for
	#		forUsername='schafer5'
	# print(response) at the bottom****
		)

	pl_response = pl_request.execute()
	#response = request.execute()

	# set vid_ids to empty list
	vid_ids = []
	# loop through playlists, accessing item key to look over playlists in response
	for item in pl_response['items']:
		# append vid ids to vid ids list	
		vid_ids.append(item['contentDetails']['videoId'])

	# a single query to video resource to grab all videos
	vid_request = youtube.videos().list(
			# part argument to get details from each video//contentDetails
			part="statistics",
			# comma separated value of multiple ids
			id=','.join(vid_ids)
		)

	# Gives us response for video items
	vid_response = vid_request.execute()

	# Loop over response
	for item in vid_response['items']:
		# have to access through each key to reach duration
		vid_views = item['statistics']['viewCount'] #//duration = item['contentDetails']['duration']

		# links to most popular videos after sorted by viewcount
		vid_id = item['id']
		# grab video id, create link
		yt_link = f'https://youtu.be/{vid_id}'

		# appending videos in playlist to list and sorted by vid_views and given a link
		videos.append(
			{
				'views': int(vid_views),
				'url': yt_link
			}
		)

		# search for values, print out
		#hours = hours_pattern.search(duration) //
		#minutes = minutes_pattern.search(duration) //
		#seconds = seconds_pattern.search(duration) //

		# return hours as string, want this value if hours, else 0
		#hours = int(hours.group(1)) if hours else 0 //
		# return minutes as string, want this value if minutes, else 0
		#minutes = int(minutes.group(1)) if minutes else 0 //
		# return seconds as string, want this value if seconds, else 0
		#seconds = int(seconds.group(1)) if seconds else 0 //

		# convert videos to seconds
		#video_seconds = timedelta( //
				#hours = hours, //
				#minutes = minutes, //
				#seconds = seconds //
			#).total_seconds() //

		# Will keep running total of all seconds for each video
		#total_seconds += video_seconds //

	# check if any pages are left
	nextPageToken = pl_response.get('nextPageToken')
	# if none, break loop
	if not nextPageToken:
		break

# sort list in place before we loop over videos, reverse to make highest viewed videos first
videos.sort(key=lambda vid: vid['views'], reverse=True)

for video in videos:
	print(video['url'], video['views'])

# convert total to integers
#total_seconds = int(total_seconds) //
# returns tuple of the quotent
#minutes, seconds = divmod(total_seconds, 60) //
# returns tuple of the quotent
#hours, minutes = divmod(minutes, 60) //

#print(f'{hours}:{minutes}:{seconds}') //