# Build the service Object
from googleapiclient.discovery import build
# Placement of API key
api_key = 'AIzaSyC7DNkq-Pj8794AzQEax1jB_RNzHVLRcM8'
# Connect to youtube service
youtube = build('youtube', 'v3', developerKey=api_key)

# playlist request
pl_request = youtube.playlistItems().list(
		# which part of data you wish to call upon
		part='contentDetails',
		# playlistId
		playlistId="PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"

# You can also add content Details to gather Id from them. 
# Returns a resource for the API route using youtube service
#request = youtube.channels().list(
		# How to look up stats for a channel
#		part='contentDetails, statistics',
		# What channel we are getting stats for
#		forUsername='schafer5'
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
		# part argument to get details from each video
		part="contentDetails",
		# comma separated value of multiple ids
		id=','.join(vid_ids)
	)

# Gives us response for video items
vid_response = vid_request.execute()

# Loop over response
for item in vid_response['items']:
	# have to access through each key to reach duration
	duration = item['contentDetails']['duration']
	print(duration)
	print()

#print(response)