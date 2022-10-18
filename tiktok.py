


def tk(link):
	import requests
	import json

	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

	querystring = {"url": link}

	headers = {
		"X-RapidAPI-Key": "c0a036af42msh77e0b69d3927b52p136525jsn108b4b137199",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	result = response.text
	rest = json.loads(result)
	return {"video": rest["video"][0],"music": rest["music"][0] }



# "https://v16m-default.tiktokcdn-us.com/908d1289261a0ee6294ca2bd120b738e/6348a150/video/tos/alisg/tos-alisg-pve-0037c001/d0871b37de504c548eab9d552694db5c/?a=0&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&br=1050&bt=525&cs=0&ds=2&ft=_G6uMBnZqq2mo0PQqOVBkVQEpfUzrKJ&mime_type=video_mp4&qs=0&rc=Z2U3ODQ3O2kzNTk7Omc5NUBpM2hyZjo6ZjlpOTMzODczNEAvLjEwMjEuNi8xXjNfNmAxYSMuLjMvcjRncWhgLS1kMS1zcw%3D%3D&l=20221013173456A0387071413808049425"