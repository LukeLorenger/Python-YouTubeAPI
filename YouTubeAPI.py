# Build the service Object
from googleapiclient.discovery import build
# Placement of API key
api_key = 'AIzaSyC7DNkq-Pj8794AzQEax1jB_RNzHVLRcM8'
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