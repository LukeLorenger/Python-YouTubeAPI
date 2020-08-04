# Build the service Object
from googleapiclient.discovery import build
# Placement of API key
api_key = 'your API key here'
# Connect to youtube service
youtube = build('youtube', 'v3', developerKey=api_key)
# Returns a resource for the API route using youtube service
request = youtube.channels().list(
		# How to look up stats for a channel
		part='statistics',
		# What channel we are getting stats for
		forUsername='PowerfulJRE'
	)

response = request.execute()

print(response)