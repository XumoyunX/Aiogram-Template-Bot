import  requests
import json


def instadownloader(link1):
	url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

	querystring = {"url": link1}

	headers = {
		"X-RapidAPI-Key": "c0a036af42msh77e0b69d3927b52p136525jsn108b4b137199",
		"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	rest = json.loads(response.text)
	if 'error' in rest:
		return 'Error'
	else:
		dict = {}
		if rest['Type'] == 'Post-Image':
			dict['type'] = 'image'
			dict['media'] = rest['media']
			return dict
		elif rest['Type'] == 'Post-Video':
			dict['type'] = 'video'
			dict['media'] = rest['media']
			return dict
		elif rest['Type'] == 'Carousel':
			dict['type'] = 'carousel'
			dict['media'] = rest['media']
			return dict
		# print(rest, '\n', dict)
		else:
			return 'error type'



# instadownloader('https://www.instagram.com/reel/CjSGl6hjynW/?igshid=ZDZjYjU5YmM=')