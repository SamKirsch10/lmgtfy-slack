import falcon
import json
from pyshorteners import Shortener
import requests

class MainResource(object):

	def on_get(self, req, resp):
		"""Handles the GET request to see if API is up"""
		resp.status = falcon.HTTP_200
		resp.body = 'LMGTFY Slack Bot'

	def on_post(self, req, resp):
		"""Handles incomming slack requests and returns lmgtfy link"""
		text = req.get_param('text').decode('ascii')
		token = req.get_param('token').decode('ascii')
		user_id = req.get_param('user_id').decode('ascii')
		channel_id = req.get_param('channel_id').decode('ascii')
		response_url = req.get_param('response_url').decode('ascii')
		print response_url
		url = "http://lmgtfy.com/?q=" + text.replace(" ","+")
		shortener = Shortener('Tinyurl')
		json_response = { 
			"token": token,
			"scope": 'client',
			"response_type": "in_channel",
			"channel": channel_id,
			"text": shortener.short(url),
			"as_user": True,
			"scope": 'chat:write:user'
		}
		resp.body = json.dumps(json_response)


app = falcon.API()
main = MainResource()
app.add_route('/',main)
