import  requests
import json


def instadownloader(link1):
	url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

	querystring = {"url": link1}

	headers = {
		"X-RapidAPI-Key": "399345e89emsh7740eba922f32c8p15e146jsnc32cea0b5409",
		"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	# print(response.text)
	rest = json.loads(response.text)
	# print(rest)
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
		else:
			return 'Error'

